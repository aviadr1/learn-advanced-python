---
redirect_from:
  - "/12-its-fun-to-be-eval/its-fun-to-be-eval"
interact_link: content/12_its_fun_to_be_eval/its_fun_to_be_eval.ipynb
kernel_name: python3
has_widgets: false
title: '12 its fun to be eval'
prev_page:
  url: /11_db_access/exercise/sqlalchemy_orm-solutions.html
  title: 'Sqlalchemy Orm-solutions'
next_page:
  url: /12_its_fun_to_be_eval/its_fun_to_be_eval.html
  title: 'Its Fun To Be Eval'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-advanced-python/blob/master/content/12_its_fun_to_be_eval/its_fun_to_be_eval.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




# Its fun to be eval

it is said about python that
> python gives you enough rope to shoot yourself in both feet

one of the awesomest tools (but also a HUGE potential security issue) is the ability to dynamically run any code.
we can do this using the _unholy trinity_:
1. `eval`
2. `exec`
3. `compile` 

we will take a look at some fun things we can do with `eval`



## eval
> ```
> eval(source, globals=None, locals=None, /)
> ```

the `eval` function (pronounced like EVIL) allows us to evaluate a string as a single __expression__

An expression in Python is whatever you can have as the value in a variable assignment:
```
a_variable = (anything you can put within these parentheses is an expression)
```

eval __returns__ the value of the given expression





<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
a=1
b=2
c=3
x=10
result = eval("a*x**2 + b*x + c")
print(result)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
123
```
</div>
</div>
</div>



### Example: parse JSON using eval
a JSON object is basically a javascript expression.
as it happens, javascript/JSON syntax is very similar (but not identical [1] ) to python syntax. <br>
many JSON strings can easily be parsed using `eval`

[1]: https://docs.python.org/3/library/json.html#encoders-and-decoders



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
json_str = """
{
    "firstName": "Jane",
    "lastName": "Doe",
    "hobbies": ["running", "sky diving", "singing"],
    "age": 35,
    "children": [
        {
            "firstName": "Alice",
            "age": 6
        },
        {
            "firstName": "Bob",
            "age": 8
        }
    ]
}
"""

json_obj = eval(json_str)
print(type(json_obj), json_obj.keys())

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
<class 'dict'> dict_keys(['firstName', 'lastName', 'hobbies', 'age', 'children'])
```
</div>
</div>
</div>



## exec
> ```
> exec(source, globals=None, locals=None, /)
> ```

The `exec` function allows us to evaluate a string as a statement or series of statements

two famous modules that use exec:

1. namedtuples
2. doctest

Note: exec __ignores the return value__ from its code, and always returns `None`




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
code = """
x=10
y=20
z=x+y
print(x, '+', y, '=', z)
"""

exec(code)


```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
10 + 20 = 30
```
</div>
</div>
</div>



### controlling the environment

Both `exec` and `eval` accept 2 additional positional arguments - `globals` and `locals` - 
which are the global and local variable scopes that the code sees. 
These default to the globals() and locals() within the scope that called exec or eval, 
but any dictionary can be used for globals and any mapping for locals (including dict of course). 
These can be used not only to restrict/modify the variables that the code sees, but are often also used 
for capturing the variables that the executed code creates

> NOTE: exec and eval add the built-ins module as `__builtins__` to the globals automatically if it is missing.



### Example: rule engine

lets imagine we have some rule-based product, such as a firewall.

furthermore:
1. we would like to be able to add, modify and delete rules of this product, by changing the configuration of the product, but without changing the source code of the product itself
2. we would like to be able to write very complex rules, that may needs complicated logic or even loops

to solve for such requirements, we can ask users to write these rules as strings in configuration files, expressed in python langauge. <br>
and to load and `exec`-ute these strings at runtime from the host product



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# rule we read from file
rule = """
if x>100:
    result = 100
elif y<0:
    result = 0
else:
    result = (x+y) / 2 
"""

# create an environment for our rule to run in
globals_ = {}
locals_ = {'x' : 75, 'y': 25}

# run the rule
exec(rule, globals_, locals_)

# get the result
result = locals_['result']
print(result)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
50.0
```
</div>
</div>
</div>



In the example above we used a __convention__ that the rule should output the result of its calculation into the `result` variable. this is a very simple and effective method of extracting the results from an exec.

> it is possible (but requires much more work) to create an rule processing engine that does not require such conventions. one way is to look more deeply into the code we're executing, such as by using python's [ast](https://docs.python.org/3.7/library/ast.html) abstract syntax trees module



## why is exec / eval a security risk?

Consider a situation, where your server runs rules written in text files, and an attacker gets access to modify these text files The attacker could write a rule that imports the `os` module and then use it to execute arbitrary code on the operating system.

If you allow users to input a value using eval(input()), the user may issue commands to change file or even delete all the files using command os.system('rm -rf *').

If you are using eval(input()) in your code, it's a good idea to check which variables and methods the user can use. You can see which variables and methods are available using dir() method.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
security_risk_code = """
import os
os.system("echo gotcha, I have access to your OS I can delete all your files >> gotcha.txt")
os.system('notepad gotcha.txt')
"""

# exec code - you just lost control
exec(security_risk_code)

```
</div>

</div>



We can use the same attack even with the much simpler `eval` <br>
we just need the expression to itself run an `exec` code: 



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
security_risk_expression = """\
exec(\"\"\"import os
os.system("echo gotcha, I have access to your OS I can delete all your files >> gotcha.txt")
os.system('notepad gotcha.txt')
\"\"\")
"""

eval(security_risk_expression)

```
</div>

</div>



to solve this particular vulnerability, you should explicitly add an empty `__builtins__` key to the globals dictionary passed to `exec` or `eval`

> NOTE: just because we solved THIS security issue, doesn't mean that there can't be more security issues, especially as you become more leniant with what the executed code can or can't do. the only way to be 100% sure we're not exposed to tricky security issues with eval/exec is to _not use them_



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
try:
    exec(security_risk_code, {'__builtins__': {}})
except Exception as ex:
    print('prevented security issue:', ex)
    
try:
    eval(security_risk_expression, {'__builtins__': {}})
except Exception as ex:
    print('prevented security issue:', ex)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
prevented security issue: __import__ not found
prevented security issue: name 'exec' is not defined
```
</div>
</div>
</div>



## Further reading

1. Difference between eval, exec and compile [1]
2. How to get results out of eval [2]
3. How to safely use eval in python [3]
4. Use of exec in python [4]

[1]: https://stackoverflow.com/questions/2220699/whats-the-difference-between-eval-exec-and-compile
[2]: https://stackoverflow.com/questions/37237034/how-to-get-results-out-of-a-python-exec-eval-call
[3]: https://stackoverflow.com/questions/9672791/how-to-safely-use-exec-in-python
[4]: https://stackoverflow.com/questions/4158117/use-of-exec-and-eval-in-python



