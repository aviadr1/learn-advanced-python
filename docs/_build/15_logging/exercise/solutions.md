---
redirect_from:
  - "/15-logging/exercise/solutions"
interact_link: content/15_logging/exercise/solutions.ipynb
kernel_name: python3
has_widgets: false
title: 'Solutions'
prev_page:
  url: /15_logging/exercise/questions.html
  title: 'Questions'
next_page:
  url: 
  title: ''
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-advanced-python/blob/master/content/15_logging/exercise/solutions.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




# setup
1. import the logging module
2. call `.basicConfig()`
3. setup autoreload to help reloading .py files from disk



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
### useful: please run this
import logging
logging.basicConfig()

%load_ext autoreload
%autoreload 2

```
</div>

</div>



# Basic
1. import 
1. Create a new python file named `ex1.py` which should:
    1. Import the logging module
    2. create a logger instance named `__name__`
    3. Create a function called `say_something()` that logs a ‘warning’ message with the text: `"This a warning message!"`.
2. use the file
   1. `import ex1`
   2. call `ex1.say_something()`





<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
%%file ex1.py

import logging
logger = logging.getLogger(__name__)

def say_something():
    logger.warning('this is a warning message')

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
Overwriting ex1.py
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
### useful: run your ex1.py
import ex1
ex1.say_something()

```
</div>

</div>



# Log level

1. Create a new python file named ‘ex2.py‘ which should:
    1. Import the logging module
    2. create a logger instance named `__name__`
    2. set the logger's level to `logging.DEBUG`
    3. create a function called `say_something()` which logs an ‘info’ message with the text: “This an informative message!”.
2. use this file
   1. import ex2
   1. call `ex2.say_something()`



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
%%file ex2.py

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def say_something():
    logger.info('this is an informative message')

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
Overwriting ex2.py
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
### useful: run your ex2.py
import ex2
ex2.say_something()

```
</div>

</div>



# Configuration
1. setup
   1. change the level of ex2's logger to DEBUG
   2. call `ex2.say_something()` - this should write the usual output 
   <br><br>
   
1. Review this basic YAML configuration, and see that you understand how it will:
   1. set a simple format that is the same as the default format
   2. set a handler that logs to console
   3. connect the root logger to the console handler, with level WARNING
   4. modify the level for the ex2 logger to ERROR
      ```
      version: 1
      disable_existing_loggers: False
      formatters:
        simple:
          format: '%(levelname)s:%(name)s:%(message)s'
      handlers:
        console:
          class: logging.StreamHandler
          formatter: simple
          stream: ext://sys.stderr
      loggers:
        ex2:
          level: ERROR
      root:
        level: WARNING
        handlers: [console]
      ``` 
      <br><br>
2. load this configuration
   1. import the `yaml` module
   2. use `yaml.load()` to read this configuration into a `dict` object
   3. import logging.config module
   4. use `logging.config.dictConfig()` function to load the configuration from your dict <br>
   <br><br>
   
3. execute `ex2.say_something()` again. this time there should not be any output. 
   why?






<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
import yaml
import logging.config

ex2.logger.setLevel(logging.DEBUG)
ex2.say_something()

config_string = """
version: 1
disable_existing_loggers: False
formatters:
  simple:
    format: '%(levelname)s:%(name)s:%(message)s'
handlers:
  console:
    class: logging.StreamHandler
    formatter: simple
    stream: ext://sys.stderr
loggers:
  ex2:
    level: ERROR
root:
  level: INFO
  handlers: [console]
"""

config_dict = yaml.safe_load(config_string)
logging.config.dictConfig(config_dict)

# now the log level is set to ERROR 
# so there should be no output from this logger
ex2.say_something() 


```
</div>

</div>



# Format #1

Copy the YAML configuration from the previous question, and change the formatter so that output from calling `ex1.say_something()` will look like this
`2019-12-26 03:07:04,560 | WARNING | ex1 | this is a warning message`


hints:
- Read the [LogRecord](https://docs.python.org/3/library/logging.html#logrecord-attributes) documentaion, which shows the attributes available for formatting




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
config_string = """
version: 1
disable_existing_loggers: False
formatters:
  simple:
    format: '%(asctime)s | %(levelname)s | %(name)s | %(message)s'
handlers:
  console:
    class: logging.StreamHandler
    formatter: simple
    stream: ext://sys.stderr
root:
  handlers: [console]
"""

config_dict = yaml.safe_load(config_string)
logging.config.dictConfig(config_dict)

ex1.say_something()

```
</div>

</div>



# Format #2
Copy the YAML configuration from the previous question, and change the formatter so that output from calling `ex1.say_something()` will look like this: 

`2019-12-26 03:10:19,852 :: WARNING :: Module ex1 :: Line No 6 :: this is a warning message`



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
config_string = """
version: 1
disable_existing_loggers: False
formatters:
  simple:
    format: '%(asctime)s :: %(levelname)s :: Module %(module)s :: Line No %(lineno)s :: %(message)s'
handlers:
  console:
    class: logging.StreamHandler
    formatter: simple
    stream: ext://sys.stderr
root:
  handlers: [console]
"""

config_dict = yaml.safe_load(config_string)
logging.config.dictConfig(config_dict)

ex1.say_something()

```
</div>

</div>



# file handler

- Use YAML configuration to
  1. set the levels of both `ex1` and `ex2` loggers to DEBUG
  2. setup file logging for `ex2` logger so that it writes to `ex2.log`
  
- test this by calling 
  ```python
  ex1.say_something()
  ex2.say_something()
  ```
  and reading `ex2.log`




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
from pathlib import Path

config_string = """
version: 1
disable_existing_loggers: False
formatters:
  simple:
    format: '%(asctime)s :: %(levelname)s :: Module %(module)s :: Line No %(lineno)s :: %(message)s'
handlers:
  console:
    class: logging.StreamHandler
    formatter: simple
    stream: ext://sys.stderr
  ex2:
    class: logging.FileHandler
    formatter: simple
    filename: ex2.log
    mode: 'w'
loggers:
  ex2:
    handlers: [ex2]
    level: DEBUG
  ex1:
    level: DEBUG
root:
  handlers: [console]
"""

config_dict = yaml.safe_load(config_string)
logging.config.dictConfig(config_dict)

ex1.say_something()
ex2.say_something()

print('ex2.log:', Path('ex2.log').read_text())

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
ex2.log: 2019-12-26 03:21:42,824 :: INFO :: Module ex2 :: Line No 8 :: this is an informative message

```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
!dir

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
 Volume in drive E is New Volume
 Volume Serial Number is 5C7B-188A

 Directory of E:\dev\GitHub\learn-advanced-python\content\15_logging\exercise

26-Dec-19  03:18 AM    <DIR>          .
26-Dec-19  03:18 AM    <DIR>          ..
26-Dec-19  01:00 AM    <DIR>          .ipynb_checkpoints
26-Dec-19  03:06 AM               129 ex1.py
26-Dec-19  03:18 AM                 0 ex2.log
26-Dec-19  03:06 AM               165 ex2.py
26-Dec-19  01:14 AM               124 example.py
26-Dec-19  03:18 AM            30,516 solutions.ipynb
26-Dec-19  03:06 AM    <DIR>          __pycache__
               5 File(s)         30,934 bytes
               4 Dir(s)  3,086,822,178,816 bytes free
```
</div>
</div>
</div>

