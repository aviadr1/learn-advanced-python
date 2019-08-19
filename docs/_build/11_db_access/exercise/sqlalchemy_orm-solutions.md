---
redirect_from:
  - "/11-db-access/exercise/sqlalchemy-orm-solutions"
interact_link: content/11_db_access/exercise/sqlalchemy_orm-solutions.ipynb
kernel_name: python3
has_widgets: false
title: 'Sqlalchemy Orm-solutions'
prev_page:
  url: /11_db_access/exercise/sqlalchemy_orm-questions.html
  title: 'Sqlalchemy Orm-questions'
next_page:
  url: /12_its_fun_to_be_eval/its_fun_to_be_eval.html
  title: '12 its fun to be eval'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-advanced-python/blob/master/content/11_db_access/exercise/sqlalchemy_orm-solutions.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




# Chinook sample database using SQLAlchemy

in this exercise we're going to experiment with the [Chinook sample DB](http://www.sqlitetutorial.net/sqlite-sample-database/). while using SQLAlchemy module

![Chinook](http://www.sqlitetutorial.net/wp-content/uploads/2015/11/sqlite-sample-database-color.jpg)

First, run the code below to download the database locally



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
### useful: download and extract chinook sample DB
import urllib.request
import zipfile
from functools import partial
import os

chinook_url = 'http://www.sqlitetutorial.net/wp-content/uploads/2018/03/chinook.zip'
if not os.path.exists('chinook.zip'):
    print('downloading chinook.zip ', end='')
    with urllib.request.urlopen(chinook_url) as response:
        with open('chinook.zip', 'wb') as f:
            for data in iter(partial(response.read, 4*1024), b''):
                print('.', end='', flush=True)
                f.write(data)

zipfile.ZipFile('chinook.zip').extractall()
assert os.path.exists('chinook.db')

```
</div>

</div>



# Helper methods

the helper methods below will help 



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
### useful: functions for displaying results from sql queries using pandas
from IPython.display import display
import pandas as pd

def sql(query):
    print()
    print(query)
    print()

def get_results(query):
    global engine
    q = query.statement if isinstance(query, sqlalchemy.orm.query.Query) else query
    return pd.read_sql(q, engine)

def display_results(query):
    df = get_results(query)
    display(df)
    sql(query)

```
</div>

</div>



# 1. open the database
1. open  the database using `sqlalchemy` module interface. create an engine object in a variable named `engine`
2. call the `connect()` method to obtain a connection and place in a variable named `cur`



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
import sqlalchemy
from sqlalchemy import create_engine
engine = create_engine('sqlite:///chinook.db')
cur = engine.connect()

```
</div>

</div>



> now run the code below to to run reflecton on the database, prepare classes that map to the database and create an orm session



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
### useful: extract classes from the chinook database
metadata = sqlalchemy.MetaData()
metadata.reflect(engine)

## we need to do this once
from sqlalchemy.ext.automap import automap_base

# produce a set of mappings from this MetaData.
Base = automap_base(metadata=metadata)

# calling prepare() just sets up mapped classes and relationships.
Base.prepare()

# also prepare an orm session
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()

```
</div>

</div>



# 2. table names
print out all the table names



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
engine.table_names()

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
['albums',
 'artists',
 'customers',
 'employees',
 'genres',
 'invoice_items',
 'invoices',
 'media_types',
 'playlist_track',
 'playlists',
 'sqlite_sequence',
 'sqlite_stat1',
 'tracks']
```


</div>
</div>
</div>



# 3. Tracks
print out the first three tracks in the `tracks` table



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
from sqlalchemy import select 
tracks = Base.classes['tracks']

# using expressions
query = select([tracks]).limit(3)
display_results(query)


```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">

<div markdown="0" class="output output_html">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>TrackId</th>
      <th>Name</th>
      <th>AlbumId</th>
      <th>MediaTypeId</th>
      <th>GenreId</th>
      <th>Composer</th>
      <th>Milliseconds</th>
      <th>Bytes</th>
      <th>UnitPrice</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>For Those About To Rock (We Salute You)</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>Angus Young, Malcolm Young, Brian Johnson</td>
      <td>343719</td>
      <td>11170334</td>
      <td>0.99</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Balls to the Wall</td>
      <td>2</td>
      <td>2</td>
      <td>1</td>
      <td>None</td>
      <td>342562</td>
      <td>5510424</td>
      <td>0.99</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Fast As a Shark</td>
      <td>3</td>
      <td>2</td>
      <td>1</td>
      <td>F. Baltes, S. Kaufman, U. Dirkscneider &amp; W. Ho...</td>
      <td>230619</td>
      <td>3990994</td>
      <td>0.99</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>
</div>
<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```

SELECT tracks."TrackId", tracks."Name", tracks."AlbumId", tracks."MediaTypeId", tracks."GenreId", tracks."Composer", tracks."Milliseconds", tracks."Bytes", tracks."UnitPrice" 
FROM tracks
 LIMIT :param_1

```
</div>
</div>
<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">

<div markdown="0" class="output output_html">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>TrackId</th>
      <th>Name</th>
      <th>AlbumId</th>
      <th>MediaTypeId</th>
      <th>GenreId</th>
      <th>Composer</th>
      <th>Milliseconds</th>
      <th>Bytes</th>
      <th>UnitPrice</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>For Those About To Rock (We Salute You)</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>Angus Young, Malcolm Young, Brian Johnson</td>
      <td>343719</td>
      <td>11170334</td>
      <td>0.99</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Balls to the Wall</td>
      <td>2</td>
      <td>2</td>
      <td>1</td>
      <td>None</td>
      <td>342562</td>
      <td>5510424</td>
      <td>0.99</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Fast As a Shark</td>
      <td>3</td>
      <td>2</td>
      <td>1</td>
      <td>F. Baltes, S. Kaufman, U. Dirkscneider &amp; W. Ho...</td>
      <td>230619</td>
      <td>3990994</td>
      <td>0.99</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>
</div>
<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```

SELECT tracks."TrackId" AS "tracks_TrackId", tracks."Name" AS "tracks_Name", tracks."AlbumId" AS "tracks_AlbumId", tracks."MediaTypeId" AS "tracks_MediaTypeId", tracks."GenreId" AS "tracks_GenreId", tracks."Composer" AS "tracks_Composer", tracks."Milliseconds" AS "tracks_Milliseconds", tracks."Bytes" AS "tracks_Bytes", tracks."UnitPrice" AS "tracks_UnitPrice" 
FROM tracks
 LIMIT ? OFFSET ?

```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# using orm
results = session.query(tracks).limit(3)
display_results(results)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">

<div markdown="0" class="output output_html">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>TrackId</th>
      <th>Name</th>
      <th>AlbumId</th>
      <th>MediaTypeId</th>
      <th>GenreId</th>
      <th>Composer</th>
      <th>Milliseconds</th>
      <th>Bytes</th>
      <th>UnitPrice</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>For Those About To Rock (We Salute You)</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>Angus Young, Malcolm Young, Brian Johnson</td>
      <td>343719</td>
      <td>11170334</td>
      <td>0.99</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Balls to the Wall</td>
      <td>2</td>
      <td>2</td>
      <td>1</td>
      <td>None</td>
      <td>342562</td>
      <td>5510424</td>
      <td>0.99</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Fast As a Shark</td>
      <td>3</td>
      <td>2</td>
      <td>1</td>
      <td>F. Baltes, S. Kaufman, U. Dirkscneider &amp; W. Ho...</td>
      <td>230619</td>
      <td>3990994</td>
      <td>0.99</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>
</div>
<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```

SELECT tracks."TrackId" AS "tracks_TrackId", tracks."Name" AS "tracks_Name", tracks."AlbumId" AS "tracks_AlbumId", tracks."MediaTypeId" AS "tracks_MediaTypeId", tracks."GenreId" AS "tracks_GenreId", tracks."Composer" AS "tracks_Composer", tracks."Milliseconds" AS "tracks_Milliseconds", tracks."Bytes" AS "tracks_Bytes", tracks."UnitPrice" AS "tracks_UnitPrice" 
FROM tracks
 LIMIT ? OFFSET ?

```
</div>
</div>
</div>



# 4. Albums from Tracks
print out the track name and albums title of the first 20 tracks in the `tracks` table





<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
from sqlalchemy import join
albums = Base.classes['albums']

# using expression language
query = select([tracks.Name, albums]).select_from(join(tracks, albums)).limit(20)
display_results(query)


```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">

<div markdown="0" class="output output_html">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>AlbumId</th>
      <th>Title</th>
      <th>ArtistId</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>For Those About To Rock (We Salute You)</td>
      <td>1</td>
      <td>For Those About To Rock We Salute You</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Put The Finger On You</td>
      <td>1</td>
      <td>For Those About To Rock We Salute You</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Let's Get It Up</td>
      <td>1</td>
      <td>For Those About To Rock We Salute You</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Inject The Venom</td>
      <td>1</td>
      <td>For Those About To Rock We Salute You</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Snowballed</td>
      <td>1</td>
      <td>For Those About To Rock We Salute You</td>
      <td>1</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Evil Walks</td>
      <td>1</td>
      <td>For Those About To Rock We Salute You</td>
      <td>1</td>
    </tr>
    <tr>
      <th>6</th>
      <td>C.O.D.</td>
      <td>1</td>
      <td>For Those About To Rock We Salute You</td>
      <td>1</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Breaking The Rules</td>
      <td>1</td>
      <td>For Those About To Rock We Salute You</td>
      <td>1</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Night Of The Long Knives</td>
      <td>1</td>
      <td>For Those About To Rock We Salute You</td>
      <td>1</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Spellbound</td>
      <td>1</td>
      <td>For Those About To Rock We Salute You</td>
      <td>1</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Balls to the Wall</td>
      <td>2</td>
      <td>Balls to the Wall</td>
      <td>2</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Fast As a Shark</td>
      <td>3</td>
      <td>Restless and Wild</td>
      <td>2</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Restless and Wild</td>
      <td>3</td>
      <td>Restless and Wild</td>
      <td>2</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Princess of the Dawn</td>
      <td>3</td>
      <td>Restless and Wild</td>
      <td>2</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Go Down</td>
      <td>4</td>
      <td>Let There Be Rock</td>
      <td>1</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Dog Eat Dog</td>
      <td>4</td>
      <td>Let There Be Rock</td>
      <td>1</td>
    </tr>
    <tr>
      <th>16</th>
      <td>Let There Be Rock</td>
      <td>4</td>
      <td>Let There Be Rock</td>
      <td>1</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Bad Boy Boogie</td>
      <td>4</td>
      <td>Let There Be Rock</td>
      <td>1</td>
    </tr>
    <tr>
      <th>18</th>
      <td>Problem Child</td>
      <td>4</td>
      <td>Let There Be Rock</td>
      <td>1</td>
    </tr>
    <tr>
      <th>19</th>
      <td>Overdose</td>
      <td>4</td>
      <td>Let There Be Rock</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>
</div>
<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```

SELECT tracks."Name" AS "tracks_Name", albums."AlbumId" AS "albums_AlbumId", albums."Title" AS "albums_Title", albums."ArtistId" AS "albums_ArtistId" 
FROM tracks JOIN albums ON albums."AlbumId" = tracks."AlbumId"
 LIMIT ? OFFSET ?

```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python

# using orm
results = session.query(tracks.Name, albums).select_from(tracks).join(albums).limit(20)
display_results(results)

```
</div>

</div>



# 5. Tracks sold

1. print out the first 10 track sales from the `invoice_items` table
2. for these first 10 sales, print what are the names of the track sold, and the quantity sold




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
items = Base.classes['invoice_items']

# print out the first 10 track sales from the invoice_items table
query = select([items]).limit(10)
display_results(query)

# for these first 10 sales, print what are the names of the track sold, and the quantity sold
query = select([tracks.Name, items.Quantity]).select_from(join(items, tracks)).limit(10)
display_results(query)    

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">

<div markdown="0" class="output output_html">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>InvoiceLineId</th>
      <th>InvoiceId</th>
      <th>TrackId</th>
      <th>UnitPrice</th>
      <th>Quantity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>0.99</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>1</td>
      <td>4</td>
      <td>0.99</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>2</td>
      <td>6</td>
      <td>0.99</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>2</td>
      <td>8</td>
      <td>0.99</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>2</td>
      <td>10</td>
      <td>0.99</td>
      <td>1</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>2</td>
      <td>12</td>
      <td>0.99</td>
      <td>1</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>3</td>
      <td>16</td>
      <td>0.99</td>
      <td>1</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>3</td>
      <td>20</td>
      <td>0.99</td>
      <td>1</td>
    </tr>
    <tr>
      <th>8</th>
      <td>9</td>
      <td>3</td>
      <td>24</td>
      <td>0.99</td>
      <td>1</td>
    </tr>
    <tr>
      <th>9</th>
      <td>10</td>
      <td>3</td>
      <td>28</td>
      <td>0.99</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>
</div>
<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```

SELECT invoice_items."InvoiceLineId", invoice_items."InvoiceId", invoice_items."TrackId", invoice_items."UnitPrice", invoice_items."Quantity" 
FROM invoice_items
 LIMIT :param_1

```
</div>
</div>
<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">

<div markdown="0" class="output output_html">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Quantity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Balls to the Wall</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Restless and Wild</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Put The Finger On You</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Inject The Venom</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Evil Walks</td>
      <td>1</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Breaking The Rules</td>
      <td>1</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Dog Eat Dog</td>
      <td>1</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Overdose</td>
      <td>1</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Love In An Elevator</td>
      <td>1</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Janie's Got A Gun</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>
</div>
<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```

SELECT tracks."Name", invoice_items."Quantity" 
FROM invoice_items JOIN tracks ON tracks."TrackId" = invoice_items."TrackId"
 LIMIT :param_1

```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# orm
result = session.query(tracks.Name, items.Quantity).select_from(items).join(tracks).limit(10)
display_results(result)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">

<div markdown="0" class="output output_html">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Quantity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Balls to the Wall</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Restless and Wild</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Put The Finger On You</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Inject The Venom</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Evil Walks</td>
      <td>1</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Breaking The Rules</td>
      <td>1</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Dog Eat Dog</td>
      <td>1</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Overdose</td>
      <td>1</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Love In An Elevator</td>
      <td>1</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Janie's Got A Gun</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>
</div>
<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```

SELECT tracks."Name" AS "tracks_Name", invoice_items."Quantity" AS "invoice_items_Quantity" 
FROM invoice_items JOIN tracks ON tracks."TrackId" = invoice_items."TrackId"
 LIMIT ? OFFSET ?

```
</div>
</div>
</div>



# 6. Top tracks sold

print the names of top 10 tracks sold, and how many they times they were sold



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
from sqlalchemy import func, column

query = select([tracks.Name, func.sum(items.Quantity).label('sold')]) \
            .select_from(join(tracks, items)) \
            .group_by(tracks.TrackId) \
            .order_by(column('sold').desc()) \
            .limit(10)

display_results(query)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">

<div markdown="0" class="output output_html">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>sold</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Balls to the Wall</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Inject The Venom</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Snowballed</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Overdose</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Deuces Are Wild</td>
      <td>2</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Not The Doctor</td>
      <td>2</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Por Causa De Você</td>
      <td>2</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Welcome Home (Sanitarium)</td>
      <td>2</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Snowblind</td>
      <td>2</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Cornucopia</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>
</div>
<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```

SELECT tracks."Name", sum(invoice_items."Quantity") AS sold 
FROM tracks JOIN invoice_items ON tracks."TrackId" = invoice_items."TrackId" GROUP BY tracks."TrackId" ORDER BY sold DESC
 LIMIT :param_1

```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# orm
results = session.query(tracks.Name, func.sum(items.Quantity).label('sold')) \
            .select_from(tracks) \
            .join(items) \
            .group_by(tracks.TrackId) \
            .order_by(column('sold').desc()) \
            .limit(10)

display_results(results)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">

<div markdown="0" class="output output_html">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>sold</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Balls to the Wall</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Inject The Venom</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Snowballed</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Overdose</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Deuces Are Wild</td>
      <td>2</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Not The Doctor</td>
      <td>2</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Por Causa De Você</td>
      <td>2</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Welcome Home (Sanitarium)</td>
      <td>2</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Snowblind</td>
      <td>2</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Cornucopia</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>
</div>
<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```

SELECT tracks."Name" AS "tracks_Name", sum(invoice_items."Quantity") AS sold 
FROM tracks JOIN invoice_items ON tracks."TrackId" = invoice_items."TrackId" GROUP BY tracks."TrackId" ORDER BY sold DESC
 LIMIT ? OFFSET ?

```
</div>
</div>
</div>



# 7. top selling artists
Who are the top 10 highest selling artists?

> _hint: you need to join the invoice_items, tracks, albums and artists tables_




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
artists = Base.classes['artists']

# solution using sqlalchemy expressions
query = select([artists.Name, func.sum(items.Quantity).label('sold')]) \
    .select_from(join(items, tracks).join(albums).join(artists)) \
    .group_by(artists.ArtistId) \
    .order_by(column('sold').desc()) \
    .limit(10)
display_results(query)


```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">

<div markdown="0" class="output output_html">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>sold</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Iron Maiden</td>
      <td>140</td>
    </tr>
    <tr>
      <th>1</th>
      <td>U2</td>
      <td>107</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Metallica</td>
      <td>91</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Led Zeppelin</td>
      <td>87</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Os Paralamas Do Sucesso</td>
      <td>45</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Deep Purple</td>
      <td>44</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Faith No More</td>
      <td>42</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Lost</td>
      <td>41</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Eric Clapton</td>
      <td>40</td>
    </tr>
    <tr>
      <th>9</th>
      <td>R.E.M.</td>
      <td>39</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>
</div>
<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```

SELECT artists."Name", sum(invoice_items."Quantity") AS sold 
FROM invoice_items JOIN tracks ON tracks."TrackId" = invoice_items."TrackId" JOIN albums ON albums."AlbumId" = tracks."AlbumId" JOIN artists ON artists."ArtistId" = albums."ArtistId" GROUP BY artists."ArtistId" ORDER BY sold DESC
 LIMIT :param_1

```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python

# solution using sqlalchemy orm
query = session.query(func.sum(items.Quantity).label('sold'), artists.Name.label('Artist')) \
    .select_from(items) \
    .join(tracks) \
    .join(albums) \
    .join(artists) \
    .group_by(artists.ArtistId) \
    .order_by(column('sold').desc()) \
    .limit(10)
display_results(query)


```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">

<div markdown="0" class="output output_html">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>sold</th>
      <th>Artist</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>140</td>
      <td>Iron Maiden</td>
    </tr>
    <tr>
      <th>1</th>
      <td>107</td>
      <td>U2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>91</td>
      <td>Metallica</td>
    </tr>
    <tr>
      <th>3</th>
      <td>87</td>
      <td>Led Zeppelin</td>
    </tr>
    <tr>
      <th>4</th>
      <td>45</td>
      <td>Os Paralamas Do Sucesso</td>
    </tr>
    <tr>
      <th>5</th>
      <td>44</td>
      <td>Deep Purple</td>
    </tr>
    <tr>
      <th>6</th>
      <td>42</td>
      <td>Faith No More</td>
    </tr>
    <tr>
      <th>7</th>
      <td>41</td>
      <td>Lost</td>
    </tr>
    <tr>
      <th>8</th>
      <td>40</td>
      <td>Eric Clapton</td>
    </tr>
    <tr>
      <th>9</th>
      <td>39</td>
      <td>R.E.M.</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>
</div>
<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```

SELECT sum(invoice_items."Quantity") AS sold, artists."Name" AS "Artist" 
FROM invoice_items JOIN tracks ON tracks."TrackId" = invoice_items."TrackId" JOIN albums ON albums."AlbumId" = tracks."AlbumId" JOIN artists ON artists."ArtistId" = albums."ArtistId" GROUP BY artists."ArtistId" ORDER BY sold DESC
 LIMIT ? OFFSET ?

```
</div>
</div>
</div>

