---
redirect_from:
  - "/13-complex-comprehensions/exercise/solutions"
interact_link: content/13_complex_comprehensions/exercise/solutions.ipynb
kernel_name: python3
has_widgets: false
title: 'Solutions'
prev_page:
  url: /13_complex_comprehensions/exercise/questions.html
  title: 'Questions'
next_page:
  url: /14_pandas/pandas_a_quick_tour.html
  title: '14 pandas'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-advanced-python/blob/master/content/13_complex_comprehensions/exercise/solutions.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




# hotel comprehension
we have information about a hotel.
The hotel has stored its information in a Python list.
The list contains lists (representing rooms), and each sublist contains one or more dictionaries (representing people).

here's the data structure



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
### useful data about hotel
rooms = [[{'age': 14, 'hobby': 'horses', 'name': 'Avram'},  
          {'age': 12, 'hobby': 'piano', 'name': 'Betty'},  
          {'age': 9, 'hobby': 'chess', 'name': 'Chen'},  
          {'age': 15, 'hobby': 'programming', 'name': 'Dov'}],
         [{'age': 17, 'hobby': 'driving', 'name': 'Efrat'}],  
         [{'age': 45, 'hobby': 'writing', 'name': 'Fred'},  
          {'age': 43, 'hobby': 'chess', 'name': 'Greg'},
          {'age': 20, 'hobby': 'surfing', 'name': 'Hofit'}]
          ]

```
</div>

</div>



1. What are the names of the people staying at our hotel?



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
[person['name']      
 for room in rooms
 for person in room ]

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
['Avram', 'Betty', 'Chen', 'Dov', 'Efrat', 'Fred', 'Greg', 'Hofit']
```


</div>
</div>
</div>



2. What are the names of people staying in our hotel who enjoy chess?



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
[person['name']
 for room in rooms
 for person in room
 if person['hobby'] == 'chess' ]

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
['Chen', 'Greg']
```


</div>
</div>
</div>



3. what unique hobbies are enjoyed in rooms with at least 2 people?



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
{person['hobby']
 for room in rooms
 if len(room) >= 2
 for person in room }

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
{'chess', 'horses', 'piano', 'programming', 'surfing', 'writing'}
```


</div>
</div>
</div>



# group by length of word
given a list of words
```
words = ['everything', 'should', 'be', 'as', 'simple', 'as', 'possible',
         'but', 'no', 'simpler', 'albert', 'einstein'
        ]
```

creat a nested list of words, grouped by the length of the words
```
grouped_by_len = [
     [],
     ['be', 'as', 'as', 'no'],
     ['but'],
     [],
     [],
     ['should', 'simple', 'albert'],
     ['simpler'],
     ['possible', 'einstein'],
     [],
     ['everything']
    ]
```



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
words = ['everything', 'should', 'be', 'as', 'simple', 'as', 'possible',
         'but', 'no', 'simpler', 'albert', 'einstein'
        ]

[[word for word in words if len(word) == len_] for len_ in range(1, 1+len(max(words, key=len)))]

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
[[],
 ['be', 'as', 'as', 'no'],
 ['but'],
 [],
 [],
 ['should', 'simple', 'albert'],
 ['simpler'],
 ['possible', 'einstein'],
 [],
 ['everything']]
```


</div>
</div>
</div>



# tranform a nested list
given a nested list of numbers
```
nums = [
 [-3],
 [-2, -1],
 [0, 1, 2],
 [3, 4, 5, 6],
 [7, 8, 9, 10, 11]
 ]
```

transform it into a list of the cumulative sums
```
cumsum = [
 [-3],
 [-2, -3],
 [0, 1, 3],
 [3, 7, 12, 18],
 [7, 15, 24, 34, 45]
 ]
```

hint: you may use this code to calculate a cumulative sum for a list:
```
def cumsum(lst_):
    total = 0
    for val in lst:
        total += val
        yield total
```



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
nums = [
 [-3],
 [-2, -1],
 [0, 1, 2],
 [3, 4, 5, 6],
 [7, 8, 9, 10, 11]
 ]

def cumsum(lst_):
    total = 0
    for val in lst_:
        total += val
        yield total
        
[[*cumsum(row)] for row in nums]

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
[[-3], [-2, -3], [0, 1, 3], [3, 7, 12, 18], [7, 15, 24, 34, 45]]
```


</div>
</div>
</div>

