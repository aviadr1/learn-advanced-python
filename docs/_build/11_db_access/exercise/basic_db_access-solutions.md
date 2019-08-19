---
redirect_from:
  - "/11-db-access/exercise/basic-db-access-solutions"
interact_link: content/11_db_access/exercise/basic_db_access-solutions.ipynb
kernel_name: python3
has_widgets: false
title: 'Basic Db Access-solutions'
prev_page:
  url: /11_db_access/exercise/basic_db_access-questions.html
  title: 'Basic Db Access-questions'
next_page:
  url: /11_db_access/exercise/sqlalchemy_orm-questions.html
  title: 'Sqlalchemy Orm-questions'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-advanced-python/blob/master/content/11_db_access/exercise/basic_db_access-solutions.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




# Chinook sample SQLite database

in this exercise we're going to experiment with the [Chinook sample DB](http://www.sqlitetutorial.net/sqlite-sample-database/).

![Chinook](http://www.sqlitetutorial.net/wp-content/uploads/2015/11/sqlite-sample-database-color.jpg)

First, run the code below to download the database locally



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# download and extract chinook sample DB
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



# 1. open the database
1. connect to the database using the `sqlite3` or `pyodbc` module interface. place the connection object in a variable named `conn`
2. create a cursor object and put it in the variable `cur`



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
import sqlite3
db="chinook.db"
conn = sqlite3.connect(db)
cur = conn.cursor()

```
</div>

</div>



# 2. table names
run an SQL to print out all the table names and their schema



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
rs = cur.execute(
    """
    SELECT name, sql FROM sqlite_master
    WHERE type='table'
    ORDER BY name;
    """)
    
for name, sql, *args in rs:
    print(name)
    print(sql)
    print()

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
albums
CREATE TABLE "albums"
(
    [AlbumId] INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    [Title] NVARCHAR(160)  NOT NULL,
    [ArtistId] INTEGER  NOT NULL,
    FOREIGN KEY ([ArtistId]) REFERENCES "artists" ([ArtistId]) 
		ON DELETE NO ACTION ON UPDATE NO ACTION
)

artists
CREATE TABLE "artists"
(
    [ArtistId] INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    [Name] NVARCHAR(120)
)

customers
CREATE TABLE "customers"
(
    [CustomerId] INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    [FirstName] NVARCHAR(40)  NOT NULL,
    [LastName] NVARCHAR(20)  NOT NULL,
    [Company] NVARCHAR(80),
    [Address] NVARCHAR(70),
    [City] NVARCHAR(40),
    [State] NVARCHAR(40),
    [Country] NVARCHAR(40),
    [PostalCode] NVARCHAR(10),
    [Phone] NVARCHAR(24),
    [Fax] NVARCHAR(24),
    [Email] NVARCHAR(60)  NOT NULL,
    [SupportRepId] INTEGER,
    FOREIGN KEY ([SupportRepId]) REFERENCES "employees" ([EmployeeId]) 
		ON DELETE NO ACTION ON UPDATE NO ACTION
)

employees
CREATE TABLE "employees"
(
    [EmployeeId] INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    [LastName] NVARCHAR(20)  NOT NULL,
    [FirstName] NVARCHAR(20)  NOT NULL,
    [Title] NVARCHAR(30),
    [ReportsTo] INTEGER,
    [BirthDate] DATETIME,
    [HireDate] DATETIME,
    [Address] NVARCHAR(70),
    [City] NVARCHAR(40),
    [State] NVARCHAR(40),
    [Country] NVARCHAR(40),
    [PostalCode] NVARCHAR(10),
    [Phone] NVARCHAR(24),
    [Fax] NVARCHAR(24),
    [Email] NVARCHAR(60),
    FOREIGN KEY ([ReportsTo]) REFERENCES "employees" ([EmployeeId]) 
		ON DELETE NO ACTION ON UPDATE NO ACTION
)

genres
CREATE TABLE "genres"
(
    [GenreId] INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    [Name] NVARCHAR(120)
)

invoice_items
CREATE TABLE "invoice_items"
(
    [InvoiceLineId] INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    [InvoiceId] INTEGER  NOT NULL,
    [TrackId] INTEGER  NOT NULL,
    [UnitPrice] NUMERIC(10,2)  NOT NULL,
    [Quantity] INTEGER  NOT NULL,
    FOREIGN KEY ([InvoiceId]) REFERENCES "invoices" ([InvoiceId]) 
		ON DELETE NO ACTION ON UPDATE NO ACTION,
    FOREIGN KEY ([TrackId]) REFERENCES "tracks" ([TrackId]) 
		ON DELETE NO ACTION ON UPDATE NO ACTION
)

invoices
CREATE TABLE "invoices"
(
    [InvoiceId] INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    [CustomerId] INTEGER  NOT NULL,
    [InvoiceDate] DATETIME  NOT NULL,
    [BillingAddress] NVARCHAR(70),
    [BillingCity] NVARCHAR(40),
    [BillingState] NVARCHAR(40),
    [BillingCountry] NVARCHAR(40),
    [BillingPostalCode] NVARCHAR(10),
    [Total] NUMERIC(10,2)  NOT NULL,
    FOREIGN KEY ([CustomerId]) REFERENCES "customers" ([CustomerId]) 
		ON DELETE NO ACTION ON UPDATE NO ACTION
)

media_types
CREATE TABLE "media_types"
(
    [MediaTypeId] INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    [Name] NVARCHAR(120)
)

playlist_track
CREATE TABLE "playlist_track"
(
    [PlaylistId] INTEGER  NOT NULL,
    [TrackId] INTEGER  NOT NULL,
    CONSTRAINT [PK_PlaylistTrack] PRIMARY KEY  ([PlaylistId], [TrackId]),
    FOREIGN KEY ([PlaylistId]) REFERENCES "playlists" ([PlaylistId]) 
		ON DELETE NO ACTION ON UPDATE NO ACTION,
    FOREIGN KEY ([TrackId]) REFERENCES "tracks" ([TrackId]) 
		ON DELETE NO ACTION ON UPDATE NO ACTION
)

playlists
CREATE TABLE "playlists"
(
    [PlaylistId] INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    [Name] NVARCHAR(120)
)

sqlite_sequence
CREATE TABLE sqlite_sequence(name,seq)

sqlite_stat1
CREATE TABLE sqlite_stat1(tbl,idx,stat)

tracks
CREATE TABLE "tracks"
(
    [TrackId] INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    [Name] NVARCHAR(200)  NOT NULL,
    [AlbumId] INTEGER,
    [MediaTypeId] INTEGER  NOT NULL,
    [GenreId] INTEGER,
    [Composer] NVARCHAR(220),
    [Milliseconds] INTEGER  NOT NULL,
    [Bytes] INTEGER,
    [UnitPrice] NUMERIC(10,2)  NOT NULL,
    FOREIGN KEY ([AlbumId]) REFERENCES "albums" ([AlbumId]) 
		ON DELETE NO ACTION ON UPDATE NO ACTION,
    FOREIGN KEY ([GenreId]) REFERENCES "genres" ([GenreId]) 
		ON DELETE NO ACTION ON UPDATE NO ACTION,
    FOREIGN KEY ([MediaTypeId]) REFERENCES "media_types" ([MediaTypeId]) 
		ON DELETE NO ACTION ON UPDATE NO ACTION
)

```
</div>
</div>
</div>



# 3. Tracks
print out the first three tracks in the `tracks` table



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
rs = cur.execute(
    """
    SELECT * 
    FROM tracks
    LIMIT 3;
    """)

for row in rs:
    print(row)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
(1, 'For Those About To Rock (We Salute You)', 1, 1, 1, 'Angus Young, Malcolm Young, Brian Johnson', 343719, 11170334, 0.99)
(2, 'Balls to the Wall', 2, 2, 1, None, 342562, 5510424, 0.99)
(3, 'Fast As a Shark', 3, 2, 1, 'F. Baltes, S. Kaufman, U. Dirkscneider & W. Hoffman', 230619, 3990994, 0.99)
```
</div>
</div>
</div>



# 4. Albums from Tracks
print out the track name and albums title of the first 20 tracks in the `tracks` table





<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
rs = cur.execute(
    """
    SELECT tracks.Name, albums.*
    FROM tracks
    JOIN albums ON tracks.AlbumId == albums.AlbumId
    LIMIT 20
    ;
    """)

for row in rs:
    print(row)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
('For Those About To Rock (We Salute You)', 1, 'For Those About To Rock We Salute You', 1)
('Put The Finger On You', 1, 'For Those About To Rock We Salute You', 1)
("Let's Get It Up", 1, 'For Those About To Rock We Salute You', 1)
('Inject The Venom', 1, 'For Those About To Rock We Salute You', 1)
('Snowballed', 1, 'For Those About To Rock We Salute You', 1)
('Evil Walks', 1, 'For Those About To Rock We Salute You', 1)
('C.O.D.', 1, 'For Those About To Rock We Salute You', 1)
('Breaking The Rules', 1, 'For Those About To Rock We Salute You', 1)
('Night Of The Long Knives', 1, 'For Those About To Rock We Salute You', 1)
('Spellbound', 1, 'For Those About To Rock We Salute You', 1)
('Balls to the Wall', 2, 'Balls to the Wall', 2)
('Fast As a Shark', 3, 'Restless and Wild', 2)
('Restless and Wild', 3, 'Restless and Wild', 2)
('Princess of the Dawn', 3, 'Restless and Wild', 2)
('Go Down', 4, 'Let There Be Rock', 1)
('Dog Eat Dog', 4, 'Let There Be Rock', 1)
('Let There Be Rock', 4, 'Let There Be Rock', 1)
('Bad Boy Boogie', 4, 'Let There Be Rock', 1)
('Problem Child', 4, 'Let There Be Rock', 1)
('Overdose', 4, 'Let There Be Rock', 1)
```
</div>
</div>
</div>



# 5. Tracks sold

1. print out the first 10 track sales from the `invoice_items` table
2. for these first 10 sales, print what are the names of the track sold, and the quantity sold




<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# print out the first 10 track sales from the invoice_items table
rs = cur.execute(
    """
    SELECT *
    FROM invoice_items
    LIMIT 10
    ;
    """)

for row in rs:
    print(row)
    
print()

# what are the names of the tracks sold in the first 10 invoices?
rs = cur.execute(
    """
    SELECT tracks.Name, invoice_items.Quantity
    FROM invoice_items
    JOIN tracks ON invoice_items.TrackId == tracks.TrackId 
    LIMIT 10
    ;
    """)

for row in rs:
    print(row)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
(1, 1, 2, 0.99, 1)
(2, 1, 4, 0.99, 1)
(3, 2, 6, 0.99, 1)
(4, 2, 8, 0.99, 1)
(5, 2, 10, 0.99, 1)
(6, 2, 12, 0.99, 1)
(7, 3, 16, 0.99, 1)
(8, 3, 20, 0.99, 1)
(9, 3, 24, 0.99, 1)
(10, 3, 28, 0.99, 1)

('Balls to the Wall', 1)
('Restless and Wild', 1)
('Put The Finger On You', 1)
('Inject The Venom', 1)
('Evil Walks', 1)
('Breaking The Rules', 1)
('Dog Eat Dog', 1)
('Overdose', 1)
('Love In An Elevator', 1)
("Janie's Got A Gun", 1)
```
</div>
</div>
</div>



# 6. Top tracks sold

print the names of top 10 tracks sold, and how many they times they were sold



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
rs = cur.execute(
    """
    SELECT tracks.Name, SUM(Quantity) AS sold
    FROM invoice_items
    JOIN tracks ON invoice_items.TrackId == tracks.TrackId 
    GROUP BY invoice_items.TrackId
    ORDER BY sold DESC    
    LIMIT 10
    ;
    """)

for row in rs:
    print(row)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
('Balls to the Wall', 2)
('Inject The Venom', 2)
('Snowballed', 2)
('Overdose', 2)
('Deuces Are Wild', 2)
('Not The Doctor', 2)
('Por Causa De Você', 2)
('Welcome Home (Sanitarium)', 2)
('Snowblind', 2)
('Cornucopia', 2)
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
rs = cur.execute(
    """
    SELECT artists.Name, SUM(Quantity) AS sold
    FROM invoice_items
    JOIN tracks ON invoice_items.TrackId == tracks.TrackId
    JOIN albums ON tracks.AlbumId == albums.AlbumId
    JOIN artists ON albums.ArtistId == artists.ArtistId
    GROUP BY artists.ArtistId
    ORDER BY sold DESC    
    LIMIT 10
    ;
    """)

for row in rs:
    print(row)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
('Iron Maiden', 140)
('U2', 107)
('Metallica', 91)
('Led Zeppelin', 87)
('Os Paralamas Do Sucesso', 45)
('Deep Purple', 44)
('Faith No More', 42)
('Lost', 41)
('Eric Clapton', 40)
('R.E.M.', 39)
```
</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python



```
</div>

</div>

