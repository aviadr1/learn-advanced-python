---
redirect_from:
  - "/02-closures-and-decorators/exercise/questions"
interact_link: content/02_closures_and_decorators/exercise/questions.ipynb
kernel_name: python3
has_widgets: false
title: 'Questions'
prev_page:
  url: /02_closures_and_decorators/exercise/questions.html
  title: 'exercise'
next_page:
  url: /02_closures_and_decorators/exercise/solutions.html
  title: 'Solutions'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-advanced-python/blob/master/content/02_closures_and_decorators/exercise/questions.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




# bind1st - create a one parameter function from a two parameter function

Imagine we have some function that takes two parameters, like `divide(x,y)` 
```python
def divide(x,y):
    return x/y
```

Write a function called `bind1st(func, value)` that can create a one parameter function from this two parameter function?
it should work like this

```python
# take the divide function, and the value 100
# and create a new function called divide_100_by(y)
divide_100_by = bind1st(divide, 100) 
print(divide_100_by(2)) # prints 50
print(divide_100_by(10)) # prints 10
```



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
### useful: this tests your function bind1st
def divide(a,b):
    return a/b

def multiply(x,y):
    return x*y


divide_100_by = bind1st(divide, 100) 
assert divide_100_by(2) == 50

multiply_by_2 = bind1st(multiply, 2) 
assert multiply_by_2(50) == 100

```
</div>

</div>



# bind - a general way to bind function parameters

This question continues from the previous one, but this time, we want to bind more than one parameter.
Write a function called `bind(func, *args, **kwargs)` that:
- receives any function `func` that has any number of parameters
- `*args` - a variable number of positional arguments
- `**kwargs` - a variable number of keyword arguments
and returns a new function with where `*args` and `**kwargs` have been bound.

for instance:
```python
def connect_to_database(usr, pwd, srv, port, protocol):
    print("connecting to db:")
    print(f"user={usr}, password={pwd}, server={srv}, port={port}, protocol={protocol}")

http_connect = bind(connect_to_database, protocol="http")
```




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
### useful: use this to test your `bind` function
def connect_to_database(usr, pwd, srv, port, protocol):
    print("connecting to db:")
    print(f"user={usr}, password={pwd}, server={srv}, port={port}, protocol={protocol}")
 
http_connect = bind(connect_to_database, protocol="http")
# prints: user=jamesbond, password=007, server=mi, port=6, protocol=http
http_connect("jamesbond", "007", "mi", 6) 

jamesbond_connect_http = bind(http_connect, "jamesbond", "007") 
# prints: user=jamesbond, password=007, server=mi, port=6, protocol=http
jamesbond_connect_http("mi", 6)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
connecting to db:
user=jamesbond, password=007, server=mi, port=6, protocol=http
connecting to db:
user=jamesbond, password=007, server=mi, port=6, protocol=http
```
</div>
</div>
</div>



# Observable decorator

Consider the `Observable` class based on the "observable" pattern
```
class Observable:
    def __init__(self):
        self.handlers = []
    
    def register(self, callable_):
        self.handlers.append(callable_)
        
    def notify(self, obj, event, *args, **kwargs):
        for handler in self.handlers:
            handler(obj, event, *args, **kwargs)
            
def start_observing(obj):
    obj.observable_events = Observable()

def observable(obj):
    return obj.observable_events
```

Create two decorator functions 
```
observable_class(klass)- decorates a class to become observable`
observe(func) - decorates a method to become observable
```

such that given a simple class like the following:
```
class Test:
    def test(self, message):
        print('test', message)
```

you could decorate Test using the decorators:
```
@observable_class
class Test:
    @observe
    def test(self, message):
        print('test', message)
```

and then be able to get notifications whenever the `Test.test()` function is used:

```
def simple_handler(obj, event, *args, **kwargs):
    print('notified:', obj, event, *args, **kwargs)
    
t = Test()
t.observable().register(simple_handler)
t.test('hello')
```

expected output:
```
notified: <__main__.Test object at 0x000002E99F51A7F0> test hello
test hello
```



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
### useful starting point
class Observable:
    def __init__(self):
        self.handlers = []
    
    def register(self, callable_):
        self.handlers.append(callable_)
        
    def notify(self, obj, event, *args, **kwargs):
        for handler in self.handlers:
            handler(obj, event, *args, **kwargs)
            
def start_observing(obj):
    obj.observable_events = Observable()

def observable(obj):
    return obj.observable_events
    

```
</div>

</div>

