---
redirect_from:
  - "/15-logging/exercise/questions"
interact_link: content/15_logging/exercise/questions.ipynb
kernel_name: python3
has_widgets: false
title: 'Questions'
prev_page:
  url: /15_logging/exercise/questions.html
  title: 'exercise'
next_page:
  url: /15_logging/exercise/solutions.html
  title: 'Solutions'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-advanced-python/blob/master/content/15_logging/exercise/questions.ipynb" target="_blank">
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
### useful: run your ex2.py
import ex2
ex2.say_something()

log_to_debug = ex2.logger
while log_to_debug is not None:
    print("level: %s, name: %s (%x), handlers: %s" % (
        log_to_debug.level,
        log_to_debug.name,
        id(log_to_debug),
        log_to_debug.handlers))
    
    log_to_debug = log_to_debug.parent

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
level: 10, name: ex2 (62fbb30), handlers: []
level: 30, name: root (3a787b0), handlers: [<StreamHandler stderr (NOTSET)>]
```
</div>
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






# Format #1

Copy the YAML configuration from the previous question, and change the formatter so that output from calling `ex1.say_something()` will look like this
`2019-12-26 03:07:04,560 | WARNING | ex1 | this is a warning message`


hints:
- Read the [LogRecord](https://docs.python.org/3/library/logging.html#logrecord-attributes) documentaion, which shows the attributes available for formatting




# Format #2
Copy the YAML configuration from the previous question, and change the formatter so that output from calling `ex1.say_something()` will look like this: 

`2019-12-26 03:10:19,852 :: WARNING :: Module ex1 :: Line No 6 :: this is a warning message`



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


