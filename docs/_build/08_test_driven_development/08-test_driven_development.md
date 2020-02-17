---
redirect_from:
  - "/08-test-driven-development/08-test-driven-development"
interact_link: content/08_test_driven_development/08-test_driven_development.ipynb
kernel_name: python3
has_widgets: false
title: '08-test Driven Development'
prev_page:
  url: /08_test_driven_development/08-test_driven_development.html
  title: '08 test driven development'
next_page:
  url: /08_test_driven_development/.pytest_cache/README.html
  title: '.pytest cache'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-advanced-python/blob/master/content/08_test_driven_development/08-test_driven_development.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




# useful resources:
1. https://stackabuse.com/test-driven-development-with-pytest/
2. https://docs.pytest.org/en/latest/goodpractices.html#conventions-for-python-test-discovery
3. https://blog.ionelmc.ro/2014/05/25/python-packaging/#the-structure
4. https://github.com/vanzaj/tdd-pytest/blob/master/docs/tdd-pytest/content/tdd-basics.md
5. https://opensource.com/article/18/6/pytest-plugins





# setup



1. install `pytest`
2. install `pytest-sugar` which will give us nicer output



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
pip -q install pytest pytest-sugar

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# move to tdd directory
from pathlib import Path
if Path.cwd().name != 'tdd':
    %mkdir tdd
    %cd tdd

%pwd

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'/content/tdd/tdd'
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# cleanup all files
%rm *.py

```
</div>

</div>



# How pytest discovers tests

pytests uses the following [conventions](https://docs.pytest.org/en/latest/goodpractices.html#conventions-for-python-test-discovery) to automatically discovering tests:
  1. files with tests should be called `test_*.py` or `*_test.py `
  2. test function name should start with `test_`






# our first test
to see if our code works, we can use the `assert` python keyword. pytest adds hooks to assertions to make them more useful



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
%%file test_math.py

import math
def test_add():
    assert 1+1 == 2

def test_mul():
    assert 6*7 == 42

def test_sin():
    assert math.sin(0) == 0

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
Writing test_math.py
```
</div>
</div>
</div>



now lets run pytest



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
!python -m pytest test_math.py 

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
[1mTest session starts (platform: linux, Python 3.6.9, pytest 5.3.5, pytest-sugar 0.9.2)[0m
rootdir: /content
plugins: sugar-0.9.2, xdist-1.31.0, forked-1.1.3, timeout-1.3.4
[1mcollecting ... [0m
 [36m[0mtest_math.py[0m [32m✓[0m[32m✓[0m[32m✓[0m                                                [32m100% [0m[40m[32m█[0m[40m[32m██[0m[40m[32m█[0m[40m[32m██[0m[40m[32m█[0m[40m[32m███[0m

Results (0.02s):
[32m       3 passed[0m
```
</div>
</div>
</div>



Great! we just wrote 3 tests that shows that basic math still works

Hurray!



## your turn

write a test for the following function. 

if there is a bug in the function, fix it




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
%%file make_triangle.py

# version 1

def make_triangle(n):
    """
    draws a triangle using '@' letters
    for instance:
        >>> print('\n'.join(make_triangle(3))
        @
        @@
        @@@
    """

    for i in range(n):
        yield '@' * i


```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
Writing make_triangle.py
```
</div>
</div>
</div>



## solution




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
%%file test_make_triangle.py

from make_triangle import make_triangle

def test_make_triangle():
    expected = "@"
    actual = '\n'.join(make_triangle(1))
    assert actual == expected

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
Overwriting test_make_triangle.py
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
!python -m pytest test_make_triangle.py

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
[1mTest session starts (platform: linux, Python 3.6.9, pytest 5.3.5, pytest-sugar 0.9.2)[0m
rootdir: /content
plugins: sugar-0.9.2, xdist-1.31.0, forked-1.1.3, timeout-1.3.4
[1mcollecting ... [0m

―――――――――――――――――――――――――――――― test_make_triangle ――――――――――――――――――――――――――――――

[1m    def test_make_triangle():[0m
[1m        expected = "@"[0m
[1m        actual = '\n'.join(make_triangle(1))[0m
[1m>       assert actual == expected[0m
[1m[31mE       AssertionError: assert '' == '@'[0m
[1m[31mE         + @[0m

[1m[31mtest_make_triangle.py[0m:7: AssertionError

 [36m[0mtest_make_triangle.py[0m [31m⨯[0m                                         [31m100% [0m[40m[31m█[0m[40m[31m█████████[0m

Results (0.04s):
[31m       1 failed[0m
         - [36m[0mtest_make_triangle.py[0m:4 [31mtest_make_triangle[0m
```
</div>
</div>
</div>



so the expected starts with `'@'` and the actual starts with `''` ...

this is a bug! lets fix the code and re-run



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
%%file make_triangle.py

# version 2 
def make_triangle(n):
    """
    draws a triangle using '@' letters
    for instance:
        >>> print('\n'.join(make_triangle(3))
        @
        @@
        @@@
    """

    for i in range(1, n+1):
        yield '@' * i

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
Overwriting make_triangle.py
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
!python -m pytest test_make_triangle.py

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
[1m============================= test session starts ==============================[0m
platform linux -- Python 3.6.9, pytest-3.6.4, py-1.8.1, pluggy-0.7.1
rootdir: /content, inifile:
collected 1 item                                                               [0m

test_make_triangle.py .[36m                                                  [100%][0m

[32m[1m=========================== 1 passed in 0.01 seconds ===========================[0m
```
</div>
</div>
</div>



# Pytest context-sensitive comparisons
[Reference](https://docs.pytest.org/en/3.0.1/assert.html#making-use-of-context-sensitive-comparisons)

pytest has rich support for providing context-sensitive information when it encounters comparisons. 

Special comparisons are done for a number of cases:
- comparing long strings: a context diff is shown
- comparing long sequences: first failing indices
- comparing dicts: different entries

Here's how this looks like for set:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
%%file test_compare_fruits.py
def test_set_comparison():
    set1 = set(['Apples', 'Bananas', 'Watermelon', 'Pear',  'Guave', 'Carambola', 'Plum'])
    set2 = set(['Plum', 'Apples', 'Grapes', 'Watermelon','Pear', 'Guave', 'Carambola',  'Melon' ])
    assert set1 == set2

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
Writing test_compare_fruits.py
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
!python -m pytest test_compare_fruits.py

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
[1mTest session starts (platform: linux, Python 3.6.9, pytest 5.3.5, pytest-sugar 0.9.2)[0m
rootdir: /content
plugins: sugar-0.9.2, xdist-1.31.0, forked-1.1.3, timeout-1.3.4
[1mcollecting ... [0m

――――――――――――――――――――――――――――― test_set_comparison ――――――――――――――――――――――――――――――

[1m    def test_set_comparison():[0m
[1m        set1 = set(['Apples', 'Bananas', 'Watermelon', 'Pear',  'Guave', 'Carambola', 'Plum'])[0m
[1m        set2 = set(['Plum', 'Apples', 'Grapes', 'Watermelon','Pear', 'Guave', 'Carambola',  'Melon' ])[0m
[1m>       assert set1 == set2[0m
[1m[31mE       AssertionError: assert {'Apples', 'B..., 'Plum', ...} == {'Apples', 'C..., 'Pear', ...}[0m
[1m[31mE         Extra items in the left set:[0m
[1m[31mE         'Bananas'[0m
[1m[31mE         Extra items in the right set:[0m
[1m[31mE         'Melon'[0m
[1m[31mE         'Grapes'[0m
[1m[31mE         Use -v to get the full diff[0m

[1m[31mtest_compare_fruits.py[0m:4: AssertionError

 [36m[0mtest_compare_fruits.py[0m [31m⨯[0m                                        [31m100% [0m[40m[31m█[0m[40m[31m█████████[0m

Results (0.03s):
[31m       1 failed[0m
         - [36m[0mtest_compare_fruits.py[0m:1 [31mtest_set_comparison[0m
```
</div>
</div>
</div>



## your turn

test the following function `count_words()` and fix any bugs.

the expected output from the function is given in `expected_output`



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
expected_output = {
 'and': 2,
 'chief': 2,
 'didnt': 1,
 'efficiency': 1,
 'expected': 1,
 'expects': 1,
 'fear': 2,
 'i': 1,
 'inquisition': 2,
 'is': 1,
 'no': 1,
 'one': 1,
 'our': 1,
 'ruthless': 1,
 'spanish': 2,
 'surprise': 3,
 'the': 2,
 'two': 1,
 'weapon': 1,
 'weapons': 1,
 'well': 1}

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
%%file spanish_inquisition.py
# version 1: buggy
import collections

quote = """
Well, I didn't expected the Spanish Inquisition ...
No one expects the Spanish Inquisition!
Our chief weapon is surprise, fear and surprise;
two chief weapons, fear, surprise, and ruthless efficiency! 
"""

def remove_punctuation(quote):
    quote.translate(str.maketrans('', '', "',.!?;")).lower()
    return quote

def count_words(quote):
    quote = remove_punctuation(quote)
    return dict(collections.Counter(quote.split(' ')))

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
Overwriting spanish_inquisition.py
```
</div>
</div>
</div>



## solution





<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
%%file test_spanish_inquisition.py

from spanish_inquisition import *

expected_output = {
 'and': 2,
 'chief': 2,
 'didnt': 1,
 'efficiency': 1,
 'expected': 1,
 'expects': 1,
 'fear': 2,
 'i': 1,
 'inquisition': 2,
 'is': 1,
 'no': 1,
 'one': 1,
 'our': 1,
 'ruthless': 1,
 'spanish': 2,
 'surprise': 3,
 'the': 2,
 'two': 1,
 'weapon': 1,
 'weapons': 1,
 'well': 1}

def test_spanish_inquisition():
    actual = count_words(quote)
    assert actual == expected_output

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
Overwriting test_spanish_inquisition.py
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
!python -m pytest -vv test_spanish_inquisition.py

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
[1mTest session starts (platform: linux, Python 3.6.9, pytest 5.3.5, pytest-sugar 0.9.2)[0m
cachedir: .pytest_cache
rootdir: /content
plugins: sugar-0.9.2, xdist-1.31.0, forked-1.1.3, timeout-1.3.4
[1mcollecting ... [0m

――――――――――――――――――――――――――― test_spanish_inquisition ―――――――――――――――――――――――――――

[1m    def test_spanish_inquisition():[0m
[1m        actual = count_words(quote)[0m
[1m>       assert actual == expected_output[0m
[1m[31mE       assert {'\n': 1,\n '\nWell,': 1,\n '...\nNo': 1,\n 'I': 1,\n 'Inquisition': 1,\n 'Inquisition!\nOur': 1,\n 'Spanish': 2,\n 'and': 2,\n 'chief': 2,\n "didn't": 1,\n 'efficiency!': 1,\n 'expected': 1,\n 'expects': 1,\n 'fear': 1,\n 'fear,': 1,\n 'is': 1,\n 'one': 1,\n 'ruthless': 1,\n 'surprise,': 2,\n 'surprise;\ntwo': 1,\n 'the': 2,\n 'weapon': 1,\n 'weapons,': 1} == {'and': 2,\n 'chief': 2,\n 'didnt': 1,\n 'efficiency': 1,\n 'expected': 1,\n 'expects': 1,\n 'fear': 2,\n 'i': 1,\n 'inquisition': 2,\n 'is': 1,\n 'no': 1,\n 'one': 1,\n 'our': 1,\n 'ruthless': 1,\n 'spanish': 2,\n 'surprise': 3,\n 'the': 2,\n 'two': 1,\n 'weapon': 1,\n 'weapons': 1,\n 'well': 1}[0m
[1m[31mE         Common items:[0m
[1m[31mE         {'and': 2,[0m
[1m[31mE          'chief': 2,[0m
[1m[31mE          'expected': 1,[0m
[1m[31mE          'expects': 1,[0m
[1m[31mE          'is': 1,[0m
[1m[31mE          'one': 1,[0m
[1m[31mE          'ruthless': 1,[0m
[1m[31mE          'the': 2,[0m
[1m[31mE          'weapon': 1}[0m
[1m[31mE         Differing items:[0m
[1m[31mE         {'fear': 1} != {'fear': 2}[0m
[1m[31mE         Left contains 13 more items:[0m
[1m[31mE         {'\n': 1,[0m
[1m[31mE          '\nWell,': 1,[0m
[1m[31mE          '...\nNo': 1,[0m
[1m[31mE          'I': 1,[0m
[1m[31mE          'Inquisition': 1,[0m
[1m[31mE          'Inquisition!\nOur': 1,[0m
[1m[31mE          'Spanish': 2,[0m
[1m[31mE          "didn't": 1,[0m
[1m[31mE          'efficiency!': 1,[0m
[1m[31mE          'fear,': 1,[0m
[1m[31mE          'surprise,': 2,[0m
[1m[31mE          'surprise;\ntwo': 1,[0m
[1m[31mE          'weapons,': 1}[0m
[1m[31mE         Right contains 11 more items:[0m
[1m[31mE         {'didnt': 1,[0m
[1m[31mE          'efficiency': 1,[0m
[1m[31mE          'i': 1,[0m
[1m[31mE          'inquisition': 2,[0m
[1m[31mE          'no': 1,[0m
[1m[31mE          'our': 1,[0m
[1m[31mE          'spanish': 2,[0m
[1m[31mE          'surprise': 3,[0m
[1m[31mE          'two': 1,[0m
[1m[31mE          'weapons': 1,[0m
[1m[31mE          'well': 1}[0m
[1m[31mE         Full diff:[0m
[1m[31mE           {[0m
[1m[31mE         -  '\n': 1,[0m
[1m[31mE         -  '\nWell,': 1,[0m
[1m[31mE         -  '...\nNo': 1,[0m
[1m[31mE         -  'I': 1,[0m
[1m[31mE         -  'Inquisition': 1,[0m
[1m[31mE         -  'Inquisition!\nOur': 1,[0m
[1m[31mE         -  'Spanish': 2,[0m
[1m[31mE            'and': 2,[0m
[1m[31mE            'chief': 2,[0m
[1m[31mE         -  "didn't": 1,[0m
[1m[31mE         ?  ^     --[0m
[1m[31mE         +  'didnt': 1,[0m
[1m[31mE         ?  ^    +[0m
[1m[31mE         -  'efficiency!': 1,[0m
[1m[31mE         ?             -[0m
[1m[31mE         +  'efficiency': 1,[0m
[1m[31mE            'expected': 1,[0m
[1m[31mE            'expects': 1,[0m
[1m[31mE         -  'fear': 1,[0m
[1m[31mE         ?          ^[0m
[1m[31mE         +  'fear': 2,[0m
[1m[31mE         ?          ^[0m
[1m[31mE         -  'fear,': 1,[0m
[1m[31mE         +  'i': 1,[0m
[1m[31mE         +  'inquisition': 2,[0m
[1m[31mE            'is': 1,[0m
[1m[31mE         +  'no': 1,[0m
[1m[31mE            'one': 1,[0m
[1m[31mE         +  'our': 1,[0m
[1m[31mE            'ruthless': 1,[0m
[1m[31mE         +  'spanish': 2,[0m
[1m[31mE         -  'surprise,': 2,[0m
[1m[31mE         ?           -   ^[0m
[1m[31mE         +  'surprise': 3,[0m
[1m[31mE         ?              ^[0m
[1m[31mE         -  'surprise;\ntwo': 1,[0m
[1m[31mE            'the': 2,[0m
[1m[31mE         +  'two': 1,[0m
[1m[31mE            'weapon': 1,[0m
[1m[31mE         -  'weapons,': 1,[0m
[1m[31mE         ?          -[0m
[1m[31mE         +  'weapons': 1,[0m
[1m[31mE         +  'well': 1,[0m
[1m[31mE           }[0m

[1m[31mtest_spanish_inquisition.py[0m:29: AssertionError

 [36mtest_spanish_inquisition.py[0m::test_spanish_inquisition[0m [31m⨯[0m         [31m100% [0m[40m[31m█[0m[40m[31m█████████[0m

Results (0.04s):
[31m       1 failed[0m
         - [36m[0mtest_spanish_inquisition.py[0m:27 [31mtest_spanish_inquisition[0m
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
%%file spanish_inquisition.py
# version 2: fixed
import collections

quote = """
Well, I didn't expected the Spanish Inquisition ...
No one expects the Spanish Inquisition!
Our chief weapon is surprise, fear and surprise;
two chief weapons, fear, surprise, and ruthless efficiency! 
"""

def remove_punctuation(quote):
    # quote.translate(str.maketrans('', '', "',.!?;")).lower() # BUG: missing return
    return quote.translate(str.maketrans('', '', "',.!?;")).lower()

def count_words(quote):
    quote = remove_punctuation(quote)
    # return dict(collections.Counter(quote.split(' '))) # BUG
    return dict(collections.Counter(quote.split()))

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
Overwriting spanish_inquisition.py
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
!python -m pytest -vv test_spanish_inquisition.py

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
[1mTest session starts (platform: linux, Python 3.6.9, pytest 5.3.5, pytest-sugar 0.9.2)[0m
cachedir: .pytest_cache
rootdir: /content
plugins: sugar-0.9.2, xdist-1.31.0, forked-1.1.3, timeout-1.3.4
[1mcollecting ... [0m
 [36mtest_spanish_inquisition.py[0m::test_spanish_inquisition[0m [32m✓[0m         [32m100% [0m[40m[32m█[0m[40m[32m█████████[0m

Results (0.02s):
[32m       1 passed[0m
```
</div>
</div>
</div>



# Using fixtures to simplify tests





## Motivating example

Lets look at an example of class `Person`, where each person has a name and remembers their friends.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
%%file person.py

#version 1
class Person:
    def __init__(self, name, favorite_color, year_born):
        self.name = name
        self.favorite_color = favorite_color
        self.year_born = year_born
        self.friends = set()

    def add_friend(self, other_person):
        if not isinstance(other_person, Person): raise TypeError(other_person, 'is not a', Person)
        self.friends.add(other_person)
        other_person.friends.add(self)

    def __repr__(self):
        return f'Person(name={self.name!r}, '  \
               f'favorite_color={self.favorite_color!r}, ' \
               f'year_born={self.year_born!r}, ' \
               f'friends={[f.name for f in self.friends]})'


```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
Overwriting person.py
```
</div>
</div>
</div>



Lets write a test for `add_friend()` function.

notice how the setup for the test is taking so much of the function, while also requiring _inventing_ a lot of repetitious data

is there a way to reduce this boiler plate code



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
%%file test_person.py

from person import Person

def test_name():
    # setup
    terry = Person(
        'Terry Gilliam',
        'red',
        1940
        )
    
    # test
    assert terry.name == 'Terry Gilliam' 


def test_add_friend():
    # setup for the test 
    terry = Person(
        'Terry Gilliam',
        'red',
        1940
        )
    eric = Person(
        'Eric Idle',
        'blue',
        1943
        )
    
    # actual test
    terry.add_friend(eric)
    assert eric in terry.friends
    assert terry in eric.friends

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
Overwriting test_person.py
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
!python -m pytest -q test_person.py

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
..[36m                                                                       [100%][0m
[32m[1m2 passed in 0.01 seconds[0m
```
</div>
</div>
</div>



## Fixtures to the rescue






what is we had a magic factory that can conjure up a name, favorite color and birth year?

then we could write our `test_name()` more simply like this:

```python
def test_name(person_name, favorite_color, birth_year):
    person = Person(person_name, favorite_color, birth_year)
    
    # test
    assert person.name == person_name 
```




furthermore, if we had a magic factory that can create `terry` and `eric` we could write our `test_add_friend()` function like this:

```python
def test_add_friend(eric, terry):
    eric.add_friend(terry)
    assert eric in terry.friends
    assert terry in eric.friends
```




fixtures in `pytest` allow us to create such magic factories using the `@pytest.fixture` notation.

here's an example:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
%%file test_person_fixtures1.py

import pytest
from person import Person

@pytest.fixture
def person_name():
    return 'Terry Gilliam'

@pytest.fixture
def birth_year():
    return 1940

@pytest.fixture
def favorite_color():
    return 'red'

def test_person_name(person_name, favorite_color, birth_year):
    person = Person(person_name, favorite_color, birth_year)
 
    # test
    assert person.name == person_name 

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
Overwriting test_person_fixtures1.py
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
!python -m pytest test_person_fixtures1.py

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
[1m============================= test session starts ==============================[0m
platform linux -- Python 3.6.9, pytest-3.6.4, py-1.8.1, pluggy-0.7.1
rootdir: /content, inifile:
collected 1 item                                                               [0m

test_person_fixtures1.py .[36m                                               [100%][0m

[32m[1m=========================== 1 passed in 0.02 seconds ===========================[0m
```
</div>
</div>
</div>



what's happening here?

`pytest` sees that the test function `test_person_name(person_name, favorite_color, birth_year)` requires three parameters, and searches for fixtures annotated with `@pytest.fixture` with the same name.

when it finds them, it calls these fixtures on our behalf, and passes the return value as the parameter. in effect, it calls

```python
test_person_name(person_name=person_name(), favorite_color=favorite_color(), birth_year=birth_year()
```

note how much code this saves



## your turn
1. rewrite the `test_add_friend` function to accept two parameters `def test_add_friend(eric, terry)` 
2. write fixtures for eric and terry
3. run pytest



## solution




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
%%file test_person_fixtures2.py

import pytest
from person import Person

@pytest.fixture
def eric():
    return Person('Eric Idle', 'red', 1943)

@pytest.fixture
def terry():
    return Person('Terry Gilliam', 'blue', 1940)

def test_add_friend(eric, terry):
    eric.add_friend(terry)
    assert eric in terry.friends
    assert terry in eric.friends
    

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
Writing test_person_fixtures2.py
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
!python -m pytest -q test_person_fixtures2.py

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
.[36m                                                                        [100%][0m
[32m[1m1 passed in 0.02 seconds[0m
```
</div>
</div>
</div>



# parameterizing fixtures

Fixture functions can be parametrized in which case they will be called multiple times, each time executing the set of dependent tests, i. e. the tests that depend on this fixture. 

Test functions usually do not need to be aware of their re-running. Fixture parametrization helps to write exhaustive functional tests for components which themselves can be configured in multiple ways.





<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
%%file test_primes.py

import pytest
import math

def is_prime(x):
    return all(x % factor != 0 for factor in range(2, int(x/2)))

@pytest.fixture(params=[2,3,5,7,11, 13, 17, 19, 101])
def prime_number(request):
    return request.param

def test_prime(prime_number):
    assert is_prime(prime_number) == True

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
Overwriting test_primes.py
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
!python -m pytest --verbose test_primes.py

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
[1m============================= test session starts ==============================[0m
platform linux -- Python 3.6.9, pytest-3.6.4, py-1.8.1, pluggy-0.7.1 -- /usr/bin/python3
cachedir: .pytest_cache
rootdir: /content, inifile:
collected 9 items                                                              [0m

test_primes.py::test_prime[2] [32mPASSED[0m[36m                                     [ 11%][0m
test_primes.py::test_prime[3] [32mPASSED[0m[36m                                     [ 22%][0m
test_primes.py::test_prime[5] [32mPASSED[0m[36m                                     [ 33%][0m
test_primes.py::test_prime[7] [32mPASSED[0m[36m                                     [ 44%][0m
test_primes.py::test_prime[11] [32mPASSED[0m[36m                                    [ 55%][0m
test_primes.py::test_prime[13] [32mPASSED[0m[36m                                    [ 66%][0m
test_primes.py::test_prime[17] [32mPASSED[0m[36m                                    [ 77%][0m
test_primes.py::test_prime[19] [32mPASSED[0m[36m                                    [ 88%][0m
test_primes.py::test_prime[101] [32mPASSED[0m[36m                                   [100%][0m

[32m[1m=========================== 9 passed in 0.03 seconds ===========================[0m
```
</div>
</div>
</div>



## your turn

test `is_prime()` for non prime numbers
> bonus: can you find and fix the bug in `is_prime()` using a test?



## solution



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
%%file test_non_primes.py

import pytest

FIX_BUG = True
if FIX_BUG:
    def is_prime_fixed(x):
        # notice the +1 - it is important when x=4
        return all(x % factor != 0 for factor in range(2, int(x/2) + 1))
    is_prime = is_prime_fixed
else:
    from test_primes import is_prime

@pytest.fixture(params=[4, 6, 8, 9, 10, 12, 14, 15, 16, 28, 60, 100])
def non_prime_number(request):
    return request.param

def test_non_primes(non_prime_number):
    assert is_prime(non_prime_number) == False

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
Overwriting test_non_primes.py
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
!python -m pytest --verbose test_non_primes.py

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
[1m============================= test session starts ==============================[0m
platform linux -- Python 3.6.9, pytest-3.6.4, py-1.8.1, pluggy-0.7.1 -- /usr/bin/python3
cachedir: .pytest_cache
rootdir: /content, inifile:
collected 12 items                                                             [0m

test_non_primes.py::test_non_primes[4] [32mPASSED[0m[36m                            [  8%][0m
test_non_primes.py::test_non_primes[6] [32mPASSED[0m[36m                            [ 16%][0m
test_non_primes.py::test_non_primes[8] [32mPASSED[0m[36m                            [ 25%][0m
test_non_primes.py::test_non_primes[9] [32mPASSED[0m[36m                            [ 33%][0m
test_non_primes.py::test_non_primes[10] [32mPASSED[0m[36m                           [ 41%][0m
test_non_primes.py::test_non_primes[12] [32mPASSED[0m[36m                           [ 50%][0m
test_non_primes.py::test_non_primes[14] [32mPASSED[0m[36m                           [ 58%][0m
test_non_primes.py::test_non_primes[15] [32mPASSED[0m[36m                           [ 66%][0m
test_non_primes.py::test_non_primes[16] [32mPASSED[0m[36m                           [ 75%][0m
test_non_primes.py::test_non_primes[28] [32mPASSED[0m[36m                           [ 83%][0m
test_non_primes.py::test_non_primes[60] [32mPASSED[0m[36m                           [ 91%][0m
test_non_primes.py::test_non_primes[100] [32mPASSED[0m[36m                          [100%][0m

[32m[1m========================== 12 passed in 0.03 seconds ===========================[0m
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
all([factor for factor in range(2, int(4/2))])

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
True
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
!python -m pytest --verbose test_primes.py

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
[1m============================= test session starts ==============================[0m
platform linux -- Python 3.6.9, pytest-3.6.4, py-1.8.1, pluggy-0.7.1 -- /usr/bin/python3
cachedir: .pytest_cache
rootdir: /content, inifile:
collected 21 items                                                             [0m

test_primes.py::test_prime[2] [32mPASSED[0m[36m                                     [  4%][0m
test_primes.py::test_prime[3] [32mPASSED[0m[36m                                     [  9%][0m
test_primes.py::test_prime[5] [32mPASSED[0m[36m                                     [ 14%][0m
test_primes.py::test_prime[7] [32mPASSED[0m[36m                                     [ 19%][0m
test_primes.py::test_prime[11] [32mPASSED[0m[36m                                    [ 23%][0m
test_primes.py::test_prime[13] [32mPASSED[0m[36m                                    [ 28%][0m
test_primes.py::test_prime[17] [32mPASSED[0m[36m                                    [ 33%][0m
test_primes.py::test_prime[19] [32mPASSED[0m[36m                                    [ 38%][0m
test_primes.py::test_prime[101] [32mPASSED[0m[36m                                   [ 42%][0m
test_primes.py::test_non_primes[4] [31mFAILED[0m[36m                                [ 47%][0m
test_primes.py::test_non_primes[6] [32mPASSED[0m[36m                                [ 52%][0m
test_primes.py::test_non_primes[8] [32mPASSED[0m[36m                                [ 57%][0m
test_primes.py::test_non_primes[9] [32mPASSED[0m[36m                                [ 61%][0m
test_primes.py::test_non_primes[10] [32mPASSED[0m[36m                               [ 66%][0m
test_primes.py::test_non_primes[12] [32mPASSED[0m[36m                               [ 71%][0m
test_primes.py::test_non_primes[14] [32mPASSED[0m[36m                               [ 76%][0m
test_primes.py::test_non_primes[15] [32mPASSED[0m[36m                               [ 80%][0m
test_primes.py::test_non_primes[16] [32mPASSED[0m[36m                               [ 85%][0m
test_primes.py::test_non_primes[28] [32mPASSED[0m[36m                               [ 90%][0m
test_primes.py::test_non_primes[60] [32mPASSED[0m[36m                               [ 95%][0m
test_primes.py::test_non_primes[100] [32mPASSED[0m[36m                              [100%][0m

=================================== FAILURES ===================================
[31m[1m______________________________ test_non_primes[4] ______________________________[0m

non_prime_number = 4

[1m    def test_non_primes(non_prime_number):[0m
[1m>       assert is_prime(non_prime_number) == False[0m
[1m[31mE       assert True == False[0m
[1m[31mE        +  where True = is_prime(4)[0m

[1m[31mtest_primes.py[0m:20: AssertionError
[31m[1m===================== 1 failed, 20 passed in 0.06 seconds ======================[0m
```
</div>
</div>
</div>



# printing and logging within tests




## printing
[Reference](https://docs.pytest.org/en/latest/capture.html)

You can use prints within tests to provide additional debug info.

pytest redirects the output and captured the output of each test. it then:
- __suppresses__ the output of all __successful__ tests (for brevity)
- __shows__ the output off all __failed__ tests (for debugging)
- both `stdout` and `stderr` are captured




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
%%file test_prints.py
import sys

def test_print_success():
    print(
        """
        @@@@@@@@@@@@@@@
        this statement will NOT be printed
        @@@@@@@@@@@@@@@
        """
    )

    assert 6*7 == 42

def test_print_fail():

    print(
        """
        @@@@@@@@@@@@@@@
        this statement WILL be printed
        @@@@@@@@@@@@@@@
        """
    )
    assert True == False


def test_stderr_capture_success():
    print(
        """
        @@@@@@@@@@@@@@@
        this STDERR statement will NOT be printed
        @@@@@@@@@@@@@@@
        """, 
        file=sys.stderr
    )
     
    assert True


def test_stderr_capture_fail():
    print(
        """
        @@@@@@@@@@@@@@@
        this STDERR statement WILL be printed
        @@@@@@@@@@@@@@@
        """, 
        file=sys.stderr
    )
     
    assert False


```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
Overwriting test_prints.py
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
!python -m pytest -q test_prints.py

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
.F.F[36m                                                                     [100%][0m
=================================== FAILURES ===================================
[31m[1m_______________________________ test_print_fail ________________________________[0m

[1m    def test_print_fail():[0m
[1m    [0m
[1m        print([0m
[1m            """[0m
[1m            @@@@@@@@@@@@@@@[0m
[1m            this statement WILL be printed[0m
[1m            @@@@@@@@@@@@@@@[0m
[1m            """[0m
[1m        )[0m
[1m>       assert True == False[0m
[1m[31mE       assert True == False[0m

[1m[31mtest_prints.py[0m:23: AssertionError
----------------------------- Captured stdout call -----------------------------

        @@@@@@@@@@@@@@@
        this statement WILL be printed
        @@@@@@@@@@@@@@@
        
[31m[1m___________________________ test_stderr_capture_fail ___________________________[0m

[1m    def test_stderr_capture_fail():[0m
[1m        print([0m
[1m            """[0m
[1m            @@@@@@@@@@@@@@@[0m
[1m            this STDERR statement WILL be printed[0m
[1m            @@@@@@@@@@@@@@@[0m
[1m            """,[0m
[1m            file=sys.stderr[0m
[1m        )[0m
[1m    [0m
[1m>       assert False[0m
[1m[31mE       assert False[0m

[1m[31mtest_prints.py[0m:49: AssertionError
----------------------------- Captured stderr call -----------------------------

        @@@@@@@@@@@@@@@
        this STDERR statement WILL be printed
        @@@@@@@@@@@@@@@
        
[31m[1m2 failed, 2 passed in 0.04 seconds[0m
```
</div>
</div>
</div>



## logging
[Reference](https://docs.pytest.org/en/latest/logging.html)

pytest captures log messages of level WARNING or above automatically and displays them in their own section for each failed test in the same manner as captured stdout and stderr.

- WARNING and above will displayed for failed tests
- INFO and below will not be displayed

example:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
%%file test_logging.py

import logging

logger = logging.getLogger(__name__)

def test_logging_warning_success():
    logger.warning('\n\n @@@ this will NOT be printed \n\n')
    assert True

def test_logging_warning_fail():
    logger.warning('\n\n @@@ this WILL be printed @@@ \n\n')
    assert False

def test_logging_info_fail():
    logger.info('\n\n @@@ this will NOT be printed @@@ \n\n')
    assert False


```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
Overwriting test_logging.py
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
!python -m pytest test_logging.py

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
[1m============================= test session starts ==============================[0m
platform linux -- Python 3.6.9, pytest-3.6.4, py-1.8.1, pluggy-0.7.1
rootdir: /content, inifile:
collected 3 items                                                              [0m

test_logging.py .FF[36m                                                      [100%][0m

=================================== FAILURES ===================================
[31m[1m__________________________ test_logging_warning_fail ___________________________[0m

[1m    def test_logging_warning_fail():[0m
[1m        logger.warning('\n\n @@@ this WILL be printed @@@ \n\n')[0m
[1m>       assert False[0m
[1m[31mE       assert False[0m

[1m[31mtest_logging.py[0m:12: AssertionError
------------------------------ Captured log call -------------------------------
test_logging.py             11 WARNING  

 @@@ this WILL be printed @@@
[31m[1m____________________________ test_logging_info_fail ____________________________[0m

[1m    def test_logging_info_fail():[0m
[1m        logger.info('\n\n @@@ this will NOT be printed @@@ \n\n')[0m
[1m>       assert False[0m
[1m[31mE       assert False[0m

[1m[31mtest_logging.py[0m:16: AssertionError
[31m[1m====================== 2 failed, 1 passed in 0.04 seconds ======================[0m
```
</div>
</div>
</div>



## your turn

We give below an implementation of the _FizzBuzz_ puzzle:
> Write a function that returns the numbers from 1 to 100. But for multiples of three returns “Fizz” instead of the number and for the multiples of five returns “Buzz”. For numbers which are multiples of both three and five return “FizzBuzz”.

thus this SHOULD be true
```python
>>> fizzbuzz() # should return the following (abridged) output
[1, 2, 'Fizz', 4, 'Buzz', 6, 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz', ... ]
```

BUT the implementation is buggy. can you write tests for it and fix it?




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
%%file fizzbuzz.py

def is_multiple(n, divisor):
    return n % divisor == 0

def fizzbuzz():
    """
    expected output: list with elements numbers 
        [1, 2, 'Fizz', 4, 'Buzz', 6, 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz', ... ]
    """
    result = []
    for i in range(100):
        if is_multiple(i, 3):
            return "Fizz"
        elif is_multiple(i, 5):
            return "Buzz"
        elif is_multiple(i, 3) and is_multiple(i, 5):
            return "FizzBuzz"
        else:
            return i
    
    return result

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
Overwriting fizzbuzz.py
```
</div>
</div>
</div>



## solution




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
%%file test_fizzbuzz.py

FIX_BUG = 1
if not FIX_BUG:
    from fizzbuzz import fizzbuzz
else:
    def fizzbuzz_fixed():
        def translate(i):
            if i%3 == 0 and i%5 == 0:
                return "FizzBuzz"
            elif i%3 == 0:
                return "Fizz"
            elif i%5 == 0:
                return "Buzz"
            else:
                return i

        return [translate(i) for i in range(1, 100+1)]

    fizzbuzz = fizzbuzz_fixed


import pytest
@pytest.fixture
def fizzbuzz_result():
    result = fizzbuzz()
    print(result)
    return result

@pytest.fixture
def fizzbuzz_dict(fizzbuzz_result):
    return dict(enumerate(fizzbuzz_result, 1))

def test_fizzbuzz_len(fizzbuzz_result):
    assert len(fizzbuzz_result) == 100

def test_fizzbuzz_len(fizzbuzz_result):
    assert type(fizzbuzz_result) == list

def test_fizzbuzz_first_element(fizzbuzz_dict):
    assert fizzbuzz_dict[1] == 1

def test_fizzbuzz_3(fizzbuzz_dict):
    assert fizzbuzz_dict[3] == 'Fizz'

def test_fizzbuzz_5(fizzbuzz_dict):
    assert fizzbuzz_dict[5] == 'Buzz'

def test_fizzbuzz_15(fizzbuzz_dict):
    assert fizzbuzz_dict[15] == 'FizzBuzz'




```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
Overwriting test_fizzbuzz.py
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
!python -m pytest test_fizzbuzz.py

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
[1m============================= test session starts ==============================[0m
platform linux -- Python 3.6.9, pytest-3.6.4, py-1.8.1, pluggy-0.7.1
rootdir: /content, inifile:
collected 5 items                                                              [0m

test_fizzbuzz.py .....[36m                                                   [100%][0m

[32m[1m=========================== 5 passed in 0.03 seconds ===========================[0m
```
</div>
</div>
</div>



# float: when things are (almost) equal
[Reference](https://docs.pytest.org/en/latest/reference.html#pytest-approx)

consider the following code, what do you expect the result to be?
```
x = 0.1 + 0.2
y = 0.3
print('x == y', x ==y) # what will it print?
```



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
x = 0.1 + 0.2
y = 0.3
print('x == y:', x == y) # what will it print?

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
x == y: False
```
</div>
</div>
</div>



if you had anticipated `True` it means you haven't tried testing code with `float` data yet



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
print(x, '!=', y)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
0.30000000000000004 != 0.3
```
</div>
</div>
</div>



the issue is that float is _approxiamtely_ accurate (enough for most calculations) but may have small rounding errors.

here'e a common but ugly way to test for float equivalence



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
abs((0.1 + 0.2) - 0.3) < 1e-6

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
True
```


</div>
</div>
</div>



here's a more pythonic and pytest-tic way, using `pytest.approx`



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
from pytest import approx
0.1 + 0.2 == approx(0.3)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
True
```


</div>
</div>
</div>



## your turn





test that 
- `math.sin(0) == 0`, 
- `math.sin(math.pi / 2) == 1`
- `math.sin(math.pi) == 0`
- `math.sin(math.pi * 3/2) == -1`
- `math.sin(math.pi * 2) == 0`



## solution



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
%%file test_sin.py

from pytest import approx
import math
def test_sin():
    assert math.sin(0) == 0
    assert math.sin(math.pi / 2) == 1
    assert math.sin(math.pi) == approx(0)
    assert math.sin(math.pi * 3/2) == approx(-1)
    assert math.sin(math.pi * 2) == approx(0)


```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
Overwriting test_sin.py
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
!python -m pytest test_sin.py

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
[1m============================= test session starts ==============================[0m
platform linux -- Python 3.6.9, pytest-3.6.4, py-1.8.1, pluggy-0.7.1
rootdir: /content, inifile:
collected 1 item                                                               [0m

test_sin.py F[36m                                                            [100%][0m

=================================== FAILURES ===================================
[31m[1m___________________________________ test_sin ___________________________________[0m

[1m    def test_sin():[0m
[1m        assert math.sin(0) == 0[0m
[1m        assert math.sin(math.pi / 2) == 1[0m
[1m>       assert math.sin(math.pi) == 0 #approx(0)[0m
[1m[31mE       assert 1.2246467991473532e-16 == 0[0m
[1m[31mE        +  where 1.2246467991473532e-16 = <built-in function sin>(3.141592653589793)[0m
[1m[31mE        +    where <built-in function sin> = math.sin[0m
[1m[31mE        +    and   3.141592653589793 = math.pi[0m

[1m[31mtest_sin.py[0m:7: AssertionError
[31m[1m=========================== 1 failed in 0.03 seconds ===========================[0m
```
</div>
</div>
</div>



# adding timeouts to tests
[Reference](https://pypi.org/project/pytest-timeout/)

Sometimes code gets stuck in an infinite loop, or waiting for a response from a server.
Sometimes, tests that run too long is in _itself_ an indication of failure.

how can we add timeouts to tests to avoid getting stuck?
the package `pytest-timeout` solves for that by providing a plugin to pytest.

1. install the package using `pip install pytest-timeout` 
2. you can set timeouts individually on tests by marking them with the `@pytest.mark.timeout(timeout=60)` decorator
3. you can set the timeout for all tests globally by using the timeout commandline parameter for pytest, like so:`pytest --timeout=300`



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
pip install -q pytest-timeout

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
%%file test_timeouts.py

import pytest

@pytest.mark.timeout(5)
def test_infinite_sleep():
    import time
    while True:
        time.sleep(1)
        print('sleeping ...') 

def test_empty():
    pass

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
Overwriting test_timeouts.py
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
!python -m pytest --verbose test_timeouts.py

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
[1mTest session starts (platform: linux, Python 3.6.9, pytest 5.3.5, pytest-sugar 0.9.2)[0m
cachedir: .pytest_cache
rootdir: /content
plugins: sugar-0.9.2, xdist-1.31.0, forked-1.1.3, timeout-1.3.4
[1mcollecting ... [0m

――――――――――――――――――――――――――――― test_infinite_sleep ――――――――――――――――――――――――――――――

[1m    @pytest.mark.timeout(5)[0m
[1m    def test_infinite_sleep():[0m
[1m        import time[0m
[1m        while True:[0m
[1m>           time.sleep(1)[0m
[1m[31mE           Failed: Timeout >5.0s[0m

[1m[31mtest_timeouts.py[0m:8: Failed
----------------------------- Captured stdout call -----------------------------
sleeping ...
sleeping ...
sleeping ...
sleeping ...

 [36mtest_timeouts.py[0m::test_infinite_sleep[0m [31m⨯[0m                          [31m50% [0m[40m[31m█[0m[40m[31m████     [0m
 [36mtest_timeouts.py[0m::test_empty[0m [32m✓[0m                                  [31m100% [0m[40m[31m█[0m[40m[31m████[0m[40m[32m█[0m[40m[32m████[0m

Results (5.03s):
[32m       1 passed[0m
[31m       1 failed[0m
         - [36m[0mtest_timeouts.py[0m:4 [31mtest_infinite_sleep[0m
```
</div>
</div>
</div>



notice how the `test_empty` test still runs and passes, even though the previous test was aborted



## your turn

1. use the `requests` module to `.get()` the url http://httpstat.us/101 and call `.raise_for_status()`
2. since this will hang forever, use a timeout on the test so that it fails after 5 seconds
3. since the test is guranteed to fail, mark it with the `xfail` (_expected fail_) annotation `@pytest.mark.xfail(reason='timeout')`





<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
%%file test_http101_timeout.py

import pytest
import requests

@pytest.mark.xfail(reason='timeout')
@pytest.mark.timeout(2)
def test_http101_timeout():
    response = requests.get('http://httpstat.us/101')
    response.raise_for_status()

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
Overwriting test_http101_timeout.py
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
!python -m pytest test_http101_timeout.py

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
[1mTest session starts (platform: linux, Python 3.6.9, pytest 5.3.5, pytest-sugar 0.9.2)[0m
rootdir: /content
plugins: sugar-0.9.2, xdist-1.31.0, forked-1.1.3, timeout-1.3.4
[1mcollecting ... [0m
 [36m[0mtest_http101_timeout.py[0m [32mx[0m                                       [32m100% [0m[40m[32m█[0m[40m[32m█████████[0m

Results (5.22s):
[32m       1 xfailed[0m
```
</div>
</div>
</div>



# testing for exceptions
[Reference](https://docs.pytest.org/en/3.0.1/assert.html#assertions-about-expected-exceptions)

consider the following code fragment from `person.py`:

```python
class Person:
    def add_friend(self, other_person):
        if not isinstance(other_person, Person) raise TypeError(other_person, 'is not a', Person)
        self.friends.add(other_person)
        other_person.friends.add(self)
```

the `add_friend()` method will raise an exception if it is used with a parameter which is not a `Person`

how can we test this?

if we wrap the code that is supposed to throw the exc



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
%%file test_add_person_exception.py

from person import Person
from test_person_fixtures2 import *

def test_add_person_exception(terry):
    with pytest.raises(TypeError):
        terry.add_friend("a shrubbey!")

def test_add_person_exception_detailed(terry):
    with pytest.raises(TypeError) as excinfo:
        terry.add_friend("a shrubbey!")
    
    assert 'Person' in str(excinfo.value)

@pytest.mark.xfail(reason='expected to fail')
def test_add_person_no_exception(terry, eric):
    with pytest.raises(TypeError): # is expecting an exception that won't happen
        terry.add_friend(eric) # this does not throw an exception


```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
Overwriting test_add_person_exception.py
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
!python -m pytest test_add_person_exception.py

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
[1mTest session starts (platform: linux, Python 3.6.9, pytest 5.3.5, pytest-sugar 0.9.2)[0m
rootdir: /content
plugins: sugar-0.9.2, xdist-1.31.0, forked-1.1.3, timeout-1.3.4
[1mcollecting ... [0m
 [36m[0mtest_add_person_exception.py[0m [32m✓[0m[32m✓[0m[32mx[0m[32m✓[0m                               [32m100% [0m[40m[32m█[0m[40m[32m█[0m[40m[32m█[0m[40m[32m██[0m[40m[32m█[0m[40m[32m█[0m[40m[32m█[0m[40m[32m██[0m

Results (0.04s):
[32m       3 passed[0m
[32m       1 xfailed[0m
```
</div>
</div>
</div>



## your turn
use the `requests` module and the `.raise_for_status()` method

1. test that `.raise_for_status` will raise an exception when accessing the following URLs:
   - http://httpstat.us/401
   - http://httpstat.us/404
   - http://httpstat.us/500
   - http://httpstat.us/501
2. test that `.raise_for_status` will NOT raise an exception when accessing the following URLs:
   - http://httpstat.us/200
   - http://httpstat.us/201
   - http://httpstat.us/202
   - http://httpstat.us/203
   - http://httpstat.us/204
   - http://httpstat.us/303
   - http://httpstat.us/304  

### hints:
1. the `requests` module raises exceptions of type `requests.HTTPError`
1. use parameterized fixtures to avoid writing a lot of tests or boilerplate code
2. use timeouts to avoid tests that wait forever





## solution



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
%%file test_requests.py

import pytest
import requests

@pytest.fixture(params=[200, 201, 202, 203, 204, 303, 304])
def good_url(request):
    return f'http://httpstat.us/{request.param}'

@pytest.fixture(params=[401, 404, 500, 501])
def bad_url(request):
    return f'http://httpstat.us/{request.param}'

@pytest.mark.timeout(2)
def test_good_urls(good_url):
    response = requests.get(good_url)
    response.raise_for_status()

@pytest.mark.timeout(2)
def test_bad_urls(bad_url):
    response = requests.get(bad_url)
    with pytest.raises(requests.HTTPError):
        response.raise_for_status()

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
Overwriting test_requests.py
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
pip install pytest-sugar

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
Collecting pytest-sugar
  Downloading https://files.pythonhosted.org/packages/da/3b/f1e3c8830860c1df8f0e0f6713932475141210cfa021e362ca2774d2bf02/pytest_sugar-0.9.2-py2.py3-none-any.whl
Requirement already satisfied: packaging>=14.1 in /usr/local/lib/python3.6/dist-packages (from pytest-sugar) (20.1)
Requirement already satisfied: termcolor>=1.1.0 in /usr/local/lib/python3.6/dist-packages (from pytest-sugar) (1.1.0)
Requirement already satisfied: pytest>=2.9 in /usr/local/lib/python3.6/dist-packages (from pytest-sugar) (5.3.5)
Requirement already satisfied: pyparsing>=2.0.2 in /usr/local/lib/python3.6/dist-packages (from packaging>=14.1->pytest-sugar) (2.4.6)
Requirement already satisfied: six in /usr/local/lib/python3.6/dist-packages (from packaging>=14.1->pytest-sugar) (1.12.0)
Requirement already satisfied: more-itertools>=4.0.0 in /usr/local/lib/python3.6/dist-packages (from pytest>=2.9->pytest-sugar) (8.2.0)
Requirement already satisfied: pluggy<1.0,>=0.12 in /usr/local/lib/python3.6/dist-packages (from pytest>=2.9->pytest-sugar) (0.13.1)
Requirement already satisfied: wcwidth in /usr/local/lib/python3.6/dist-packages (from pytest>=2.9->pytest-sugar) (0.1.8)
Requirement already satisfied: attrs>=17.4.0 in /usr/local/lib/python3.6/dist-packages (from pytest>=2.9->pytest-sugar) (19.3.0)
Requirement already satisfied: py>=1.5.0 in /usr/local/lib/python3.6/dist-packages (from pytest>=2.9->pytest-sugar) (1.8.1)
Requirement already satisfied: importlib-metadata>=0.12; python_version < "3.8" in /usr/local/lib/python3.6/dist-packages (from pytest>=2.9->pytest-sugar) (1.5.0)
Requirement already satisfied: zipp>=0.5 in /usr/local/lib/python3.6/dist-packages (from importlib-metadata>=0.12; python_version < "3.8"->pytest>=2.9->pytest-sugar) (2.2.0)
Installing collected packages: pytest-sugar
Successfully installed pytest-sugar-0.9.2
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
!python -m pytest --verbose test_requests.py

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
[1mTest session starts (platform: linux, Python 3.6.9, pytest 5.3.5, pytest-sugar 0.9.2)[0m
cachedir: .pytest_cache
rootdir: /content
plugins: sugar-0.9.2, xdist-1.31.0, forked-1.1.3, timeout-1.3.4
[1mcollecting ... [0m
 [36mtest_requests.py[0m::test_good_urls[200][0m [32m✓[0m                           [32m9% [0m[40m[32m▉[0m[40m[32m         [0m
 [36mtest_requests.py[0m::test_good_urls[201][0m [32m✓[0m                          [32m18% [0m[40m[32m█[0m[40m[32m▊        [0m
 [36mtest_requests.py[0m::test_good_urls[202][0m [32m✓[0m                          [32m27% [0m[40m[32m█[0m[40m[32m█[0m[40m[32m▊       [0m
 [36mtest_requests.py[0m::test_good_urls[203][0m [32m✓[0m                          [32m36% [0m[40m[32m█[0m[40m[32m█[0m[40m[32m█[0m[40m[32m▋      [0m
 [36mtest_requests.py[0m::test_good_urls[204][0m [32m✓[0m                          [32m45% [0m[40m[32m█[0m[40m[32m█[0m[40m[32m█[0m[40m[32m█[0m[40m[32m▋     [0m
 [36mtest_requests.py[0m::test_good_urls[303][0m [32m✓[0m                          [32m55% [0m[40m[32m█[0m[40m[32m█[0m[40m[32m█[0m[40m[32m█[0m[40m[32m█[0m[40m[32m▌    [0m
 [36mtest_requests.py[0m::test_good_urls[304][0m [32m✓[0m                          [32m64% [0m[40m[32m█[0m[40m[32m█[0m[40m[32m█[0m[40m[32m█[0m[40m[32m█[0m[40m[32m█[0m[40m[32m▍   [0m
 [36mtest_requests.py[0m::test_bad_urls[401][0m [32m✓[0m                           [32m73% [0m[40m[32m█[0m[40m[32m█[0m[40m[32m█[0m[40m[32m█[0m[40m[32m█[0m[40m[32m█[0m[40m[32m█[0m[40m[32m▍  [0m
 [36mtest_requests.py[0m::test_bad_urls[404][0m [32m✓[0m                           [32m82% [0m[40m[32m█[0m[40m[32m█[0m[40m[32m█[0m[40m[32m█[0m[40m[32m█[0m[40m[32m█[0m[40m[32m█[0m[40m[32m█[0m[40m[32m▎ [0m
 [36mtest_requests.py[0m::test_bad_urls[500][0m [32m✓[0m                           [32m91% [0m[40m[32m█[0m[40m[32m█[0m[40m[32m█[0m[40m[32m█[0m[40m[32m█[0m[40m[32m█[0m[40m[32m█[0m[40m[32m█[0m[40m[32m█[0m[40m[32m▏[0m
 [36mtest_requests.py[0m::test_bad_urls[501][0m [32m✓[0m                          [32m100% [0m[40m[32m█[0m[40m[32m█[0m[40m[32m█[0m[40m[32m█[0m[40m[32m█[0m[40m[32m█[0m[40m[32m█[0m[40m[32m█[0m[40m[32m█[0m[40m[32m█[0m

Results (2.12s):
[32m      11 passed[0m
```
</div>
</div>
</div>



# running tests in parallel

[Reference](https://pypi.org/project/pytest-xdist/)

The `pytest-xdist` plugin extends pytest with some unique test execution modes:

- **test run parallelization**: if you have multiple CPUs or hosts you can use those for a combined test run. This allows to speed up development or to use special resources of remote machines.
- **--looponfail**: run your tests repeatedly in a subprocess. After each run pytest waits until a file in your project changes and then re-runs the previously failing tests. This is repeated until all tests pass after which again a full run is performed.
- **Multi-Platform coverage**: you can specify different Python interpreters or different platforms and run tests in parallel on all of them.
- **--boxed** and **pytest-forked**: running each test in its own process, so that if a test catastrophically crashes, it doesn't interfere with other tests

We're going to cover only test run parallelization.




first, lets install `pytest-xdist`:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
pip install -qq pytest-xdist

```
</div>

</div>



now, lets write a few long running tests



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
%%file test_parallel.py

import time
def test_t1():
    time.sleep(2)

def test_t2():
    time.sleep(2)

def test_t3():
    time.sleep(2)

def test_t4():
    time.sleep(2)

def test_t5():
    time.sleep(2)

def test_t6():
    time.sleep(2)

def test_t7():
    time.sleep(2)

def test_t8():
    time.sleep(2)

def test_t9():
    time.sleep(2)

def test_t10():
    time.sleep(2)


```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
Writing test_parallel.py
```
</div>
</div>
</div>



now, we can run these tests in parallel using the `pytest -n NUM` commandline parameter.

Lets use 10 threads, this will allow us to finish in 2 seconds rather than 20



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
!python -m pytest -n 10 test_parallel.py

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
[1m============================= test session starts ==============================[0m
platform linux -- Python 3.6.9, pytest-5.3.5, py-1.8.1, pluggy-0.13.1
rootdir: /content
plugins: xdist-1.31.0, forked-1.1.3, timeout-1.3.4
gw0 [10] / gw1 [10] / gw2 [10] / gw3 [10] / gw4 [10] / gw5 [10] / gw6 [10] / gw7 [10] / gw8 [10] / gw9 [10][0m
[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m                                                               [100%][0m
[32m============================== [32m[1m10 passed[0m[32m in 5.94s[0m[32m ==============================[0m
```
</div>
</div>
</div>



# Codebase to test: class Person

Lets reuse the `Person` and `OlympicRunner` classes we've defined in earlier chapters in order to see how to write tests




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
%%file person.py

# Person v1
class Person:
    def __init__(self, name):
        name = name
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

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
Overwriting person.py
```
</div>
</div>
</div>



# our first test

- [conventions](https://docs.pytest.org/en/latest/goodpractices.html#conventions-for-python-test-discovery) 
  1. files with tests should be called `test_*.py` or `*_test.py `
  2. test function name should start with `test_`

- to see if our code works, we can use the `assert` python keyword. pytest adds hooks to assertions to make them more useful



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
%%file test_person1.py
from person import Person

# our first test
def test_preson_name():
    terry = Person('Terry Gilliam')
    assert terry.name == 'Terry Gilliam'

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
Overwriting test_person1.py
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
!python -m pytest

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
[1m============================= test session starts ==============================[0m
platform linux -- Python 3.6.9, pytest-3.6.4, py-1.8.1, pluggy-0.7.1
rootdir: /content, inifile:
collected 1 item                                                               [0m

test_person1.py F[36m                                                        [100%][0m

=================================== FAILURES ===================================
[31m[1m_______________________________ test_preson_name _______________________________[0m

[1m    def test_preson_name():[0m
[1m        terry = Person('Terry Gilliam')[0m
[1m>       assert terry.name == 'Terry Gilliam'[0m
[1m[31mE       AttributeError: 'Person' object has no attribute 'name'[0m

[1m[31mtest_person1.py[0m:6: AttributeError
[31m[1m=========================== 1 failed in 0.03 seconds ===========================[0m
```
</div>
</div>
</div>



## lets run our tests




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

```
</div>
</div>
</div>



## running our first test




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

