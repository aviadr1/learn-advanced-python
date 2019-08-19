---
redirect_from:
  - "/10-package-management/exercise/solutions"
interact_link: content/10_package_management/exercise/solutions.ipynb
kernel_name: python3
has_widgets: false
title: 'Solutions'
prev_page:
  url: /10_package_management/exercise/questions.html
  title: 'Questions'
next_page:
  url: /11_db_access/01_basic_db_access.html
  title: '11 db access'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-advanced-python/blob/master/content/10_package_management/exercise/solutions.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




# using new modules without polluting your system

in this exercize we're going to use `pipenv` to try out some new modules without polluting your environment



## start a new project called cute-python

make a new folder called cute-python



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# useful: current directory
import os
os.path.realpath('.')

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'E:\\dev\\GitHub\\learn-advanced-python\\notebooks'
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
if not os.path.exists('cute-python'):
    os.mkdir('cute-python')
os.chdir('cute-python')
os.path.realpath('.')

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'E:\\dev\\GitHub\\learn-advanced-python\\notebooks\\cute-python'
```


</div>
</div>
</div>



## function that downloads image from web

> remember to use `pipenv` for this step

we want to download a particular image from the web: <br>
```https://inews.co.uk/wp-content/uploads/2018/03/Nobody-expects-the-Spanish-Inquisition_.jpg```

why not use an awesome library to perform our HTTP download for us?
lets see if this library is indeed so awesome without affecting our whole system.

1. use `pipenv` to install the `requests` library for the `cute-python` project
2. use the [requests](https://2.python-requests.org/en/master/) library to write a function that downloads the image file mentioned above to a file called `cute-python.jpg`
   > hint: you're looking for the `requests.get()` function, <br>
   > you need to write the _content_ to a binary file opened like this `open('cute-python.jpg', "wb")`



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# run this in the shell:
"""
>> pipenv install requests
"""

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'\npipenv install requests\n'
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
code = """
import requests
def download():
    url = 'https://inews.co.uk/wp-content/uploads/2018/03/Nobody-expects-the-Spanish-Inquisition_.jpg'
    with open('cute-python.jpg', 'wb') as file:
        r = requests.get(url, allow_redirects=True)
        file.write(r.content)

if __name__ == '__main__':
    download()
"""
with open('download.py', 'w') as codefile:
    codefile.write(code)


```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# run this in the shell
"""
>> pipenv shell
(cute-python) >> python download.py
"""

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'\n>> pipenv shell\n(cute-python) >> python download.py\n'
```


</div>
</div>
</div>



# lets also show the file
here's some code based on `matplotlib` and `pillow` modules that can show the image
```
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
plt.imshow(mpimg.imread('cute-python.jpg'))
plt.show()
```

1. lets use pipenv to get these two modules for our project
2. lets add this code to a file called `show.py` and run it




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# run this in the shell
"""
>> pipenv install pillow matplotlib
"""

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
code = """
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
plt.imshow(mpimg.imread('cute-python.jpg'))
plt.show()
"""
with open('show.py', 'w') as codefile:
    codefile.write(code)

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# run this in the shell
"""
>> pipenv run python show.py
"""

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'\n>> pipenv run python show.py\n'
```


</div>
</div>
</div>



# what are our project's dependencies?

1. what libraries we actuall care about did we install
2. what sub-dependencies were installed in addition?



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
!pipenv graph

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
matplotlib==3.1.1
  - cycler [required: >=0.10, installed: 0.10.0]
    - six [required: Any, installed: 1.12.0]
  - kiwisolver [required: >=1.0.1, installed: 1.1.0]
    - setuptools [required: Any, installed: 41.0.1]
  - numpy [required: >=1.11, installed: 1.16.4]
  - pyparsing [required: >=2.0.1,!=2.1.6,!=2.1.2,!=2.0.4, installed: 2.4.0]
  - python-dateutil [required: >=2.1, installed: 2.8.0]
    - six [required: >=1.5, installed: 1.12.0]
Pillow==6.1.0
requests==2.22.0
  - certifi [required: >=2017.4.17, installed: 2019.6.16]
  - chardet [required: >=3.0.2,<3.1.0, installed: 3.0.4]
  - idna [required: >=2.5,<2.9, installed: 2.8]
  - urllib3 [required: >=1.21.1,<1.26,!=1.25.1,!=1.25.0, installed: 1.25.3]
```
</div>
</div>
</div>

