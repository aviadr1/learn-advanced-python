---
redirect_from:
  - "/08-test-driven-development/exercise/questions"
interact_link: content/08_test_driven_development/exercise/questions.ipynb
kernel_name: python3
has_widgets: false
title: 'exercise'
prev_page:
  url: /08_test_driven_development/08-test_driven_development.html
  title: '08-test Driven Development'
next_page:
  url: /08_test_driven_development/exercise/questions.html
  title: 'Questions'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-advanced-python/blob/master/content/08_test_driven_development/exercise/questions.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




# Unit testing a contact list

The code sample below has `Contact` class that contains both a `Person` and an `Address` class, and finally, a `Notebook` class that contains multiple contacts.

Can you use `pytest` and `unittest.mock` modules to write tests for these classes and fix the bugs in this code



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
### useful: This is the code you should test

class Address:
    def __init__(self, street, city):
        self.street = str(street)
        self.city = str(city)

    def __repr__(self):
        return f"Address({self.city!r}, {self.street!r})"

class Person:
    def __init__(self, name, email):
        self.name = name
        self.email= email

    def __repr__(self):
        return f"Person({self.name!r}, {self.email!r})"
        
class Contact:
    def __init__(self, street, city, name, email, **kwargs):
        self.person = Person(name, email)
        self.address = Address(street, city)
    
    def __str__(self):
        return f"""\
        {self.person.name}:
            {self.person.email}
            address:
                {self.address.city}
                {self.address.street}
        """
        
class Notebook:
    def __init__(self):
        self.contacts = dict()

    def add(self, street, city, name, email):
        self.contacts[name] = Contact(name, email, city, street)

    def remove(name):
        self.contacts.remove(name)
        
    def __str__(self):
        results = []
        for name, contact in self.contacts.items():
            results.append(str(contact))
            results.append("")
        return '\n'.join(results)

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
### useful: run the tests you wrote
import ipytest

# enable pytest's assertions and ipytest's magics
ipytest.config(rewrite_asserts=True, magics=True)

# set the filename
__file__ = 'ex 08 - solutions.ipynb'

# execute the tests via pytest, arguments are passed to pytest
ipytest.run('-qq')

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
....F                                                                                                            [100%]
====================================================== FAILURES =======================================================
__________________________________________________ test_notebook_add __________________________________________________

empty_notebook = <__main__.Notebook object at 0x000001B745CA9080>, name = 'name', email = 'email', city = 'city'
street = 'street'

    def test_notebook_add(empty_notebook, name, email, city, street):
        empty_notebook.add(name=name, email=email, city=city, street=street)
        assert len(empty_notebook.contacts) == 1
>       assert empty_notebook.contacts[name].person.name == name
E       AssertionError: assert 'city' == 'name'
E         - city
E         + name

<ipython-input-43-f0faace97c0e>:47: AssertionError
```
</div>
</div>
</div>

