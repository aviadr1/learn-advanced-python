---
redirect_from:
  - "/04-writing-our-own-container-types/writing-our-own-container-types"
interact_link: content/04_writing_our_own_container_types/writing_our_own_container_types.ipynb
kernel_name: python3
has_widgets: false
title: '04 writing our own container types'
prev_page:
  url: /03_polymorphism_protocols_and_abcs/polymorphism_protocols_abcs.html
  title: 'Polymorphism Protocols Abcs'
next_page:
  url: /04_writing_our_own_container_types/writing_our_own_container_types.html
  title: 'Writing Our Own Container Types'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-advanced-python/blob/master/content/04_writing_our_own_container_types/writing_our_own_container_types.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




# Creating new collections

We've seen collections like lists, strings and tuples that allow indexed access 

   `mylist[0]`

And we've seen collections like dict and set that allow keyed access

`menu_prices_dict['hamburger'] = 59`

In this chapter we will learn how the magic behind collections and access works
and how to create our own containers or customize existing containers


## Note:
In this lesson we're going to rely heavily on decorators, duck-typing, protocols, and ABCs - which we've covered in lessons 02 and 03



# Iterator protocol

Lets start with one of the simplest python protocols: the __iterator__ protocol.

## [What are iterators in Python?][1]
Iterators are everywhere in Python. They are elegantly implemented within for loops, comprehensions, generators etc. but hidden in plain sight.

Iterator in Python is simply an object that can be iterated upon. An object which will return data, one element at a time.

Technically speaking, Python iterator object must implement two special methods, `__iter__()` and `__next__()`, collectively called the iterator protocol.

An object is called iterable if we can get an iterator from it. Most of built-in containers in Python like: list, tuple, string etc. are iterables.

The iter() function (which in turn calls the `__iter__()` method) returns an iterator from them.

## [Iterator Types][2]
Python supports a concept of iteration over containers. This is implemented using two distinct methods; these are used to allow user-defined classes to support iteration. Sequences, described below in more detail, always support the iteration methods.

One method needs to be defined for container objects to provide iteration support:

`container.__iter__()`
> Return an iterator object. The object is required to support the iterator protocol described below. If a container supports different types of iteration, additional methods can be provided to specifically request iterators for those iteration types. (An example of an object supporting multiple forms of iteration would be a tree structure which supports both breadth-first and depth-first traversal.) This method corresponds to the tp_iter slot of the type structure for Python objects in the Python/C API.

The iterator objects themselves are required to support the following two methods, which together form the iterator protocol:

`iterator.__iter__()`
> Return the iterator object itself. This is required to allow both containers and iterators to be used with the for and in statements. This method corresponds to the tp_iter slot of the type structure for Python objects in the Python/C API.

`iterator.__next__()`
> Return the next item from the container. If there are no further items, raise the StopIteration exception. This method corresponds to the tp_iternext slot of the type structure for Python objects in the Python/C API.

Python defines several iterator objects to support iteration over general and specific sequence types, dictionaries, and other more specialized forms. The specific types are not important beyond their implementation of the iterator protocol.

Once an iterator’s __next__() method raises StopIteration, it must continue to do so on subsequent calls. Implementations that do not obey this property are deemed broken.

[1]: https://www.programiz.com/python-programming/iterator
[2]: https://docs.python.org/3.7/library/stdtypes.html#iterator-types

## Example
Below we show an example class that implements the iterator protocol



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
class VersionedObject :
    """
    VersionedObject is a type that remembers all the past values it held
    and can return the history of its values with a for loop
    """
    def __init__(self, value=None):
        self.__values = [ value ]
        
    def update(self, value):
        self.__values.append(value)

    def latest(self):
        return self.__values[-1]
    
    def __iter__(self):
        return self.Iterator(self.__values)
    
    class Iterator:
        def __init__(self, values):
            self.__index = 0
            self.__values = values
            
        def __next__(self):
            # Return the next item from the container. 
            # If there are no further items, raise the StopIteration exception
            if self.__index is None or len(self.__values) <= self.__index:
                # Once an iterator’s next() method raises StopIteration, it must continue to do so
                self.__index = None 
                raise StopIteration()
            
            value = self.__values[self.__index]
            self.__index += 1
            return value
        
        def __iter__(self):
            # Return the iterator object itself. 
            # This is required to allow both containers and iterators to be used with the for and in statements
            return self #
    
x = VersionedObject([1])
x.update(2)
x.update("third version")
x.update(4)
for older_value in x: # calls the __iter__ method on x
    print(older_value) # calls the __next__ method on the iterator


```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
[1]
2
third version
4
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
"""

Lets simplify the code for VersionObject, by using the fact that lists []
also support the iterator protocol themselves

"""

class VersionedObject_2 :
    def __init__(self, value=None):
        self.__values = [ value ]
        
    def update(self, value):
        self.__values.append(value)

    def latest(self):
        return self.__values[-1]
    
    def __iter__(self):
        return iter(self.__values) # calls self.__values iterator
        
x = VersionedObject_2([1])
x.update(2)
x.update("third version")
x.update(4)
for older_value in x: # calls the __iter__ method on x
    print(older_value) # calls the __next__ method on the iterator


```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
[1]
2
third version
4
```
</div>
</div>
</div>



## [Sequence protocol](https://docs.python.org/3.7/library/stdtypes.html#iterator-types)

There are three basic sequence types: lists, tuples, and range objects.

Sequences support the following operations:


```
Operation             Result

x in s                True if an item of s is equal to x, else False
x not in s            False if an item of s is equal to x, else True
s + t                 the concatenation of s and t
s * n or n * s        equivalent to adding s to itself n times
s[i]                  ith item of s, origin 0
s[i:j]                slice of s from i to j
s[i:j:k]              slice of s from i to j with step k
len(s)                length of s
min(s)                smallest item of s
max(s)                largest item of s
s.index(x[, i[, j]])  index of the first occurrence of x in s (at or after index i and before index j)
s.count(x)            total number of occurrences of x in s
```

This is a rather long list of operations ... 
also it doesn't tell us which methods to implement and how ... 

to help us with this difficult task, python provides an abstract base class(ABC) `collections.abc.Sequence`that implements the most of the sequence protocol and only asks us to implement two abstract function: `__len__` and `__getitem__`

> * if you're interested in the details of how the Sequence class implements other functions such as `index`, `count` or `__contains__` just by using `__len__` and `__getitem__` see the `_collections_abc.py` module in the python standard library 

Lets see `collections.abc.Sequence` in action by implementing an incredibly simple sequence that we're already familiar with - range.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
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
        if isinstance(offset, slice):
            return itertools.islice(self, offset.start, offset.stop, offset.step)
        
        if self.__n <= offset:
            raise IndexError('range object index out of range')
            
        return self.__start + offset * self.__step
    
    def __repr__(self):
        return f"{type(self).__name__}({self.__start},{self.__stop},{self.__step})"

        
# Let's use MyRange 
range5 = MyRange(0, 5)

# convert to list
print(list(range5)) # [0, 1, 2, 3, 4]

# use indexing
print(range5[0], range5[1], range5[2]) # 0 1 2

# use 'in' keyword
print(3 in range5)   # true
print(100 in range5) # false

# min/max/count
print(min(range5)) # 0
print(max(range5)) # 4
print(range5.count(4)) # 1

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
[0, 1, 2, 3, 4]
0 1 2
True
False
0
4
1
```
</div>
</div>
</div>



## [Mapping protocol](https://docs.python.org/3.7/library/stdtypes.html#dict)

A mapping object maps hashable values to arbitrary objects. Mappings are mutable objects. There is currently only one standard mapping type, the dictionary. 

A dictionary’s keys are _almost_ arbitrary values. key have to be __hashable__, which means that keys must be immutable. that is, objects containing lists, dictionaries or other mutable types may not be used as keys.

mappings should support the following operations:
```
len(d)
    Return the number of items in the dictionary d.

d[key]
    Return the item of d with key key. Raises a KeyError if key is not in the map.
    
d[key] = value
    Set d[key] to value.

del d[key]
    Remove d[key] from d. Raises a KeyError if key is not in the map.

key in d
    Return True if d has a key key, else False.

key not in d
    Equivalent to not key in d.

iter(d)
    Return an iterator over the keys of the dictionary. This is a shortcut for iter(d.keys()).

clear()
    Remove all items from the dictionary.

copy()
    Return a shallow copy of the dictionary.

@classmethod 
fromkeys(iterable[, value])
    Create a new dictionary with keys from iterable and values set to value.

get(key[, default])
    Return the value for key if key is in the dictionary, else default. 
    If default is not given, it defaults to None, so that this method never raises a KeyError.

items()
    Return a new view of the dictionary’s items ((key, value) pairs). See the documentation of view objects.

keys()
    Return a new view of the dictionary’s keys. See the documentation of view objects.

pop(key[, default])
    If key is in the dictionary, remove it and return its value, else return default. 
    If default is not given and key is not in the dictionary, a KeyError is raised.

popitem()
    Remove and return a (key, value) pair from the dictionary. Pairs are returned in LIFO order.

setdefault(key[, default])
    If key is in the dictionary, return its value. If not, insert key with a value of default and return default. 
    default defaults to None.

update([other])
    Update the dictionary with the key/value pairs from other, overwriting existing keys. Return None.

values()
    Return a new view of the dictionary’s values.  
```

### 😱

Yes, that's quite a big number of things. again, the `collections` module has a class called `MutableMapping` which takes care of most things and only asks that we implement `__getitem__, __setitem__, __delitem__, __iter__, and __len__` functions


### Example
Lets use `MutableMapping` to create a new type of dictionary, one that sends a message to observers whenever it changes



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
from collections.abc import MutableMapping

class Observable: # from ex 02
    def __init__(self):
        self.handlers = []
    
    def register(self, callable_):
        self.handlers.append(callable_)
        
    def notify(self, event, *args, **kwargs):
        for handler in self.handlers:
            handler(event, *args, **kwargs)
            
class ObservableMapping(MutableMapping):
    def __init__(self, dict_ = {}, dicttype = None):
        dicttype = dicttype or type(dict_)
        self.data = dicttype(dict_)
        self.events = Observable()
        
    def __setitem__(self, key, value):
        self.events.notify('set', self, key, value)
        return self.data.__setitem__(key, value)
        
    def __delitem__(self, key):
        self.events.notify('del', self, key)
        return self.data.__delitem__(key)
                
    def __getitem__(self, key):
        return self.data.__getitem__(key)
    
    def __iter__(self):
        return self.data.__iter__()
    
    def __len__(self):
        return self.data.__len__()
    
def handler(event, obj, key, *args, **kwargs):
    print(event, repr(key), '-->>', *args, **kwargs)
    
d = ObservableMapping()
d.events.register(handler)
d['name'] = 'Sir Launcelot of Camelot'
d['favorite color'] = 'blue'
d.popitem()


```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
set 'name' -->> Sir Launcelot of Camelot
set 'favorite color' -->> blue
del 'name' -->>
```
</div>
</div>
<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
('name', 'Sir Launcelot of Camelot')
```


</div>
</div>
</div>

