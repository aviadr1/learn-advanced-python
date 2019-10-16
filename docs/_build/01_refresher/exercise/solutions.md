---
redirect_from:
  - "/01-refresher/exercise/solutions"
interact_link: content/01_refresher/exercise/solutions.ipynb
kernel_name: python3
has_widgets: false
title: 'Solutions'
prev_page:
  url: /01_refresher/exercise/questions.html
  title: 'Questions'
next_page:
  url: /01_refresher/notebooks/generators.html
  title: 'notebooks'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-advanced-python/blob/master/content/01_refresher/exercise/solutions.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




# multi-level sorting

here's a list of fruits and their prices:

```
prices = {
    'apple' : 20, 
    'melon' : 7,
    'peach' : 20,
    'grapes' : 25,
    'watermelon' : 5,
    'apricot' : 7,
    'citrus' : 5
}
fruits_in_store = list(prices.keys())
```
can you use the function `sorted` to `fruits_in_store` first by price and then by alphabetical order?




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
### useful
prices = {
    'apple' : 20, 
    'melon' : 7,
    'peach' : 20,
    'grapes' : 25,
    'watermelon' : 5,
    'apricot' : 7,
    'citrus' : 5
}
fruits_in_store = list(prices.keys())

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# solution 1
def getprice(fruit):
    return prices[fruit]

def price_and_name(fruit):
    return (prices[fruit], fruit)

sorted(fruits_in_store, key=price_and_name)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
['citrus', 'watermelon', 'apricot', 'melon', 'apple', 'peach', 'grapes']
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# solution 2
def identity(fruit):
    return fruit

def make_sorter(key_funcs):
    def sort_key(fruit):
        return tuple(key(fruit) for key in key_funcs)
    return sort_key

sorted(fruits_in_store, key=make_sorter([len, getprice, identity]))
    


```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
<function make_sorter.<locals>.sort_key at 0x00377E40>
```
</div>
</div>
<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
['melon', 'apple', 'peach', 'citrus', 'grapes', 'apricot', 'watermelon']
```


</div>
</div>
</div>



# count repeating words in a song

Count the number of times each word appears in this short song 
```
song = """\
Lovely Spam! Wonderful Spam!
Lovely Spam! Wonderful Spam
Spa-a-a-a-a-a-a-am
Spa-a-a-a-a-a-a-am
Spa-a-a-a-a-a-a-am
Spa-a-a-a-a-a-a-am
Lovely Spam! (Lovely Spam!)
Lovely Spam! (Lovely Spam!)
Lovely Spam!
Spam, Spam, Spam, Spam!
"""
```

you may find certain classes in the module `collections` useful



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
song = """\
Lovely Spam! Wonderful Spam!
Lovely Spam! Wonderful Spam
Spa-a-a-a-a-a-a-am
Spa-a-a-a-a-a-a-am
Spa-a-a-a-a-a-a-am
Spa-a-a-a-a-a-a-am
Lovely Spam! (Lovely Spam!)
Lovely Spam! (Lovely Spam!)
Lovely Spam!
Spam, Spam, Spam, Spam!
"""
song = song.translate(song.maketrans('', '', ',.!()')) # remove annoying chars
words = song.split()
from pprint import pprint

def order_by_value(d):
    return dict(sorted(d.items(), key=lambda item: (item[1], item[0]), reverse=True))

# solution #1
counter = {}
for word in words:
    if word not in counter:
        counter[word] = 1
    else:
        counter[word] +=1
pprint(order_by_value(counter))
print()

# solution #2
counter = {}
for word in words:
    counter[word] = 1+ counter.get(word, 0)
pprint(order_by_value(counter))
print()

# solution #3
import collections
counter = collections.defaultdict(int)
for word in words:
    counter[word] +=1
pprint(order_by_value(counter))
print()

# solution #4
counter = collections.Counter(words)
pprint(order_by_value(counter))
print()

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
{'Lovely': 7, 'Spa-a-a-a-a-a-a-am': 4, 'Spam': 13, 'Wonderful': 2}

{'Lovely': 7, 'Spa-a-a-a-a-a-a-am': 4, 'Spam': 13, 'Wonderful': 2}

{'Lovely': 7, 'Spa-a-a-a-a-a-a-am': 4, 'Spam': 13, 'Wonderful': 2}

{'Lovely': 7, 'Spa-a-a-a-a-a-a-am': 4, 'Spam': 13, 'Wonderful': 2}

```
</div>
</div>
</div>



# file read generator
how is it that we can iterate over lines in a file with a for loop?
in this exercize we will write a generator function that shows how this works in practice.

write a function called `def make_file_reader(f):` that can be used in the following manner:
```
for line in make_file_reader(open('spam.txt')):
    print(line)
```

the `make_file_reader` function should take very little time/memory to run, 
regardless of how big the file is. the file could potentially be 1000GB or more and still take only milliseconds to run.

you are only allowed to use the function `f.readline()` on file objects.





<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def make_file_reader(f):
    line = None
    while line != "":
        line = f.readline()
        yield line


```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
### useful test for your make_file_reader()
with open('spam.txt', 'w') as f: print(song, file=f)

for line in make_file_reader(open('spam.txt')):
    print(line, end='')

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
Lovely Spam Wonderful Spam
Lovely Spam Wonderful Spam
Spa-a-a-a-a-a-a-am
Spa-a-a-a-a-a-a-am
Spa-a-a-a-a-a-a-am
Spa-a-a-a-a-a-a-am
Lovely Spam Lovely Spam
Lovely Spam Lovely Spam
Lovely Spam
Spam Spam Spam Spam

```
</div>
</div>
</div>

