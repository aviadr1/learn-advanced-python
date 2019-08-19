---
redirect_from:
  - "/08-test-driven-development/08-test-driven-development"
interact_link: content/08_test_driven_development/08-test_driven_development.ipynb
kernel_name: python3
has_widgets: false
title: '08 test driven development'
prev_page:
  url: /07_design_patterns_in_python/07-design_patterns_in_python.html
  title: '07-design Patterns In Python'
next_page:
  url: /08_test_driven_development/08-test_driven_development.html
  title: '08-test Driven Development'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-advanced-python/blob/master/content/08_test_driven_development/08-test_driven_development.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




install ipytest so we can run tests in the jupyter notebook



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
pip -q install ipytest pytest

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
Note: you may need to restart the kernel to use updated packages.
```
</div>
</div>
</div>



initialize pytest



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
import pytest
import ipytest
import unittest.mock as mocking 

# enable pytest's assertions and ipytest's magics
ipytest.config(rewrite_asserts=True, magics=True)

# set the filename
__file__ = 'adv python 08 - test driven development.ipynb'

```
</div>

</div>



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

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# very simple test
def test_person_repr1():
    assert str(Person('terry gilliam')) == f"Person('terry gilliam')"

# test using mock object
def test_train1():
    person = mocking.Mock()
    
    train(person)
    person.walk.assert_called_once()
    person.run.assert_called_once()
    person.swim.assert_called_once()

# create factory for person's name
@pytest.fixture
def person_name():
    return 'terry gilliam'
    
# create factory for Person, that requires a person_name 
@pytest.fixture
def person(person_name):
    return Person(person_name)

# test using mock object
def test_train2(person):
    # this makes sure no other method is called
    person = mocking.create_autospec(person)
    
    train(person)
    person.walk.assert_called_once()
    person.run.assert_called_once()
    person.swim.assert_called_once()


# test Person using and request a person, person_name from the fixtures
def test_person_repr2(person, person_name):
    assert str(person) == f"Person('{person_name}')"
    
# fixture with multiple values
@pytest.fixture(params=['usain bolt', 'Matthew Wells'])
def olympic_runner_name(request):
    return request.param

@pytest.fixture
def olympic_runner(olympic_runner_name):
    return OlympicRunner(olympic_runner_name)

# test train() using mock object for print
@mocking.patch('builtins.print')
def test_train3(mocked_print, olympic_runner):
    train(olympic_runner)
    mocked_print.assert_called()

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# execute the tests via pytest, arguments are passed to pytest
ipytest.run('-qq')

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
......                                                                                                           [100%]
```
</div>
</div>
</div>

