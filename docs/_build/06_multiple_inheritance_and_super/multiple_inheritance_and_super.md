---
redirect_from:
  - "/06-multiple-inheritance-and-super/multiple-inheritance-and-super"
interact_link: content/06_multiple_inheritance_and_super/multiple_inheritance_and_super.ipynb
kernel_name: python3
has_widgets: false
title: '06 multiple inheritance and super'
prev_page:
  url: /05_more_on_classes_and_objects/exercise/solutions.html
  title: 'Solutions'
next_page:
  url: /06_multiple_inheritance_and_super/multiple_inheritance_and_super.html
  title: 'Multiple Inheritance And Super'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-advanced-python/blob/master/content/06_multiple_inheritance_and_super/multiple_inheritance_and_super.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




### super() and multiple inheritance

Lets consider a complicated diamond multiple inheritance scenario.

>> _hint_: multiple inheritance is not trivial to implement, and this example will show super() is not a silver bullt



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
class A:
    def __init__(self):
        print("A")

class B:
    def __init__(self):
        print("B")

class C(A):
    def __init__(self, arg):
        print("C","arg=",arg)
        A.__init__(self)

class D(B):
    def __init__(self, arg):
        print("D", "arg=",arg)
        B.__init__(self)

class E(C,D):
    def __init__(self, arg):
        print("E", "arg=",arg) 
        C.__init__(self, arg)
        D.__init__(self, arg)

E(10)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
E arg= 10
C arg= 10
A
D arg= 10
B
```
</div>
</div>
<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
<__main__.E at 0x68b1fd0>
```


</div>
</div>
</div>



we want to rewrite this example using super()

> super() actually returns a proxy object that understands the _MRO_ of the object <br>
> and will call the _next_ function in the hierarchy, like so:

![class diagram](https://fuhm.net/super-harmful/example1-2.png)



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
class A:
    def __init__(self):
        print("A")
        super().__init__()

class B(object):
    def __init__(self):
        print("B")
        super().__init__()

class C(A):
    def __init__(self, arg):
        print("C","arg=",arg)
        super().__init__()

class D(B):
    def __init__(self, arg):
        print("D", "arg=",arg)
        super().__init__()

class E(C,D):
    def __init__(self, arg):
        print("E", "arg=",arg)
        super().__init__(arg)

print("MRO:", [x.__name__ for x in E.__mro__])
E(10) # this won't work


```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
MRO: ['E', 'C', 'A', 'D', 'B', 'object']
E arg= 10
C arg= 10
A
```
</div>
</div>
<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_traceback_line}
```

    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-2-7c928c6c4b55> in <module>
         25 
         26 print("MRO:", [x.__name__ for x in E.__mro__])
    ---> 27 E(10) # this won't work
    

    <ipython-input-2-7c928c6c4b55> in __init__(self, arg)
         22     def __init__(self, arg):
         23         print("E", "arg=",arg)
    ---> 24         super().__init__(arg)
         25 
         26 print("MRO:", [x.__name__ for x in E.__mro__])


    <ipython-input-2-7c928c6c4b55> in __init__(self, arg)
         12     def __init__(self, arg):
         13         print("C","arg=",arg)
    ---> 14         super().__init__()
         15 
         16 class D(B):


    <ipython-input-2-7c928c6c4b55> in __init__(self)
          2     def __init__(self):
          3         print("A")
    ----> 4         super().__init__()
          5 
          6 class B(object):


    TypeError: __init__() missing 1 required positional argument: 'arg'


```
</div>
</div>
</div>



#### What's happening here?

![class diagram](https://fuhm.net/super-harmful/example1-2.png)

```
<ipython-input-32-7c928c6c4b55> in __init__(self)
      2     def __init__(self):
      3         print("A")
----> 4         super().__init__()
      5 
      6 class B(object):

TypeError: __init__() missing 1 required positional argument: 'arg'
```

Look at the MRO:
```
MRO: ['E', 'C', 'A', 'D', 'B', 'object']
```

looks like A's `__init__` function is calling D's `__init__ ` function, even though A does not inherit from D ... this makes sense since we want to make sure that all the `__init__` functions in the hierarchy are being called exactly once ... 

> _super does not call your superclass. You must be prepared to call any other class's method in the hierarchy and be prepared to be called from any other class's method._

but how do we solve the issue?




##### using super() in a multiple inheritance setting
We need to keep to principles in mind:

1. `super()`  usage has to be consistent: In a class hierarchy, super should be used everywhere or nowhere. is part of the contract of the class. if one classes uses `super()` all the classes _MUST_ also use `super()` in the same way, or otherwise we might call certain functions in the hierarchy zero times, or more than once <br><br>

1. to correctly support `__init__` functions with any parameters, the top-level classes in your hierarchy must inherit from a custom class like SuperObject:

    ```
    # module superobject in this repository
    class SuperObject:        
        def __init__(self, **kwargs):
            mro = type(self).__mro__
            assert mro[-1] is object
            if mro[-2] is not SuperObject:
                raise TypeError(
                    'all top-level classes in this hierarchy must inherit from SuperObject',
                    'the last class in the MRO should be SuperObject',
                    f'mro={[cls.__name__ for cls in mro]}'
                )

            # super().__init__ is guaranteed to be object.__init__        
            init = super().__init__
            init()
            
    def super_call(self, super_, funcname, **kwargs):
        """
        cooperatively calls a function on super. 
        usage:
            self.super_call(super(), 'my_method_name', param1='example', param2='whatever')
        """
        super_func = getattr(super_, funcname, None)
        if super_func is not None:
            return super_func(**kwargs)

    ```
   > i've added SuperObject to a module in this git repository
   > you can use SuperObject in your own code by importing it:
   ```
   from superobject import SuperObject
   ```

1. when calling functions on `super()` make sure you take into account the fact that `class object` may not have that function and therefore the call might fail. avoid this by using a function like `SuperObject.super_call()` <br><br>

1. if a overriden functions in the class hierarchy can take differing arguments, always pass all arguments you received on to the super function as keyword arguments, and, always accept **kwargs.

For more details, see my writeup [super() and changing the signature of cooperative methods](https://stackoverflow.com/a/56714809/52917)




#### Example rewritten to support these principles



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
from superobject import SuperObject 

class A(SuperObject):
    def __init__(self, **kwargs):
        print("A")
        super(A, self).__init__(**kwargs)
        
    def test(self, param1, **kwargs):
        self.super_call(super(), 'test', param1=param1, **kwargs)
        print("A", 'test', f"param1={param1}")

class B(SuperObject):
    def __init__(self, **kwargs):
        print("B")
        super(B, self).__init__(**kwargs)
        
    def test(self, param2, **kwargs):
        self.super_call(super(), 'test', param2=param2, **kwargs)
        print("B", 'test', f"param2={param2}")

class C(A):
    def __init__(self, age, **kwargs):
        print("C",f"age={age}")
        super(C, self).__init__(age=age, **kwargs)
        
    def test(self, param1, param3, **kwargs):
        self.super_call(super(), 'test', param1=param1, param3=param3, **kwargs)
        print("C", 'test', f"param1={param1}", f"param3={param3}")
        
        
class D(B):
    def __init__(self, name, **kwargs):
        print("D", f"name={name}")
        super(D, self).__init__(name=name, **kwargs)
        
    def test(self, param2, param4, **kwargs):
        self.super_call(super(), 'test', param2=param2, param4=param4, **kwargs)
        print("D", 'test', f"param2={param2}", f"param4={param4}")

class E(C,D):
    def __init__(self, name, age, *args, **kwargs):
        print( "E", f"name={name}", f"age={age}")
        super(E, self).__init__(name=name, age=age, *args, **kwargs)

e = E(name='python', age=28)
print()

e.test(param1='p1', param2='p2', param3='p3', param4='p4')

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
E name=python age=28
C age=28
A
D name=python
B
SuperObject

B test param2=p2
D test param2=p2 param4=p4
A test param1=p1
C test param1=p1 param3=p3
```
</div>
</div>
</div>

