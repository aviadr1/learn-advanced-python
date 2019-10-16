---
redirect_from:
  - "/01-refresher/notebooks/generic-functions-closures"
interact_link: content/01_refresher/notebooks/generic_functions_closures.ipynb
kernel_name: python3
has_widgets: false
title: 'Generic Functions Closures'
prev_page:
  url: /01_refresher/notebooks/generators.html
  title: 'Generators'
next_page:
  url: /01_refresher/notebooks/reduce.html
  title: 'Reduce'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-advanced-python/blob/master/content/01_refresher/notebooks/generic_functions_closures.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def generic_func(*args, **kwargs):
    print('the positional args are:', args)
    print('the keyword args are:', kwargs)
    


```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
generic_func()

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
the positional args are: ()
the keyword args are: {}
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
generic_func("one", "two", "three", blah=1, moshe=2, test=[1,2,3])

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
the positional args are: ('one', 'two', 'three')
the keyword args are: {'blah': 1, 'moshe': 2, 'test': [1, 2, 3]}
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
len([1,2,3], [1,2,3])

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_traceback_line}
```

    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-6-7407188aa4f7> in <module>
    ----> 1 len([1,2,3], [1,2,3])
    

    TypeError: len() takes exactly one argument (2 given)


```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print(1,2,3,4,5,6,7,8,1,2,34,25,4,5432,5432,5432,5432,5432)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
1 2 3 4 5 6 7 8 1 2 34 25 4 5432 5432 5432 5432 5432
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def test():
    class ToldYou:
        pass
    import math
    x = 10
    def inner():
        print('in inner func')
    return inner
    

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def make_str_factory(s):
    
    def str_factory():
        return s
    
    return str_factory
    

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
smiley_factory = make_str_factory('😊')
hello_factory = make_str_factory('hello')

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
smiley_factory.__closure__

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
(<cell at 0x011302D0: str object at 0x010FF758>,)
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
dir(smiley_factory)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
['__annotations__',
 '__call__',
 '__class__',
 '__closure__',
 '__code__',
 '__defaults__',
 '__delattr__',
 '__dict__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__get__',
 '__getattribute__',
 '__globals__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__kwdefaults__',
 '__le__',
 '__lt__',
 '__module__',
 '__name__',
 '__ne__',
 '__new__',
 '__qualname__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__']
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
hello_factory()

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'hello'
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
class Factory:
    def __init__(self, value):
        self.value = value
        
    def make(self):
        return self.value

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
smiley_factory = Factory('😊')
smiley_factory.make()

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'😊'
```


</div>
</div>
</div>

