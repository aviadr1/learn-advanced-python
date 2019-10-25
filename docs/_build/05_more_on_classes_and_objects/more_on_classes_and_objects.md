---
redirect_from:
  - "/05-more-on-classes-and-objects/more-on-classes-and-objects"
interact_link: content/05_more_on_classes_and_objects/more_on_classes_and_objects.ipynb
kernel_name: python3
has_widgets: false
title: 'More On Classes And Objects'
prev_page:
  url: /05_more_on_classes_and_objects/more_on_classes_and_objects.html
  title: '05 more on classes and objects'
next_page:
  url: /05_more_on_classes_and_objects/exercise/questions.html
  title: 'exercise'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-advanced-python/blob/master/content/05_more_on_classes_and_objects/more_on_classes_and_objects.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
class Person:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f"{type(self).__name__}({self.name!r})"
    def walk(self):
        print(self.name, 'walking')
    def run(self):
        print(self.name,'running')
    def swim(self):
        print(self.name,'swimming')
        
class OlympicRunner(Person):
    def run(self):
        print(self.name,self.name,"running incredibly fast!")
        
    def show_medals(self):
        print(self.name, 'showing my olympic medals')
    
def train(person):
    person.walk()
    person.swim()
    person.run()
    
terry = Person('Terry Gilliam')
graham = Person('Graham Chapman')
train(terry)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
Terry Gilliam walking
Terry Gilliam swimming
Terry Gilliam running
```
</div>
</div>
</div>



## Constructors are inheritable

we define a constructor in class `Person`, notice how since I didnt redefine the constructor 
in `OlympicRunner` I can reuse it



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
usainbolt = OlympicRunner('Usain Bolt')
usainbolt

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
OlympicRunner('Usain Bolt')
```


</div>
</div>
</div>



## Bound and unbound methods
### Umbound methods



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# what's heppening here
terry.swim()

# its actually equivalent to:
Person.swim(terry)

# we can take the function swim out of the Person class
swim = Person.swim

# this is called an unbound function - it is not glued to a particular object
print(swim) # <function Person.swim at 0x06737228>

# we can call it on any person
swim(terry)
swim(graham)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
Terry Gilliam swimming
Terry Gilliam swimming
<function Person.swim at 0x0612F468>
Terry Gilliam swimming
Graham Chapman swimming
```
</div>
</div>
</div>



### Bound methods



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# lets take the function 'swim' from terry
terry_swim = terry.swim
print(terry_swim) # <bound method Person.swim of Person('Terry Gilliam')>

# this function is bound to Terry Gilliam. 
# the 'self' parameter has been determined - we dont need any parameters
terry_swim()

try:
    terry_swim(graham)
except Exception as ex:
    print('you cannot change the object:', ex)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
<bound method Person.swim of Person('Terry Gilliam')>
Terry Gilliam swimming
you cannot change the object: swim() takes 1 positional argument but 2 were given
```
</div>
</div>
</div>



## Monkey-patching methods to a class or instance

* We can monkey-patch classes (change classes at run time) by just adding function to the class
* We can 'trick' functions to think they are methods of a class, bound to a particular object
* We can add methods to a particular object

> This works through the magic of 'descriptors' i.e. objects that know who owns them \[ [more details](https://docs.python.org/3.7/howto/descriptor.html) \]



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def sing(self):
    print(self, 'is singing')

# add sing() method to Person class
# from this moment on, any Person object also has a sing() method 
Person.sing = sing
print(sing)
print(terry.sing)
terry.sing()
print()

# can we add functions to a particular instance?
# just putting a function in an instance does not bind it to the instance
print(train) # the train() function
usainbolt.train = train
try:
    usainbolt.train() # this won't work
except Exception as ex:
    print('the train function is not bound:', ex, '\n')
    
# here's how we can can do it
# bind the function `train` to think it bound to usainbolt
train_usain = train.__get__(usainbolt, type(usainbolt))
print(train_usain)
train_usain()
usainbolt.train = train_usain
usainbolt.train()

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
<function sing at 0x0612F198>
<bound method sing of Person('Terry Gilliam')>
Person('Terry Gilliam') is singing

<function train at 0x0612F2B8>
the train function is not bound: train() missing 1 required positional argument: 'person' 

<bound method train of OlympicRunner('Usain Bolt')>
Usain Bolt walking
Usain Bolt swimming
Usain Bolt Usain Bolt running incredibly fast!
Usain Bolt walking
Usain Bolt swimming
Usain Bolt Usain Bolt running incredibly fast!
```
</div>
</div>
</div>



## Where is everything?

* the attributes of each instance are stored in a `__dict__` attribute
* the class of an instance is stored in the `__class__` attribute
* methods are usually stored in the `__dict__` object of the class
* base classes are stored in the `__base__` and `__bases__` atrributes of the class

It gets a bit more complicated though:
* an object can have a `__slots__`  variable instead of a `__dict__` this is used to save memory [more details](https://stackoverflow.com/questions/472000/usage-of-slots)
* an object can have a `__getattr__` (or `__getattribute__`) function to return additional attributes [more details](https://stackoverflow.com/questions/4295678/understanding-the-difference-between-getattr-and-getattribute)



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
from pprint import pprint
pprint(usainbolt.__dict__)
print()

pprint(usainbolt.__class__) # OlympicRunner
pprint(OlympicRunner.__dict__)
print()

pprint(OlympicRunner.__base__)
pprint(Person.__dict__)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
{'name': 'Usain Bolt',
 'train': <bound method train of OlympicRunner('Usain Bolt')>}

<class '__main__.OlympicRunner'>
mappingproxy({'__doc__': None,
              '__module__': '__main__',
              'run': <function OlympicRunner.run at 0x0612F300>,
              'show_medals': <function OlympicRunner.show_medals at 0x0612F4B0>})

<class '__main__.Person'>
mappingproxy({'__dict__': <attribute '__dict__' of 'Person' objects>,
              '__doc__': None,
              '__init__': <function Person.__init__ at 0x0612F348>,
              '__module__': '__main__',
              '__repr__': <function Person.__repr__ at 0x0612F390>,
              '__weakref__': <attribute '__weakref__' of 'Person' objects>,
              'run': <function Person.run at 0x0612F420>,
              'sing': <function sing at 0x0612F198>,
              'swim': <function Person.swim at 0x0612F468>,
              'walk': <function Person.walk at 0x0612F3D8>})
```
</div>
</div>
</div>



## Testing if an object has an attribute

To get an attribute `x` from an object `obj`, we can easily just write `obj.x`
but what if the object doesn't have the x property? then `obj.x` will throw an exception
```
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-42-5a93966dfc11> in <module>
----> 4 obj.x

AttributeError: object has no attribute 'x'
```

how can we test for an attribute? we can either catch the exception, or use the `getattr()` function:
```
getattr(object, name[, default]) -> value
```



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
run = getattr(usainbolt, 'run') # equivalent to usainbolt.run
print(run)

time_machine = attribute_usain_doesnt_have = getattr(usainbolt, 'time_machine', None)
print(time_machine) if time_machine is not None else print('no time machine yet')

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
<bound method OlympicRunner.run of OlympicRunner('Usain Bolt')>
no time machine yet
```
</div>
</div>
</div>



## inspecting objects

the `dir` function is useful when inspecting objects in an interactive environment - it is designed to return the most 'interesting' things in an object. 
but it is not necessarily complete or consistent, and may change between versions
  
if are writing reflection code to iterate through other objects, we need something more consistent and powerful - the `inspect` module \[ [more details](https://docs.python.org/3/library/inspect.html) \]



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
import inspect
pprint(inspect.getfile(inspect)) # what .py created this module?
print()

pprint(inspect.getmembers(usainbolt, inspect.ismethod)) # get methods of usainbolt
print()

pprint(inspect.signature(train)) # returns the parameters of the function train()
print()

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
'c:\\users\\aviad\\appdata\\local\\programs\\python\\python37-32\\lib\\inspect.py'

[('__init__', <bound method Person.__init__ of OlympicRunner('Usain Bolt')>),
 ('__repr__', <bound method Person.__repr__ of OlympicRunner('Usain Bolt')>),
 ('run', <bound method OlympicRunner.run of OlympicRunner('Usain Bolt')>),
 ('show_medals',
  <bound method OlympicRunner.show_medals of OlympicRunner('Usain Bolt')>),
 ('sing', <bound method sing of OlympicRunner('Usain Bolt')>),
 ('swim', <bound method Person.swim of OlympicRunner('Usain Bolt')>),
 ('train', <bound method train of OlympicRunner('Usain Bolt')>),
 ('walk', <bound method Person.walk of OlympicRunner('Usain Bolt')>)]

<Signature (person)>

```
</div>
</div>
</div>



## Which method will get called?

When calling a function that exists in both a base class (`Person.run()`) and in a derived class (`OlympicRunner.run()`) which function will actually be called?

* the function that will be called depends on the type of the object and the **Method Resolution Order** or *MRO* - (see example below). 
* when calling `usainbolt.run()` python will access `type(usainbolt).__mro__` to get at the list of classes in the object's inheritance tree. 
* python will iterate through this list of classes, looking for the method `run` and returns the method from the first class that has this method.

the property of having a different function called depending on the type of the object and its location in an inheritance tree is a well-known OO principle that goes by many names:

* Polymorphism
* Virtual functions
* Liskov-Substition principle
* Single dispatch

>> _in python, all methods are 'virtual'_



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# objects of type Person first look for methods in class Person, then in class object
print(Person.__mro__, '\n')

# objects of type OlympicRunner first look for methods in class OlympicRunner, then in Person, then in class object
print(OlympicRunner.__mro__, '\n')

terry.swim()     # Person.swim(terry)
usainbolt.swim() # Person.swim(usainbolt)
terry.run()      # Person.run()
usainbolt.run()  # OlympicRunner.run(usainbolt)


```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
(<class '__main__.Person'>, <class 'object'>) 

(<class '__main__.OlympicRunner'>, <class '__main__.Person'>, <class 'object'>) 

Terry Gilliam swimming
Usain Bolt swimming
Terry Gilliam running
Usain Bolt Usain Bolt running incredibly fast!
```
</div>
</div>
</div>



## Accessing your base class(es)
### The explicit method

Sometimes when inheriting a class we want to override a function, while still reusing the implementation of the base class.
we can do so by explitily referring naming the unbound name of the function we want to use from the base class:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
class InstagramCelebrity(Person):        
    def run(self):
        Person.run(self) # call the run() method defined in class Person
        print(self.name, 'taking picture and uploading to instagram')

kardashian = InstagramCelebrity('Kardashian')
kardashian.run()

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
Kardashian running
Kardashian taking picture and uploading to instagram
```
</div>
</div>
</div>



### using super()

> What if we don't want to explicitly write the name of the base class? `super()` can help with that

consider these two scenarios:
1. Notice in the example above how we've not followed the _DRY_ principle (Don't Repeat Yourself) and explicitly referred to class `Person` in `InstagramCelebrity.run()`? what if we later decided that `InstagramCelebrity` should not inherit directly from `Person` but rather inherit from (say) `Celebrity`? we would need to change the run() method to call `Celebrity.run(self)` instead, but we might forget to do so. <br><br>

2. What if we have a complicated _diamond-shape multiple inheritance_ and we're not sure what's the right base class to call?

Lets first focus on scenario 1, where we don't really need to know much about how `super()` works. <br>
in the example below works exactly the same as the example above, except it uses `super()` instead of an explicit `Person.` notation




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
class InstagramCelebrity(Person):        
    def run(self):
        super().run() # calls the run() on the first base class that has a run() function
        print(self.name, 'taking picture and uploading to instagram')

kardashian = InstagramCelebrity('Kardashian')
kardashian.run()

```
</div>

</div>



### Super and multiple inheritance
we'll talk about how super() interacts with multiple inheritance in lesson 06



# class scope: code and variables

consider the following code:

```
class Comedian(Person):
    funny_level = 0
```
what's happening here? when is this code run? where does the `funny_level` attribute live?

1. code inside a class scope is run at the time the class is defined, **NOT** when an instance is created
2. variables defined at class scope, including methods defined using `def` or any other variables, end up as attributes of the class in its `__dict__` 



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
class Comedian(Person):
    # this code is run NOW, when this class is being defined
    funny_level = 0

# therefore we can access Comedian.funny_level even BEFORE creating any instances
print(Comedian.funny_level) # 0
pprint(Comedian.__dict__) # funny_level is an attribute of Comedian class
Comedian.funny_level = 50

# create a comedian instance
eric = Comedian('Eric Idle')

#  eric doesn't its own funny_level attribute
pprint(eric.__dict__)

# eric.funny_level actually returns Comedian.funny_level
print(eric.funny_level) # 50 

# when we're assigning a value to eric.funny_level, we're actually ADDING a new attribute to eric's __dict__
eric.funny_level = 100
pprint(eric.__dict__)
print(eric.funny_level) # 100
print(Comedian.funny_level) # unchanged, it is still 50


```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
0
mappingproxy({'__module__': '__main__', 'funny_level': 0, '__doc__': None})
{'name': 'Eric Idle'}
50
{'funny_level': 100, 'name': 'Eric Idle'}
100
50
```
</div>
</div>
</div>



## What kind of code can we run at class scope?

Answer: **any legal python code** can be written at class scope, including:
* defining functions (obviously)
* defining variables
* creating inner classes
* calling functions or print
* even run loops! 



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def show_dict_helper(dict_): return [ k for k in dict_ if not k.startswith('__')]

class Test:
    
    print("computing squares:")
    squares = []
    for i in range(10):
        squares.append(i**2)
    print("finished computing squares:", squares)
        
    class InnerClass:
        print("Defining an inner function now")
        
    def myfunc(self):
        pass

        
print()        
pprint(Test.squares)
pprint(show_dict_helper(Test.__dict__)) # ['squares', 'i', 'InnerClass', 'myfunc']      

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
computing squares:
finished computing squares: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
Defining an inner function now

[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
['squares', 'i', 'InnerClass', 'myfunc']
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
## How is it different from __init__ methods?
class Comedian2(Person):
    
    # code to *define* the __init__ function runs *now*
    # the __init__ function goes into Comedian2.__dict__
    def __init__(self, name, funny_level):
        # this code runs only when we are creating an instance
        # name, funny_level end up in the instance's dict
        self.name = name
        self.funny_level = funny_level
        
eric2 = Comedian2('Eric Idle', funny_level=100)

# now Comedian2 only has attributes related to the class
pprint(Comedian2.__dict__) # mostly just __init__

# and our instance eric2 has all the attributes related to instances
pprint(eric2.__dict__) # 'name' and 'funny_level'



```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
mappingproxy({'__doc__': None,
              '__init__': <function Comedian2.__init__ at 0x067ADA08>,
              '__module__': '__main__'})
{'funny_level': 100, 'name': 'Eric Idle'}
```
</div>
</div>
</div>



# using `__getattr__()` to dynamically support more attributes

python is incredibly dynamic and extensible. a class can handle requests for attributes even if they don't actual "exist" in the class by implementing the `__getattr__` function. this can be useful in many design patterns such as `Composition` or `Proxy` as we will see in the next chapter.

> The notebook **ex 05 - questions** has a question about `__setattr__()`

meanwhile, lets look at a silly example of an `ImprovComedian` class that returns random jokes for every attribute that isn't found in the class



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
import random
class ImprovComedian(Comedian2):
    JOKES = [
        'why is 10 afraid of 7? because 7 8 9',
        'How did 10 die ? he was in the middle of 9 11',
        "What's the difference between insomnia and amnesia? " \
            "I stayed up all night yesterday trying to remember ...",
        "what's a freudian slip? its when you mean one thing but you say your mother"
    ]
        
    # return random joke for every attribute that doesn't already exist in the class
    def __getattr__(self, name):
        return f"so regarding {name}... " + random.choice(type(self).JOKES)    

    
seinfeld = ImprovComedian('Seinfeld', 100)
print(seinfeld.name, seinfeld.funny_level) # normal attributes continue to work

# when you ask for attributes that "don't exist" __getattr__ gets called
print(seinfeld.numbers)
print(seinfeld.sleep)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
Seinfeld 100
so regarding numbers... what's a freudian slip? its when you mean one thing but you say your mother
so regarding sleep... What's the difference between insomnia and amnesia? I stayed up all night yesterday trying to remember ...
```
</div>
</div>
</div>

