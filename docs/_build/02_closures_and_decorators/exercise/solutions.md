---
redirect_from:
  - "/02-closures-and-decorators/exercise/solutions"
interact_link: content/02_closures_and_decorators/exercise/solutions.ipynb
kernel_name: python3
has_widgets: false
title: 'Solutions'
prev_page:
  url: /02_closures_and_decorators/exercise/questions.html
  title: 'Questions'
next_page:
  url: /03_polymorphism_protocols_and_abcs/polymorphism_protocols_abcs.html
  title: '03 polymorphism protocols and abcs'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-advanced-python/blob/master/content/02_closures_and_decorators/exercise/solutions.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




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



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
import functools
def observable_class(klass):
    init_func = klass.__init__
    
    @functools.wraps(klass.__init__)
    def init_wrapper(self, *args, **kwargs):
        start_observing(self)
        init_func(self, *args, **kwargs)
    
    klass.__init__ = init_wrapper
    klass.observable = observable
    return klass

def observe(f):
    @functools.wraps(f)
    def observed_wrapper(self, *args, **kwargs):
        observable(self).notify(self, f.__name__, *args, **kwargs)
        return f(self, *args, *kwargs)
    return observed_wrapper

@observable_class
class Test:
    @observe
    def test(self, message):
        print('test', message)

def simple_handler(obj, event, *args, **kwargs):
    print('notified:', obj, event, *args, **kwargs)
    
t = Test()
t.observable().register(simple_handler)
t.test('hello')

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
notified: <__main__.Test object at 0x000001957A3ED2E8> test hello
test hello
```
</div>
</div>
</div>

