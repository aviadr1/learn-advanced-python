---
redirect_from:
  - "/01-refresher/exercise/questions"
interact_link: content/01_refresher/exercise/questions.ipynb
kernel_name: python3
has_widgets: false
title: 'Questions'
prev_page:
  url: /01_refresher/exercise/questions.html
  title: 'exercise'
next_page:
  url: /01_refresher/exercise/solutions.html
  title: 'Solutions'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-advanced-python/blob/master/content/01_refresher/exercise/questions.ipynb" target="_blank">
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

