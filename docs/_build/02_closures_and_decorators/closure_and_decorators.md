---
redirect_from:
  - "/02-closures-and-decorators/closure-and-decorators"
interact_link: content/02_closures_and_decorators/closure_and_decorators.ipynb
kernel_name: python3
has_widgets: false
title: 'Closure And Decorators'
prev_page:
  url: /02_closures_and_decorators/closure_and_decorators.html
  title: '02 closures and decorators'
next_page:
  url: /02_closures_and_decorators/variadic_functions.html
  title: 'Variadic Functions'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-advanced-python/blob/master/content/02_closures_and_decorators/closure_and_decorators.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




# Closures and decorators

In this lesson, we will learn what closures are, 
and see two uses of closures:
1. replacing trivial do_something classes with closures
2. decorators

decorators will take the bulk of time in this lesson

## Closures
Consider the example below, where a function defines an inner function and returns it:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# make_printer() is a function that creates functions!
def make_printer(message):
    
    def nested_printer_func(): # this creates a new function object
        # use the message parameter to the make_printer() printer
        print(message)
    
    # return the nested function object
    return nested_printer_func

# lets create a function that prints 'hello' when called
print_hello = make_printer('hello')
print_hello()

# lets create a function that prints 'world' when called
print_world = make_printer('world')
print_world()

# notice that these are not the same object, they are not the same function
print('are these the same function?', print_world == print_hello)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
hello
world
are these the same function? False
```
</div>
</div>
</div>



### What's happening here?
The `make_printer()` function was called with the string "hello" and the returned function was bound to the name print_hello. On calling print_hello(), the message was still remembered although we had already finished executing the `make_printer()` function.

This technique by which some data ("hello") gets attached to the code is called closure in Python.

### When do we have a closure?
As seen from the above example, we have a closure in Python when a nested function references a value in its enclosing scope.

The criteria that must be met to create closure in Python are summarized in the following points.

* We must have a nested function (function inside a function).
* The nested function must refer to a value defined in the enclosing function.
* The enclosing function must return the nested function.

### When are closures useful?

There's two main cases:
1. trivial *do_something* classes <br>
   If you see an object-oriented solution that creates a class with just one method, or one method and a constructor, it can easily be replaced with functions or functions created as coloures. often with these classes, the function will be called something opaque like update(), do_it(), action() etc

2. *decorators* <br>
   if we want to take an exising function and add functionality to that function without changing the original function's code by 'wrapping' or 'decorating' that function, closures are a good solution 
   
we will take a long look at decorators at the end of this lesson, so for now, lets focus on do_something classes



### replacing do_something classes with closures



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
"""
Here is a classic example of a do_something class interface.
class Event registers event handlers objects that must have an event_handler function
"""
class PrintEventHandler:
    def __init__(self, message):
        self.__message = message
        
    def handle_event(self, event, *args):
        print(self.__message, *args)

class Event :
    """
    Event class allows registering event handler objects, which must have a handle_event() function
    """
    def __init__(self):
        self.__handlers = []
        
    def notify(self, *args):
        for handler in self.__handlers:
            # notice 
            handler.handle_event(self, *args)
            
    def add_event_handler(self, handler_object):
        self.__handlers.append(handler_object)
        
e = Event()
e.add_event_handler(PrintEventHandler('well I didnt expect'))
e.add_event_handler(PrintEventHandler('nobody expects'))
e.notify('the spanish inquisition')

        

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
well I didnt expect the spanish inquisition
nobody expects the spanish inquisition
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
"""
Simplified version of above example, where the class PrintEventHandler is not needed
"""
def make_print_handler(message):
    def handler(event, *args): 
        print(message, *args)
        
    return handler

class SimplerEvent :
    """
    Event class allows registering event handling *functions*
    """
    def __init__(self):
        self.__handlers = []
        
    def notify(self, *args):
        for handler in self.__handlers: 
            handler(self, *args) # handler now is simply a callable function
            
    def add_event_handler(self, handler):
        self.__handlers.append(handler)
        
e = SimplerEvent()
e.add_event_handler(make_print_handler('well I didnt expect'))
e.add_event_handler(make_print_handler('nobody expects'))
e.notify('the spanish inquisition')


```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
well I didnt expect the spanish inquisition
nobody expects the spanish inquisition
```
</div>
</div>
</div>



## Decorators
Decorators are a simple pattern to add functionality to an existing function, without changing the code for that function.

here is an extremely simplified example:

[1]: https://realpython.com/primer-on-python-decorators/#simple-decorators



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_whee():
    print("Whee!")

# decorate the say_whee function 
say_whee = my_decorator(say_whee)

# use it
say_whee()

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
Something is happening before the function is called.
Whee!
Something is happening after the function is called.
```
</div>
</div>
</div>



To understand what’s going on here, look back at the previous examples. 
We are literally just applying everything you have learned so far.

The so-called decoration happens at the following line:

`say_whee = my_decorator(say_whee)`
In effect, the name say_whee now points to the `wrapper()` inner function. 
Remember that you return wrapper as a function when you call `my_decorator(say_whee)`:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print(say_whee)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_traceback_line}
```

    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-1-2051ccf0e421> in <module>()
    ----> 1 print(say_whee)
    

    NameError: name 'say_whee' is not defined


```
</div>
</div>
</div>



However, `wrapper()` has a reference to the original `say_whee()` as func, and calls that function between the two calls to `print()`.

Put simply: decorators wrap a function, modifying its behavior.



Before moving on, let’s have a look at a second example. 
Because wrapper() is a regular Python function, 
the way a decorator modifies a function can change dynamically. 
So as not to disturb your neighbors, the following example will only run the decorated code during the day:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
from datetime import datetime
override_hour =  None

def not_during_the_night(func):
    def wrapper():
        hour = override_hour or datetime.now().hour
        if 7 <= hour < 22:
            func()
        else:
            pass  # Hush, the neighbors are asleep
    return wrapper

def say_whee():
    print("Whee!")

say_whee = not_during_the_night(say_whee)

# If you try to call say_whee() after bedtime, nothing will happen:
override_hour = 23
say_whee()


```
</div>

</div>



### Syntactic Sugar!
The way we decorated `say_whee()` above is a little clunky. 
First of all, we end up typing the name say_whee three times. 

In addition, the decoration gets a bit hidden away below the definition of the function.

Instead, Python allows us to use decorators in a simpler way with the `@` symbol, sometimes called the “pie” syntax. 

The following example does the exact same thing as the first decorator example:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_whee():
    print("Whee!")
    
# So, @my_decorator is just an easier way of saying 
# say_whee = my_decorator(say_whee). 
# It’s how you apply a decorator to a function.

```
</div>

</div>



### Reusing Decorators
Recall that a decorator is just a regular Python function. 
All the usual tools for easy reusability are available: such as placing the decorator in a module and importing it.

obviously, There's a bunch of decorators in the standard library, which we will go through.

lets start with defining a more useful decorator:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# imagine you place this in a file called my_decorators.py

def do_twice(func):
    def wrapper_do_twice():
        func()
        func()
    return wrapper_do_twice

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# We can now use this new decorator wherever we want in our code by importing it
# from decorators import do_twice

@do_twice
def say_whee():
    print("Whee!")
    
say_whee()

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
Whee!
Whee!
```
</div>
</div>
</div>



### Decorating Functions With Arguments
Say that you have a function that accepts some arguments. Can you still decorate it? Let’s try:

```
@do_twice
def greet(name):
    print(f"Hello {name}")

greet('bob')
```
```
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-10-250b00126245> in <module>
      5     print(f"Hello {name}")
      6 
----> 7 greet('bob')
      8 
      9 # The problem is that the inner function wrapper_do_twice() does not take any arguments,

TypeError: wrapper_do_twice() takes 0 positional arguments but 1 was given
```

The problem is that the inner function wrapper_do_twice() does not take any arguments, 
but name="World" was passed to it. 

You could fix this by letting wrapper_do_twice() accept one argument, 
but then it would not work for the say_whee() function you created earlier.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# The solution is to use *args and **kwargs in the inner wrapper function. 
# Then it will accept an arbitrary number of positional and keyword arguments. 

def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice



```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# The wrapper_do_twice() inner function now accepts any number of arguments 
# and passes them on to the function it decorates. 

# Now both your say_whee() and greet() examples works:
    
@do_twice
def greet(name):
    print(f"Hello {name}")
    
@do_twice
def say_whee():
    print("Whee!")

greet('bob')
say_whee()

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
Hello bob
Hello bob
Whee!
Whee!
```
</div>
</div>
</div>



### Returning Values From Decorated Functions
What happens to the return value of decorated functions? Well, that’s up to the decorator to decide. 
Let’s say you decorate a simple function as follows:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
@do_twice
def return_greeting(name):
    print("Creating greeting")
    return f"Hi {name}"

hi_bob = return_greeting("bob")
# Creating greeting
# Creating greeting

print(hi_bob)
# None


# Oops, our decorator ate the return value from the function.

# Because the do_twice_wrapper() doesn’t explicitly return a value, 
# the call return_greeting("bob") ended up returning None.

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
Creating greeting
Creating greeting
None
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# To fix this, we need to make sure the wrapper function returns the return value of the decorated function. 

def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice

@do_twice
def return_greeting(name):
    print("Creating greeting")
    return f"Hi {name}"

# The return value from the last execution of the function is returned:
return_greeting("Adam")
# Creating greeting
# Creating greeting
# 'Hi Adam'

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
Creating greeting
Creating greeting
```
</div>
</div>
<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'Hi Adam'
```


</div>
</div>
</div>



### Who Are You, Really?
A great convenience when working with Python, especially in the interactive shell, is its powerful introspection ability. Introspection is the ability of an object to know about its own attributes at runtime. For instance, a function knows its own name and documentation:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# a function knows its own name and documentation:
import math
print(math.sin) 
# <built-in function len>

print(math.sin.__name__)
# 'sin'

help(math.sin)
# Help on built-in function sin in module math:
# sin(x, /)
#     Return the sine of x (measured in radians).

#
# The introspection works for functions you define yourself as well:
#

print(say_whee)
# <function do_twice.<locals>.wrapper_do_twice at 0x7f43700e52f0>

print(say_whee.__name__)
# 'wrapper_do_twice'

help(say_whee)
# Help on function wrapper_do_twice in module decorators:
#  wrapper_do_twice()


#
# However, after being decorated, say_whee() has gotten very confused about its identity. 
# It now reports being the wrapper_do_twice() inner function inside the do_twice() decorator. 
# Although technically true, this is not very useful information.
#


```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
<built-in function sin>
sin
Help on built-in function sin in module math:

sin(...)
    sin(x)
    
    Return the sine of x (measured in radians).

<function do_twice.<locals>.wrapper_do_twice at 0x000001A27D0B1620>
wrapper_do_twice
Help on function wrapper_do_twice in module __main__:

wrapper_do_twice(*args, **kwargs)

```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# To fix this, decorators should use the @functools.wraps decorator, 
# which will preserve information about the original function. 

import functools

def do_twice(func):
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice

# We do not need to change anything about the decorated say_whee() function:
@do_twice
def say_whee():
    print("Whee!")

print(say_whee)
# <function say_whee at 0x7ff79a60f2f0>

print(say_whee.__name__)
#'say_whee'

help(say_whee)
# Help on function say_whee in module __main__:

say_whee()

#
# Much better! Now say_whee() is still itself after decoration.
#

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
<function say_whee at 0x000001A27D0C26A8>
say_whee
Help on function say_whee in module __main__:

say_whee()

Whee!
Whee!
```
</div>
</div>
</div>



### A Few Real World Examples
Let’s look at a few more useful examples of decorators. You’ll notice that they’ll mainly follow the same pattern that you’ve learned so far:

```
import functools

def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do something before
        value = func(*args, **kwargs)
        # Do something after
        return value
    return wrapper_decorator
    
```    
This formula is a good boilerplate template for building more complex decorators.



#### Timing Functions
Let’s start by creating a `@timer` decorator. It will measure the time a function takes to execute and print the duration to the console. Here’s the code:




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
import functools
import time

def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer

@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])
        
#
# This decorator works by storing the time just before the function starts running (at the line marked # 1) 
# and just after the function finishes (at # 2). 
# The time the function takes is then the difference between the two (at # 3). 
# We use the time.perf_counter() function, which does a good job of measuring time intervals. 
# 

# Here are some examples of timings:
waste_some_time(1)
waste_some_time(999)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
Finished 'waste_some_time' in 0.0033 secs
Finished 'waste_some_time' in 3.3701 secs
```
</div>
</div>
</div>



Run it yourself. Work through the code line by line. Make sure you understand how it works. Don’t worry if you don’t get it, though. Decorators are advanced beings. Try to sleep on it or make a drawing of the program flow.

> Note: The @timer decorator is great if you just want to get an idea about the runtime of your functions. If you want to do more precise measurements of code, you should instead consider the timeit module in the standard library. It temporarily disables garbage collection and runs multiple trials to strip out noise from quick function calls.



#### Debugging Code
The following @debug decorator will print the arguments a function is called with as well as its return value every time the function is called:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
import functools

def debug(func):
    """Print the function signature and return value"""
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]                      # 1
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # 2
        signature = ", ".join(args_repr + kwargs_repr)           # 3
        print(f"Calling {func.__name__}({signature})")
        
        value = func(*args, **kwargs)
        
        print(f"{func.__name__!r} returned {value!r}")           # 4
        return value
    return wrapper_debug

```
</div>

</div>



The signature is created by joining the string representations of all the arguments. The numbers in the following list correspond to the numbered comments in the code:

1. Create a list of the positional arguments. Use repr() to get a nice string representing each argument.
1. Create a list of the keyword arguments. The f-string formats each argument as key=value where the !r specifier means that repr() is used to represent the value.
1. The lists of positional and keyword arguments is joined together to one signature string with each argument separated by a comma.
1. The return value is printed after the function is executed.
Let’s see how the decorator works in practice by applying it to a simple function with one position and one keyword argument:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
@debug
def make_greeting(name, age=None):
    if age is None:
        return f"Howdy {name}!"
    else:
        return f"Whoa {name}! {age} already, you are growing up!"
    
make_greeting("Benjamin")
# Calling make_greeting('Benjamin')
# 'make_greeting' returned 'Howdy Benjamin!'
# 'Howdy Benjamin!'

make_greeting("Richard", age=112)
# Calling make_greeting('Richard', age=112)
# 'make_greeting' returned 'Whoa Richard! 112 already, you are growing up!'
# 'Whoa Richard! 112 already, you are growing up!'

make_greeting(name="Dorrisile", age=116)
# Calling make_greeting(name='Dorrisile', age=116)
# 'make_greeting' returned 'Whoa Dorrisile! 116 already, you are growing up!'
# 'Whoa Dorrisile! 116 already, you are growing up!'

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
Calling make_greeting('Benjamin')
'make_greeting' returned 'Howdy Benjamin!'
Calling make_greeting('Richard', age=112)
'make_greeting' returned 'Whoa Richard! 112 already, you are growing up!'
Calling make_greeting(name='Dorrisile', age=116)
'make_greeting' returned 'Whoa Dorrisile! 116 already, you are growing up!'
```
</div>
</div>
<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'Whoa Dorrisile! 116 already, you are growing up!'
```


</div>
</div>
</div>



The above example might not seem immediately useful since the @debug decorator just repeats what you just wrote. It’s more powerful when applied to small convenience functions that you don’t call directly yourself.


The following example calculates an approximation to the mathematical constant e:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
import math

# Apply a decorator to a standard library function
math.factorial = debug(math.factorial)

def approximate_e(terms=18):
    return sum(1 / math.factorial(n) for n in range(terms))

```
</div>

</div>



This example also shows how you can apply a decorator to a function that has already been defined. The approximation of e is based on the following series expansion: <br>
$$ {\rm e} = \sum_{n=0}^{\infty} \frac{1}{n!} = \frac{1}{0!} + \frac{1}{1!} + \frac{1}{2!} + \frac{1}{3!} + \ldots $$ <br>
Series for calculating mathematical constant e

When calling the approximate_e() function, you can see the @debug decorator at work:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
approximate_e(5)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
Calling factorial(0)
'factorial' returned 1
Calling factorial(1)
'factorial' returned 1
Calling factorial(2)
'factorial' returned 2
Calling factorial(3)
'factorial' returned 6
Calling factorial(4)
'factorial' returned 24
```
</div>
</div>
<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
2.708333333333333
```


</div>
</div>
</div>



#### Registering Plugins
Decorators don’t have to wrap the function they’re decorating. They can also simply register that a function exists and return it unwrapped. This can be used, for instance, to create a light-weight plug-in architecture:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
import random
PLUGINS = dict()

def register(func):
    """Register a function as a plug-in"""
    PLUGINS[func.__name__] = func
    return func

@register
def say_hello(name):
    return f"Hello {name}"

@register
def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"

def randomly_greet(name):
    greeter, greeter_func = random.choice(list(PLUGINS.items()))
    print(f"Using {greeter!r}")
    return greeter_func(name)

# The @register decorator simply stores a reference to the decorated function in the global PLUGINS dict. 
# Note that you do not have to write an inner function or use @functools.wraps in this example 
# because you are returning the original function unmodified.

# The randomly_greet() function randomly chooses one of the registered functions to use. 
# Note that the PLUGINS dictionary already contains references to each function object that is registered as a plugin:

print(PLUGINS)
# {'say_hello': <function say_hello at 0x7f768eae6730>,
#  'be_awesome': <function be_awesome at 0x7f768eae67b8>}

randomly_greet("Alice")


```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
{'say_hello': <function say_hello at 0x000001A27D0D89D8>, 'be_awesome': <function be_awesome at 0x000001A27D0D8B70>}
Using 'be_awesome'
```
</div>
</div>
<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'Yo Alice, together we are the awesomest!'
```


</div>
</div>
</div>



The main benefit of this simple plugin architecture is that you do not need to maintain a list of which plugins exist. That list is created when the plugins register themselves. This makes it trivial to add a new plugin: just define the function and decorate it with @register.

If you are familiar with globals() in Python, you might see some similarities to how the plugin architecture works. globals() gives access to all global variables in the current scope, including your plugins:

```
>>> globals()
{..., # Lots of variables not shown here.
 'say_hello': <function say_hello at 0x7f768eae6730>,
 'be_awesome': <function be_awesome at 0x7f768eae67b8>,
 'randomly_greet': <function randomly_greet at 0x7f768eae6840>}
```

Using the @register decorator, you can create your own curated list of interesting variables, effectively hand-picking some functions from globals().



## Fancy decorators
So far, you’ve seen how to create simple decorators. You already have a pretty good understanding of what decorators are and how they work. 

### Decorating Classes
There are two different ways you can use decorators on classes. The first one is very close to what you have already done with functions: you can decorate the methods of a class. This was one of the motivations for introducing decorators back in the day.

#### Commonly used decorators: `@classmethod`, `@staticmethod`, and `@property`
Some commonly used decorators that are even built-ins in Python are `@classmethod`, `@staticmethod`, and `@property`. The @classmethod and @staticmethod decorators are used to define methods inside a class namespace that are not connected to a particular instance of that class. The @property decorator is used to customize getters and setters for class attributes. Expand the box below for an example using these decorators.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        """Get value of radius"""
        return self._radius

    @radius.setter
    def radius(self, value):
        """Set radius, raise error if negative"""
        if value >= 0:
            self._radius = value
        else:
            raise ValueError("Radius must be positive")

    @property
    def area(self):
        """Calculate area inside circle"""
        return self.pi() * self.radius**2

    def cylinder_volume(self, height):
        """Calculate volume of cylinder with circle as base"""
        return self.area * height

    @classmethod
    def unit_circle(cls):
        """Factory method creating a circle with radius 1"""
        return cls(1)

    @staticmethod
    def pi():
        """Value of π, could use math.pi instead though"""
        return 3.1415926535

```
</div>

</div>



* .cylinder_volume() is a regular method.
* .radius is a mutable property: it can be set to a different value. However, by defining a setter method, we can do some error testing to make sure it’s not set to a nonsensical negative number. Properties are accessed as attributes without parentheses.
* .area is an immutable property: properties without .setter() methods can’t be changed. Even though it is defined as a method, it can be retrieved as an attribute without parentheses.
* .unit_circle() is a class method. It’s not bound to one particular instance of Circle. Class methods are often used as factory methods that can create specific instances of the class.
* .pi() is a static method. It’s not really dependent on the Circle class, except that it is part of its namespace. Static methods can be called on either an instance or the class.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
c = Circle(5)
print(c.radius)
# 5

print(c.area)
# 78.5398163375

c.radius = 2
print(c.area)
12.566370614

# c.area = 100 # AttributeError: can't set attribute

c.cylinder_volume(height=4) 
# 50.265482456

# c.radius = -1 # ValueError: Radius must be positive

c = Circle.unit_circle()
print(c.radius)
1

print(c.pi())
# 3.1415926535

print(Circle.pi())
3.1415926535

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
5
78.5398163375
12.566370614
1
3.1415926535
3.1415926535
```
</div>
</div>
<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
3.1415926535
```


</div>
</div>
</div>



#### Decorating functions in a class

Let’s define a class where we decorate some of its methods using the @debug and @timer decorators from earlier:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
class TimeWaster:
    @debug
    def __init__(self, max_num):
        self.max_num = max_num

    @timer
    def waste_time(self, num_times):
        for _ in range(num_times):
            sum([i**2 for i in range(self.max_num)])
            
# Using this class, you can see the effect of the decorators:

tw = TimeWaster(1000)
# Calling __init__(<time_waster.TimeWaster object at 0x7efccce03908>, 1000)
# '__init__' returned None

tw.waste_time(999)
# Finished 'waste_time' in 0.3376 secs

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
Calling __init__(<__main__.TimeWaster object at 0x000001A27D0E0C88>, 1000)
'__init__' returned None
Finished 'waste_time' in 0.3012 secs
```
</div>
</div>
</div>



### Whole class decorators
The other way to use decorators on classes is to decorate the whole class. This is, for example, done in the new dataclasses module in Python 3.7:





<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
import sys
if sys.version_info < (3, 7):
    print('dataclasses only work with python 3.7 and above')
else:    
    
    from dataclasses import dataclass

    @dataclass
    class PlayingCard:
        rank: str
        suit: str

    PlayingCard('queen', 'hearts')

    # The meaning of the syntax is similar to the function decorators. 
    # In the example above, you could have done the decoration by writing PlayingCard = dataclass(PlayingCard).

    # A common use of class decorators is to be a simpler alternative to some use-cases of metaclasses. 
    # In both cases, you are changing the definition of a class dynamically.

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
dataclasses only work with python 3.7 and above
```
</div>
</div>
</div>



#### Whole class decorators - Constructor decorator
Writing a class decorator is very similar to writing a function decorator. The only difference is that the decorator will receive a class and not a function as an argument. In fact, all the decorators you saw above will work as class decorators. When you are using them on a class instead of a function, their effect might not be what you want. In the following example, the @timer decorator is applied to a class:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
@timer # decorates TimeWaster.__init__
class TimeWaster:
    def __init__(self, max_num):
        self.max_num = max_num

    def waste_time(self, num_times):
        for _ in range(num_times):
            sum([i**2 for i in range(self.max_num)])
            
# Decorating a class does not decorate its methods. 
# Recall that @timer is just shorthand for TimeWaster = timer(TimeWaster).
# Here, @timer only measures the time it takes to instantiate the class:

tw = TimeWaster(1000)
# Finished 'TimeWaster' in 0.0000 secs

tw.waste_time(999) # doesnt use the #timer decorator


```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
Finished 'TimeWaster' in 0.0000 secs
```
</div>
</div>
</div>



### Nesting Decorators
You can apply several decorators to a function by stacking them on top of each other:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
@debug
@do_twice
def greet(name):
    print(f"Hello {name}")
    
#
# Think about this as the decorators being executed in the order they are listed. 
# In other words, @debug calls @do_twice, which calls greet(), or debug(do_twice(greet())):
#

greet("Eva")
# Calling greet('Eva')
# Hello Eva
# Hello Eva
# 'greet' returned None

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
Calling greet('Eva')
Hello Eva
Hello Eva
'greet' returned None
```
</div>
</div>
</div>



### Decorators With Arguments
Sometimes, it’s useful to pass arguments to your decorators. For instance, @do_twice could be extended to a @repeat(num_times) decorator. The number of times to execute the decorated function could then be given as an argument.

This would allow you to do something like this:

```
@repeat(num_times=4)
def greet(name):
    print(f"Hello {name}")

>>> greet("World")
Hello World
Hello World
Hello World
Hello World
```

Think about how you could achieve this. <br>

So far, the name written after the @ has referred to a function object that can be called with another function. To be consistent, you then need repeat(num_times=4) to return a function object that can act as a decorator. Luckily, you already know how to return functions! In general, you want something like the following:

```
def repeat(num_times):
    def decorator_repeat(func):
        ...  # Create and return a wrapper function
    return decorator_repeat
```

Typically, the decorator creates and returns an inner wrapper function, so writing the example out in full will give you an inner function within an inner function. While this might sound like the programming equivalent of the Inception movie, we’ll untangle it all in a moment:




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrapper_repeat
    return decorator_repeat

# It looks a little messy, but we have only put the same decorator pattern you have seen 
# many times by now inside one additional def that handles the arguments to the decorator. 

@repeat(num_times=4)
def greet(name):
    print(f"Hello {name}")

greet("World")

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
Hello World
Hello World
Hello World
Hello World
```
</div>
</div>
</div>

