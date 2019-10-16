---
redirect_from:
  - "/01-refresher/notebooks/reduce"
interact_link: content/01_refresher/notebooks/reduce.ipynb
kernel_name: python3
has_widgets: false
title: 'Reduce'
prev_page:
  url: /01_refresher/notebooks/generic_functions_closures.html
  title: 'Generic Functions Closures'
next_page:
  url: /01_refresher/notebooks/refresher.html
  title: 'Refresher'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-advanced-python/blob/master/content/01_refresher/notebooks/reduce.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
import functools

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
mysum = functools.partial(functools.reduce, lambda x, y: x+y)
mysum([1,2,3,2,1])

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
9
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
mymax = functools.partial(functools.reduce, lambda x, y: x if x>=y else y)
mymax([1,2,3,2,1])

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
3
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
myaverage = lambda list_ : mysum(list_) / len(list_)
myaverage([1,2,3])

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
2.0
```


</div>
</div>
</div>

