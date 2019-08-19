---
redirect_from:
  - "/06-multiple-inheritance-and-super/exercise/solutions"
interact_link: content/06_multiple_inheritance_and_super/exercise/solutions.ipynb
kernel_name: python3
has_widgets: false
title: 'Solutions'
prev_page:
  url: /06_multiple_inheritance_and_super/exercise/questions.html
  title: 'Questions'
next_page:
  url: /07_design_patterns_in_python/07-design_patterns_in_python.html
  title: '07 design patterns in python'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-advanced-python/blob/master/content/06_multiple_inheritance_and_super/exercise/solutions.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




# Multiple inheritance

given the following classes `Address` and `Person`:
```
class Address:
    def __init__(self, street, city):
        self.street = str(street)
        self.city = str(city)
        
    def show(self):
        print(self.street)
        print(self.city)

class Person:
    def __init__(self, name, email):
        self.name = name
        self.email= email
        
    def show(self):
        print(self.name + ' ' + self.email)
```

## Task:

1. Modify classes `Person` and `Address` 
so that they can work well in a multiple-inheritance hierarchy <br><br>
> you may want to add `from superobject import SuperObject` to be able to use the `SuperObject` class from lesson 06

2. implement the following classes:

  1. `class Contact` that inherits from both `Address` and `Person`
     > this class should have a `def show(self)` method
   
  2. `class Notebook` that is a dictionary that maps people's names to a `Contact` object. 
     it doesnt need to inherit anything
     > 1. this class should have a `def show(se)` method
     > 2. this class should have a `def add(self, name, email, street, city)` method

3. Test your code with the sample code below:

    ```
    notes = Notebook()
    notes.add('Alice', '<alice@example.com>', 'Lv 24', 'Sthlm')
    notes.add('Bob', '<bob@example.com>', 'Rtb 35', 'Sthlm')

    notes.show()
    ```

    expected output:
    
    ```
    Alice
    <alice@example.com>
    Lv 24 Sthlm

    Bob
    <bob@example.com>
    Rtb 35 Sthlm
    ```




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
from superobject import SuperObject

class Address(SuperObject):
    def __init__(self, street, city, **kwargs):
        super().__init__(street=street, city=city, **kwargs)
        self.street = str(street)
        self.city = str(city)
        
    def show(self):
        self.super_call(super(), 'show')           
        print(self.street)
        print(self.city)

class Person(SuperObject):
    def __init__(self, name, email, **kwargs):
        super().__init__(name=name, email=email, **kwargs)
        self.name = name
        self.email= email
        
    def show(self):
        self.super_call(super(), 'show')
        print(self.name + ' ' + self.email)
        
class Contact(Person, Address):
    def __init__(self, street, city, name, email, **kwargs):
        super().__init__(street=street, city=city, name=name, email=email, **kwargs)
    
    def show(self):
        super().show()
        
class Notebook:
    def __init__(self):
        self.__contacts = dict()

    def add(self, street, city, name, email):
        self.__contacts[name] = Contact(street=street, city=city, name=name, email=email)

    def show(self):
        for name, contact in self.__contacts.items():
            contact.show()
            print()


                            
        

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
Alice
<alice@example.com>
Lv 24 Sthlm

Bob
<bob@example.com>
Rtb 35 Sthlm

```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
### useful test for your code
notes = Notebook()
notes.add('Alice', '<alice@example.com>', 'Lv 24', 'Sthlm')
notes.add('Bob', '<bob@example.com>', 'Rtb 35', 'Sthlm')

notes.show()

```
</div>

</div>

