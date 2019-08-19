---
redirect_from:
  - "/04-writing-our-own-container-types/exercise/solutions"
interact_link: content/04_writing_our_own_container_types/exercise/solutions.ipynb
kernel_name: python3
has_widgets: false
title: 'Solutions'
prev_page:
  url: /04_writing_our_own_container_types/exercise/questions.html
  title: 'Questions'
next_page:
  url: /05_more_on_classes_and_objects/more_on_classes_and_objects.html
  title: '05 more on classes and objects'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-advanced-python/blob/master/content/04_writing_our_own_container_types/exercise/solutions.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




# supporting slices in MyRange class

note that the MyRange class in lecture 04 does not support slices

```
range10 = MyRange(10)
range10[::2]
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-5-2886954a11eb> in <module>
      8 
      9 range10 = MyRange(0, 10)
---> 10 list(range10[::2])

<ipython-input-2-25399ac18a9d> in __getitem__(self, offset)
     13 
     14     def __getitem__(self, offset):
---> 15         if self.__n <= offset:
     16             raise IndexError('range object index out of range')
     17 

TypeError: '<=' not supported between instances of 'int' and 'slice'
```

create a new class `MyRange2` that inherits from MyRange and adds support of slices

HINT: use the class `islice` from the module `itertools`

expected output:

      >>> range10 = MyRange2(0, 10)
      >>> list(range10[::2])
      [0, 2, 4, 6, 8]




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
### useful starting point
import collections.abc
import math
class MyRange(collections.abc.Sequence):
    def __init__(self, start, stop, step=1):
        self.__start = start
        self.__stop = stop
        self.__step = step
        self.__n = max(0, math.ceil((stop-start) / step))
        super().__init__()
        
    def __len__(self):
        return self.__n
    
    def __getitem__(self, offset):
        if self.__n <= offset:
            raise IndexError('range object index out of range')
            
        return self.__start + offset * self.__step
    
    def __repr__(self):
        return f"{type(self).__name__}({self.__start},{self.__stop},{self.__step})"


```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
import itertools

class MyRange2(MyRange):    
    def __getitem__(self, offset):
        if isinstance(offset, slice):
            return itertools.islice(self, offset.start, offset.stop, offset.step)
        return MyRange.__getitem__(self, offset)
    
range10 = MyRange2(0, 10)
list(range10[::2])

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
[0, 2, 4, 6, 8]
```


</div>
</div>
</div>



# 3x3 matrix

Write a class called Matrix that represents a simple 3x3 matrix. 

namely it should support the following operations:
you do not need to derive from any ABC

```
>>> m = Matrix()
>>> print(m)
[0, 0, 0]
[0, 0, 0]
[0, 0, 0]

>>> m[0,0] = 10
>>> print(m)
[10, 0, 0]
[0, 0, 0] 
[0, 0, 0]

>>> m[1,1] = 100
>>> m[1,1]
100
```







<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
 class Matrix:
    def __init__(self):
        self.data = [ [0, 0, 0], [0,0,0], [0,0,0] ]
    
    def __getitem__(self, key):
        x, y = key
        return self.data[x][y]
    
    def __setitem__(self, key, value):
        x, y = key
        self.data[x][y] = value
        
    def __len__(self):
        return 9
    
    def __repr__(self):
        return '\n'.join([repr(row) for row in self.data])
    
    def __iter__(self):
        for row in self.data:
            for x in row:
                yield x
    
m = Matrix()
print(m)
print()

m[0,0] = 10
print(m)
print()

m[1,1] = 100
print(m[1,1]) # 1o0
print()

for i in m:
    print(i)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
[0, 0, 0]
[0, 0, 0]
[0, 0, 0]

[10, 0, 0]
[0, 0, 0]
[0, 0, 0]

100

10
0
0
0
100
0
0
0
0
```
</div>
</div>
</div>

