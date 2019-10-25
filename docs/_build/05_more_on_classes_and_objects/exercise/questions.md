---
redirect_from:
  - "/05-more-on-classes-and-objects/exercise/questions"
interact_link: content/05_more_on_classes_and_objects/exercise/questions.ipynb
kernel_name: python3
has_widgets: false
title: 'Questions'
prev_page:
  url: /05_more_on_classes_and_objects/exercise/questions.html
  title: 'exercise'
next_page:
  url: /05_more_on_classes_and_objects/exercise/solutions.html
  title: 'Solutions'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-advanced-python/blob/master/content/05_more_on_classes_and_objects/exercise/questions.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




# `__setattr__`

here's a trivial person class
```
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

notice that you can add any attribute to an instance of person
```
terry = Person('Terry Gilliam', 78)
terry.new_attribute = 'lets make sure this fails'
print(terry.new_attribute) # 'lets make sure this fails'
```

can you modify `class Person` so that it disallows adding any new attributes beyond `.name` and `.age`?
> hint: add a `__setattr__(self, name, value)` function to Person

the following code should succeed:

```
terry = Person('Terry Gilliam', 78)        
terry.age = terry.age + 1
print(terry.age) # 79

ok = False
try:
    terry.new_attribute = 'lets make sure this fails'
except:
    ok = True
    print('good')

assert ok
```



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
### useful test - the following code should succeed
terry = Person('Terry Gilliam', 78)        
terry.age = terry.age + 1
print(terry.age) # 79

ok = False
try:
    terry.new_attribute = 'lets make sure this fails'
except:
    ok = True
    print('good')

assert ok

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
79
good
```
</div>
</div>
</div>

