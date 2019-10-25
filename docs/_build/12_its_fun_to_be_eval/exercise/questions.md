---
redirect_from:
  - "/12-its-fun-to-be-eval/exercise/questions"
interact_link: content/12_its_fun_to_be_eval/exercise/questions.ipynb
kernel_name: python3
has_widgets: false
title: 'Questions'
prev_page:
  url: /12_its_fun_to_be_eval/exercise/questions.html
  title: 'exercise'
next_page:
  url: /12_its_fun_to_be_eval/exercise/solutions.html
  title: 'Solutions'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-advanced-python/blob/master/content/12_its_fun_to_be_eval/exercise/questions.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




# 1. doctest

do you remember the module `doctest` which allows writing tests inside a functions doc comment?

take a look at the code below, isnt this quite magical?

### your exercise
the exercise is to write a function called `func_test` that gets a function as a parameter and tests it using the tests in the functions docstreing
```
def func_test(func):
```

1. func_test should use the `func.__doc__` to get the docstring of the function to test
2. lines with '>>>' are what needs to be evaluated (hint: use `eval` for a MUCH simpler solution)
3. lines afer '>>>' that don't start with '>>>' are the expected result
4. `func_test` should return a dictionary with the number of failed tests, and number of tests ran
5. try to mimic the output of the `doctest` module
6. there's a simple code to test your `func_test` below



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
### useful example of doctest usage
def my_func(x, y, z):
    """
    >>> my_func(1, 2, 3)
    5
    >>> my_func('hello ', 3, 'world')
    hello hello hello world
    >>> my_func(0, 0, 0)
    what happens when things are wrong?
    """
    return x * y + z

import doctest
doctest.testmod()

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
**********************************************************************
File "__main__", line 6, in __main__.my_func
Failed example:
    my_func('hello ', 3, 'world')
Expected:
    hello hello hello world
Got:
    'hello hello hello world'
**********************************************************************
File "__main__", line 8, in __main__.my_func
Failed example:
    my_func(0, 0, 0)
Expected:
    what happens when things are wrong?
Got:
    0
**********************************************************************
1 items had failures:
   2 of   3 in __main__.my_func
***Test Failed*** 2 failures.
```
</div>
</div>
<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
TestResults(failed=2, attempted=3)
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
### useful: test your 'func_test' function
result = func_test(my_func)
assert result['failed'] == 1
assert result['attempted'] == 3


```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
**********************************************************************
Failed example:
	  my_func(0, 0, 0)
Expected:
	 what happens when things are wrong?
Got:
	 0
**********************************************************************
```
</div>
</div>
</div>



# 2. Game of life

python has been used by a lot of game engines as a way to 'script' the engine.
in this example, we have written an incredibly simple game called 'Conway's game of life' [1].
> fun fact: this game is is Turing complete. which means that anything that could be calculated, can be calculated using this game. In fact, several different programmable computer architectures have been implemented in Conway's Life, including a pattern that simulates Tetris.

![Animation](https://upload.wikimedia.org/wikipedia/commons/e/e5/Gospers_glider_gun.gif)

The game consists of an infinite 2d board on which cells live or die.

The rules of the game are simple:
1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
2. Any live cell with two or three live neighbours lives on to the next generation.
3. Any live cell with more than three live neighbours dies, as if by overpopulation.
4. Any dead cell with three live neighbours becomes a live cell, as if by reproduction.

the file `game-of-life.py` contains a full implementation of the game. go ahead and run it now
```
>> python game-of-life.py
```

## Your task

1. add a custom rule engine to the game

    to do this you have to edit the file `game-of-life.py` you find in this directory
    and implement two methods that are currently unimplemented:

    1. implement the `read_custom_rules()` function
    2. implement the `apply_custom_rules()` function <br><br>

2. look at the `apply_default_rules()` function, and implement the default rules of the game as two rule files `rule-1.txt` and `rule-2.txt` <br><br>

3. invent new rules or modify the a rules by adding more `rule-xyz.txt` files and without changing the `game-of-life.py` file

> __HINTS__: 
> 1. both of the functions you need to implement have a handy `TODO` comment to help you with your task
> 2. apart from implementing these functions, no other code needs to be modified
> 3. here's how rule #1 and rule #3 can be implemented together as a custom rule in a file called `rule-1.txt`
     ```
     if grid[i, j]  == ON:
        if (total_neighbours < 2) or (total_neighbours > 3):
            result = OFF
     ```
> 4. a solution can be found in `game-of-life.solution.py`


The bundled game of life code is based on this awesome implementation [2]


[1]: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
[2]: https://electronut.in/simple-python-matplotlib-implementation-of-conways-game-of-life/


