---
redirect_from:
  - "/03-polymorphism-protocols-and-abcs/polymorphism-protocols-abcs"
interact_link: content/03_polymorphism_protocols_and_abcs/polymorphism_protocols_abcs.ipynb
kernel_name: python3
has_widgets: false
title: 'Polymorphism Protocols Abcs'
prev_page:
  url: /03_polymorphism_protocols_and_abcs/polymorphism_protocols_abcs.html
  title: '03 polymorphism protocols and abcs'
next_page:
  url: /04_writing_our_own_container_types/writing_our_own_container_types.html
  title: '04 writing our own container types'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-advanced-python/blob/master/content/03_polymorphism_protocols_and_abcs/polymorphism_protocols_abcs.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




# Abstract Base Classes (ABCs)

In this lesson we will learn about what polymorphism is, what protocols are, and how Abstract Base Classes (ABCs) help
us correctly implement protocols. 

lets start by understanding polymorphism

## Polymorphism
Polymorphism is the ability to define a an operation or function that can work, without modifications, on objects of more than one type. 

Polymorphism is an Object Oriented Design (OOD) concept. and as we know, python is highly OO oriented, so it should come as no surprise that polymorphism is inherent to python, and that without realizing it, we have been using polymorphism extensively already



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# the len function is polymorphic - 
# it works on many copntainer-like types - dicts, lists, strings, ranges etc
u = len({"one": 'is the loneliest number'}) # 1
x = len([1,2,3]) # 3
y = len("hello") # 5
z = len(range(10)) # 10
print(u, x, y, z, '\n', sep='\n')

# the max function is polymorphic, it works on many container-like types
x = max([1,2, 3, 2, 1]) # 3
y = max('hello') # 'o'
z = max( (('avram', 'cohen'), ('beni', 'levi'), ('zvi', 'arad'), ('moshe', 'zamir')) )
print(x, y, z, '\n',sep='\n')

# the print function is polymorphic - it works on *any* type
import math
print(1, {2}, [3], range(4), '5', len, math, math.sin, sep='\n') 

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
1
3
5
10


3
o
('zvi', 'arad')


1
{2}
[3]
range(0, 4)
5
<built-in function len>
<module 'math' (built-in)>
<built-in function sin>
```
</div>
</div>
</div>



### Writing our own polymorphic functions
How can we write our own polymorphic functions?
easy, any python function we write is _always_ polymorphic 

> Any python function is polymorphic in the sense that you _can_ try to call it with any parameter regardless of its type. to understand wether or not the function will have the desired effect (or would perhaps simply fail by raising an exception), requires us to understand  _Protocols_ - which are discussed below

here's an easy example:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def add(x,y):
    return x+y

# our function add() is polymorphic, it works on many types and combination of types
u = add( 0.25, 0.75) # 1.0
x = add(1, 2) # 3
y = add([1,2,3], [4, 5]) # [1,2,3,4,5]
z = add( 'hello ', ' world') # 'hello  world'
print(u,x,y,z, '\n', sep='\n')


```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
1.0
3
[1, 2, 3, 4, 5]
hello  world


```
</div>
</div>
</div>



Obviously, this function is not going to work for just __any__ type or combination of types

```
add(10, 'hello') 

---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-14-d1478ef3d713> in <module>
----> 1 add(10, 'hello') # TypeError: unsupported operand type(s) for +: 'int' and 'str'

<ipython-input-12-396b6352e406> in add(x, y)
      1 def add(x,y):
----> 2     return x+y
      3 
      4 # our function add() is polymorphic, it works on many types and combination of types
      5 u = add( 0.25, 0.75) # 1

TypeError: unsupported operand type(s) for +: 'int' and 'str'

```

lets explore how this works in more detail 

### A classical object oriented example

Lets imagine we are writing program for a zoo where we keep a bunch of animals. 
We have a class for each type of animal, and we keep a list of all the animals living in the zoo.

some of the animals are similar to ducks: such as `Duck`, `Mallard` and `Goose` <br>
Some are not similar to ducks such as : `Elephant` and `Lion`



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
#
# define some of the animal types in our zoo and what each can do
#

class Duck:
    def walk(self):
        print('duck walking here')
        
    def quack(self):
        print('duck quacks')
        
class Goose: # a goose is also very similar to a duck
    def walk(self):
        print('goose walking here')
        
    def quack(self):
        print('goose quacks')

class Elephant:
    def walk(self):
        print('elephant walk')
        
class Lion:
    def nap(self):
        print('lion napping')
        
# create a list of the animals in our zoo
all_animals = [Duck(), Elephant(), Lion(), Goose()]

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
#
# now lets write some functions to take care of animals and especially ducks in our zoo
#

def animal_type_name(animal):
    return animal.__class__.__qualname__

def feed_animal(animal, food):
    print('giving', food, 'to', animal_type_name(animal))

def treat_the_ducks(animals):
    """
    treat the ducks finds all the ducks in the list of given animals and:
    1. gives them proper exercise - walking and quacking
    2. feeds them with appropriate duck food
    """
    
    for animal in animals:
        print()
        print(animal_type_name(animal), ':')
        try:
            animal.walk() # walks like a duck?
            animal.quack() # talks like a duck?
        except:
            continue # this is not a duck, go to next animal
        
        # its a duck!, so give it some duck food
        duck = animal
        feed_animal(duck, 'duck food')
        
        
# lets feed the ducks    
treat_the_ducks(all_animals)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```

Duck :
duck walking here
duck quacks
giving duck food to Duck

Elephant :
elephant walk

Lion :

Goose :
goose walking here
goose quacks
giving duck food to Goose
```
</div>
</div>
</div>



What's happening here?
We're going through a list of animals, and trying to __polymorphically__ call methods related to ducks on each animal, regardless of their actual type
```
animal.walk() # walks like a duck?
animal.quack() # talks like a duck?
```

python implements polymorphism in a way that's humorously called __duck-typing__ (or more formally as _Ad hoc polymorphism_).
when a method is being called on a type, python just 'tries' to call that method at __run-time__ and simply raises an exception if the method doesnt exist, has a different number of parameters, or if anything else failed

or more concisely, _duck-typing polymorphism_ can be summarised as:
>   if it walks like a duck <br>
>   and quacks like a duck <br>
>   it is a duck

In our example, we considered objects that had a `walk()` method and `quack()` method to be _enough like ducks_ to be fed duck food. 


to be more formal, we've defined a __duck protocol__ and any other object that follows this protocol can also be fed by the `treat_the_ducks()` function

## Protocols

A protocol is a contract about what a type must provide or implement in order to be able to be used in a certain way.
In our case the duck protocol is that a contract that if an object has a `quack()` and `walk()` method then it can be treated as a duck and be fed duck food

In many cases, protocols can be used informally, as a sort of a _'gentelman's agreement'_ and python will not try to make explicit checks for correctly following a protocol

Lets create a new Mallard class (mallards are a type of duck) that also informally conforms to this protocol



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
class Mallard: 
    """
    a mallard is a bird that is very similar to a duck
    
    it follows the duck protocol by implementing a walk() and quack() function
    """
    def walk(self):
        print('mallard walking here')
        
    def quack(self):
        print('mallard quacks')

# function treat_the_ducks() doesn't know anything about Mallards
# but since it follows the the duck protocol, it can be fed using the same function
treat_the_ducks( [ Mallard() ] )

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```

Mallard :
mallard walking here
mallard quacks
giving duck food to Mallard
```
</div>
</div>
</div>



## Abstract base classes (ABCs)

Is there a way for us to express this _duck protocol_ in a way that would make it easy for us to implement new classes of Ducks and make sure that all of the conform to the protocol? 

lets introduce ABCs by defining a new abstract base class called `AbstractDuck` that captures all there is to know about what being a duck is like 



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
from abc import ABC, abstractmethod

class AbstractDuck(ABC):
    @abstractmethod
    def walk(self):
        print(animal_type_name(self), 'walking here')
        
    @abstractmethod
    def quack(self):
        print(animal_type_name(self), 'quacks')
        


```
</div>

</div>



### What's going on here?
1. Declared a new class called `AbstractDuck`
1. Declared that it is a type of ABC by inheriting from the ABC class
1. Defined two methods `walk()` and `quack()` and marked them as abstract using an `@abstractmethod` decorator 

### What's _abstract_ about abcs?
Abstract classes cannot be instantiated into objects (they only capture an idea) 

```
my_new_duck = AbstractDuck()

---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-52-dd1dce9299b8> in <module>
----> 1 AbstractDuck()

TypeError: Can't instantiate abstract class AbstractDuck with abstract methods quack, walk
```

### Using your ABCs



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
class AmericanWigeon(AbstractDuck):
    """
    a wigeon is another type of duck-like bird. cute!
    """
    
    def walk(self):
        AbstractDuck.walk(self)
        
    def quack(self):
        AbstractDuck.quack(self)
        
new_duck = AmericanWigeon()
treat_the_ducks( [ new_duck ] )

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```

AmericanWigeon :
AmericanWigeon walking here
AmericanWigeon quacks
giving duck food to AmericanWigeon
```
</div>
</div>
</div>



### What happens if we don't override all the methods?
If a type does not override all the abstract methods of an ABC, it will continue to be abstract and cannot be instantiated

```
class Cormorant(AbstractDuck):
    def walk(self):
        print('cormorant walking')
        
    # notice we haven't overriden the quack() method
    
bird = Cormorant()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-10-b2c9c88c912b> in <module>
      5     # notice we haven't overriden the quack() method
      6 
----> 7 bird = Cormorant()

TypeError: Can't instantiate abstract class Cormorant with abstract methods quack
```




### Using ABCs to check for protocol

what if similarly to `treat_the_ducks()`, we need to a write a function that should only work on 
types that follow the duck protocol?

How about using the `isinstance()` function? certainly that would work for objects of type `AmericanWigeon` it inherites from `AbstractDuck`.

what about the other duck-like types such as `Duck`, `Mallard`, and `Goose` that we implemented before we wrote AbstractDuck?





<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def is_it_a_duck(animal):
    """
    use isinstance() function against AbstractDuck to determine if the given animal is a duck"
    """
    
    is_duck = isinstance(animal, AbstractDuck)
    
    if is_duck:  print(animal_type_name(animal), 'IS a duck')
    else:        print(animal_type_name(animal), 'is NOT a duck')


# works as expected
is_it_a_duck(AmericanWigeon())

print()

# unfortunately this method doesn't (YET!) seem to recognize our other duck classes that 
# didnt inherit from AbstractDuck
is_it_a_duck(Duck())
is_it_a_duck(Mallard())
is_it_a_duck(Goose())



```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
AmericanWigeon IS a duck

Duck is NOT a duck
Mallard is NOT a duck
Goose is NOT a duck
```
</div>
</div>
</div>



Do we need to change the code for `Duck`, `Mallard`, and `Goose` to be able to detect that these are also ducks? <br>

fortunately, the answer is NO

### Registering types
We can register  `Duck`, `Mallard`, and `Goose` as also being a sort-of subclass of AbstractDuck using the `AbstractDuck.register()` function

after calling this function on our other duck types, calls to `isinstance(animal, AbstractDuck)` will return True. <br>
This is called _virtual subclassing_ <br>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
AbstractDuck.register(Duck)
AbstractDuck.register(Mallard)
AbstractDuck.register(Goose)

# now isinstance() can be used to check if an object is a duck
is_it_a_duck(Duck())
is_it_a_duck(Mallard())
is_it_a_duck(Goose())
print()

# and obviously, it has no effect on other types we have not registered
is_it_a_duck(Lion())


```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
Duck IS a duck
Mallard IS a duck
Goose IS a duck

Lion is NOT a duck
```
</div>
</div>
</div>



# Summary
What have we learned?
1. Learned what polymorphism is, and seen some simple polymorphism examples in python 
1. We've learned that polymorphism in python is achieved through a simple mechanism known as _duck-typing_
1. We've learned that protocols are informal contracts about how objects can be used - often that means which functions these objects must have
1. We've learned what Abstract Base Classes (ABCs) are
  1. motivation to use ABCs to make sure classes conform to a protocol
  1. how to create new ABCs to capture a protocol
  1. checking if a class conforms to a protocol by using isinstance with an ABC
  1. registering classes that did not inherit from an ABC - virtual subclassing

