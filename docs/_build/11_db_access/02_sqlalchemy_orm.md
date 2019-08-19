---
redirect_from:
  - "/11-db-access/02-sqlalchemy-orm"
interact_link: content/11_db_access/02_sqlalchemy_orm.ipynb
kernel_name: python3
has_widgets: false
title: 'Sqlalchemy Orm'
prev_page:
  url: /11_db_access/01_basic_db_access.html
  title: 'Basic Db Access'
next_page:
  url: /11_db_access/exercise/basic_db_access-questions.html
  title: 'exercise'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-advanced-python/blob/master/content/11_db_access/02_sqlalchemy_orm.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




# SQLAlchemy
> SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL.

We're going to show how to create a database, add some data and do basic queries.
more complex queriex, doing migrations and database admin, are outside the scope of this lesson



## Create a new database from scratch
Lets create a new database from scratch. we will
1. Create classes to define a schema
2. Map the scheme to a database
3. add objects to the database
4. run queries

> NOTE: we will use an in-memory database, but running with a file based one or a remote database would be just as easy



### 1. Create a database session



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
from sqlalchemy import create_engine
#engine = create_engine('sqlite:///example.db', echo=True)
engine = create_engine('sqlite:///:memory:', echo=True)
#engine = create_engine('sqlite:///:memory:')
conn = engine.connect()

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
2019-07-15 19:23:47,832 INFO sqlalchemy.engine.base.Engine SELECT CAST('test plain returns' AS VARCHAR(60)) AS anon_1
2019-07-15 19:23:47,838 INFO sqlalchemy.engine.base.Engine ()
2019-07-15 19:23:47,838 INFO sqlalchemy.engine.base.Engine SELECT CAST('test unicode returns' AS VARCHAR(60)) AS anon_1
2019-07-15 19:23:47,839 INFO sqlalchemy.engine.base.Engine ()
```
</div>
</div>
</div>



### 2. Helper functions to print SQL queries and SQL results



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
from IPython.display import display
import pandas as pd
import sqlalchemy

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
    #sql(query)

```
</div>

</div>



### 3.  creating a schema base



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy_explore

### the basic base class for SQLAlchemy schema objects
# Base = declarative_base(bind=engine)

### base class including utils like an __repr__ method
### see https://pypi.org/project/sqlalchemy-explore/
Base = declarative_base(cls=sqlalchemy_explore.ReflectiveMixin)

```
</div>

</div>



### 4. Create the schema



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
from sqlalchemy import Column, DateTime, ForeignKey, Integer, NVARCHAR, Numeric, Sequence
from sqlalchemy.orm import relationship

class Customer(Base):
    __tablename__ = 'customers'

    CustomerId = Column(Integer, Sequence('customer_id_seq'), primary_key=True)
    FirstName = Column(NVARCHAR(40), nullable=False)
    LastName = Column(NVARCHAR(20), nullable=False)
    Company = Column(NVARCHAR(80))
    Address = Column(NVARCHAR(70))
    Phone = Column(NVARCHAR(24))
    Email = Column(NVARCHAR(60), nullable=False)
    
class Item(Base):
    __tablename__ = 'items'
    
    ItemId = Column(Integer, Sequence('item_id_seq'), primary_key=True)
    Name = Column(NVARCHAR(40), nullable=False)
    Price = Column(Numeric, nullable=False)

class Purchase(Base):
    __tablename__ = 'purchases'
    
    PurchaseId = Column(Integer, Sequence('purchase_id_seq'), primary_key=True)
    ItemId = Column(ForeignKey('items.ItemId'), nullable=False, index=True)
    CustomerId = Column(ForeignKey('customers.CustomerId'), nullable=False, index=True)
    Date = Column(DateTime, nullable=False)
    
    item = relationship('Item')
    customer = relationship('Customer')

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
Purchase.ItemId.name

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
'ItemId'
```


</div>
</div>
</div>



### 5. Create tables in the database to conform with the schema



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
Base.metadata.create_all(engine)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
2019-07-15 19:23:48,336 INFO sqlalchemy.engine.base.Engine PRAGMA table_info("customers")
2019-07-15 19:23:48,337 INFO sqlalchemy.engine.base.Engine ()
2019-07-15 19:23:48,338 INFO sqlalchemy.engine.base.Engine PRAGMA table_info("items")
2019-07-15 19:23:48,339 INFO sqlalchemy.engine.base.Engine ()
2019-07-15 19:23:48,339 INFO sqlalchemy.engine.base.Engine PRAGMA table_info("purchases")
2019-07-15 19:23:48,340 INFO sqlalchemy.engine.base.Engine ()
2019-07-15 19:23:48,341 INFO sqlalchemy.engine.base.Engine 
CREATE TABLE customers (
	"CustomerId" INTEGER NOT NULL, 
	"FirstName" NVARCHAR(40) NOT NULL, 
	"LastName" NVARCHAR(20) NOT NULL, 
	"Company" NVARCHAR(80), 
	"Address" NVARCHAR(70), 
	"Phone" NVARCHAR(24), 
	"Email" NVARCHAR(60) NOT NULL, 
	PRIMARY KEY ("CustomerId")
)


2019-07-15 19:23:48,342 INFO sqlalchemy.engine.base.Engine ()
2019-07-15 19:23:48,342 INFO sqlalchemy.engine.base.Engine COMMIT
2019-07-15 19:23:48,343 INFO sqlalchemy.engine.base.Engine 
CREATE TABLE items (
	"ItemId" INTEGER NOT NULL, 
	"Name" NVARCHAR(40) NOT NULL, 
	"Price" NUMERIC NOT NULL, 
	PRIMARY KEY ("ItemId")
)


2019-07-15 19:23:48,344 INFO sqlalchemy.engine.base.Engine ()
2019-07-15 19:23:48,344 INFO sqlalchemy.engine.base.Engine COMMIT
2019-07-15 19:23:48,345 INFO sqlalchemy.engine.base.Engine 
CREATE TABLE purchases (
	"PurchaseId" INTEGER NOT NULL, 
	"ItemId" INTEGER NOT NULL, 
	"CustomerId" INTEGER NOT NULL, 
	"Date" DATETIME NOT NULL, 
	PRIMARY KEY ("PurchaseId"), 
	FOREIGN KEY("ItemId") REFERENCES items ("ItemId"), 
	FOREIGN KEY("CustomerId") REFERENCES customers ("CustomerId")
)


2019-07-15 19:23:48,346 INFO sqlalchemy.engine.base.Engine ()
2019-07-15 19:23:48,346 INFO sqlalchemy.engine.base.Engine COMMIT
2019-07-15 19:23:48,347 INFO sqlalchemy.engine.base.Engine CREATE INDEX "ix_purchases_CustomerId" ON purchases ("CustomerId")
2019-07-15 19:23:48,348 INFO sqlalchemy.engine.base.Engine ()
2019-07-15 19:23:48,349 INFO sqlalchemy.engine.base.Engine COMMIT
2019-07-15 19:23:48,349 INFO sqlalchemy.engine.base.Engine CREATE INDEX "ix_purchases_ItemId" ON purchases ("ItemId")
2019-07-15 19:23:48,350 INFO sqlalchemy.engine.base.Engine ()
2019-07-15 19:23:48,351 INFO sqlalchemy.engine.base.Engine COMMIT
```
</div>
</div>
</div>



### 6. Create a customer



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
moshe = Customer(
    FirstName='Moshe', 
    LastName='Cohen', 
    Address='Alenbi 99, Tel Aviv', 
    Phone="053-5556789", 
    Email='moshe@cohen.com')

session.add(moshe)
session.commit()

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
2019-07-15 19:23:48,361 INFO sqlalchemy.engine.base.Engine BEGIN (implicit)
2019-07-15 19:23:48,363 INFO sqlalchemy.engine.base.Engine INSERT INTO customers ("FirstName", "LastName", "Company", "Address", "Phone", "Email") VALUES (?, ?, ?, ?, ?, ?)
2019-07-15 19:23:48,364 INFO sqlalchemy.engine.base.Engine ('Moshe', 'Cohen', None, 'Alenbi 99, Tel Aviv', '053-5556789', 'moshe@cohen.com')
2019-07-15 19:23:48,365 INFO sqlalchemy.engine.base.Engine COMMIT
```
</div>
</div>
</div>



### 7. run queries



#### Using SQLAlchemy expression language



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
from sqlalchemy import select 

customers_query = select([Customer.FirstName, Customer.Email])
results = conn.execute(customers_query)

print()
for row in results:
    print(row)

print()
print(type(row)) # rows are of type sqlalchemy.engine.result.RowProxy

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
2019-07-15 19:23:48,373 INFO sqlalchemy.engine.base.Engine SELECT customers."FirstName", customers."Email" 
FROM customers
2019-07-15 19:23:48,374 INFO sqlalchemy.engine.base.Engine ()

('Moshe', 'moshe@cohen.com')

<class 'sqlalchemy.engine.result.RowProxy'>
```
</div>
</div>
</div>



> Our handy `display_results` function uses `pandas` library to display the results as a table



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
display_results(customers_query)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
2019-07-15 19:23:48,382 INFO sqlalchemy.engine.base.Engine SELECT customers."FirstName", customers."Email" 
FROM customers
2019-07-15 19:23:48,383 INFO sqlalchemy.engine.base.Engine ()
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
      <th>FirstName</th>
      <th>Email</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Moshe</td>
      <td>moshe@cohen.com</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>
</div>
</div>



#### Using SQLAlchemy ORM Object Relation Manager



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
results = session.query(Customer)

print()
for customer in results:
    print(customer)
    
print()
print(type(customer))

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```

2019-07-15 19:23:48,399 INFO sqlalchemy.engine.base.Engine BEGIN (implicit)
2019-07-15 19:23:48,401 INFO sqlalchemy.engine.base.Engine SELECT customers."CustomerId" AS "customers_CustomerId", customers."FirstName" AS "customers_FirstName", customers."LastName" AS "customers_LastName", customers."Company" AS "customers_Company", customers."Address" AS "customers_Address", customers."Phone" AS "customers_Phone", customers."Email" AS "customers_Email" 
FROM customers
2019-07-15 19:23:48,402 INFO sqlalchemy.engine.base.Engine ()
Customer(CustomerId=1, FirstName='Moshe', LastName='Cohen', Company=None, Address='Alenbi 99, Tel Aviv', Phone='053-5556789', Email='moshe@cohen.com')

<class '__main__.Customer'>
```
</div>
</div>
</div>



## Reflect an existing database

When we have an existing database, and would like to start accessing this database using SQLAlchemy, we need to have classes that represent the database. 

Being good lazy programmers, we often don't want to write these classes by hand, and would like a helpful start.
We're going to show how to create such classes from an existing database.

we will do it in two methods
1. use the automap class in SQLAlchemy to create dynamic classes (without source) for the db
2. use the `sqlacodegen` module [1] to generate source code for classes

[1]: https://pypi.org/project/sqlacodegen/

### Chinook sample DB
Let's download a sample database called [Chinook](http://www.sqlitetutorial.net/sqlite-sample-database/) 
![Chinook](http://www.sqlitetutorial.net/wp-content/uploads/2015/11/sqlite-sample-database-color.jpg)

there's a file in the `notebooks` directory called `download_chinook.py` with simple code to download this zip to the current directory. 



> lets run `download_chinook.download` now



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# run this code to get the chinook database
import download_chinook
download_chinook.download()

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
ready: C:\Users\CP\Downloads\learn-advanced-python-master\notebooks\chinook.db
```
</div>
</div>
</div>



> Now lets connect to the database and create an `engine` variable



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
import sqlalchemy
from sqlalchemy import create_engine
engine = create_engine('sqlite:///chinook.db')

```
</div>

</div>



> lets get the list of table names from the database



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



### using automap to refelect a db

We use the `automap` extension to __dynamically__ create classes for each table __at runtime__. 

- __advantage__: automap is faily easy to use, and it comes bundled in SQLAlchemy without a need for installing additional modules
- __disadvantage__: There is no way to see the _code_ for these automap classes. we need to use the classes without seeing the code for it




> first, lets define a helper function called `automap_database()` that generates classes for us



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
def automap_database(engine):
    ### useful: extract classes from the chinook database
    metadata = sqlalchemy.MetaData()
    metadata.reflect(engine)

    ## we need to do this once
    from sqlalchemy.ext.automap import automap_base

    # produce a set of mappings from this MetaData.
    Base = automap_base(metadata=metadata)

    # calling prepare() just sets up mapped classes and relationships.
    Base.prepare()
    return Base

```
</div>

</div>



> next, lets use the `automap_database()` function and see which classes were generated



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# create dynamic classes for every table using automap 
AutoMapBase = automap_database(engine)

# which classes were generated?
print('Generated the following classes:')
print('\t', ', '.join(AutoMapBase.classes.keys()))

# Let's prepare an ORM session so we can query the database based on these classes
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
Generated the following classes:
	 albums, artists, customers, employees, genres, invoice_items, invoices, tracks, media_types, playlists
```
</div>
</div>
</div>



> Lastly, lets use one of these classes, see what columns it has and use it to query the database 



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# lets get the Album class for the albums table
Album = AutoMapBase.classes['albums']

# what columns are available in this class?
print('columns for Album class:')
print('\t', Album.__table__.columns) # 'albums.AlbumId', 'albums.Title', 'albums.ArtistId'

# lets get the first album and print it out
first_album = session.query(Album).first()
print()
print('first album:', type(first_album))
print('\t', first_album.AlbumId, first_album.Title, first_album.ArtistId)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
columns for Album class:
	 ['albums.AlbumId', 'albums.Title', 'albums.ArtistId']

first album: <class 'sqlalchemy.ext.automap.albums'>
	 1 For Those About To Rock We Salute You 1
```
</div>
</div>
</div>



### using sqlacodegen to generate classes with source code

> first, we need to install the `sqlacodegen` module



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
pip install sqlacodegen

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
Requirement already satisfied: sqlacodegen in c:\users\cp\appdata\local\programs\python\python37-32\lib\site-packages (2.0.1)
Requirement already satisfied: inflect>=0.2.0 in c:\users\cp\appdata\local\programs\python\python37-32\lib\site-packages (from sqlacodegen) (2.1.0)
Requirement already satisfied: SQLAlchemy>=0.8.0 in c:\users\cp\appdata\local\programs\python\python37-32\lib\site-packages (from sqlacodegen) (1.3.5)
Note: you may need to restart the kernel to use updated packages.
```
</div>
</div>
</div>



> now, lets run it



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
!sqlacodegen sqlite:///chinook.db --tables albums,artists,customers,employees,genres,invoice_items,invoices,tracks

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
# coding: utf-8
from sqlalchemy import Column, DateTime, ForeignKey, Integer, NVARCHAR, Numeric
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Artist(Base):
    __tablename__ = 'artists'

    ArtistId = Column(Integer, primary_key=True)
    Name = Column(NVARCHAR(120))


class Employee(Base):
    __tablename__ = 'employees'

    EmployeeId = Column(Integer, primary_key=True)
    LastName = Column(NVARCHAR(20), nullable=False)
    FirstName = Column(NVARCHAR(20), nullable=False)
    Title = Column(NVARCHAR(30))
    ReportsTo = Column(ForeignKey('employees.EmployeeId'), index=True)
    BirthDate = Column(DateTime)
    HireDate = Column(DateTime)
    Address = Column(NVARCHAR(70))
    City = Column(NVARCHAR(40))
    State = Column(NVARCHAR(40))
    Country = Column(NVARCHAR(40))
    PostalCode = Column(NVARCHAR(10))
    Phone = Column(NVARCHAR(24))
    Fax = Column(NVARCHAR(24))
    Email = Column(NVARCHAR(60))

    parent = relationship('Employee', remote_side=[EmployeeId])


class Genre(Base):
    __tablename__ = 'genres'

    GenreId = Column(Integer, primary_key=True)
    Name = Column(NVARCHAR(120))


class MediaType(Base):
    __tablename__ = 'media_types'

    MediaTypeId = Column(Integer, primary_key=True)
    Name = Column(NVARCHAR(120))


class Album(Base):
    __tablename__ = 'albums'

    AlbumId = Column(Integer, primary_key=True)
    Title = Column(NVARCHAR(160), nullable=False)
    ArtistId = Column(ForeignKey('artists.ArtistId'), nullable=False, index=True)

    artist = relationship('Artist')


class Customer(Base):
    __tablename__ = 'customers'

    CustomerId = Column(Integer, primary_key=True)
    FirstName = Column(NVARCHAR(40), nullable=False)
    LastName = Column(NVARCHAR(20), nullable=False)
    Company = Column(NVARCHAR(80))
    Address = Column(NVARCHAR(70))
    City = Column(NVARCHAR(40))
    State = Column(NVARCHAR(40))
    Country = Column(NVARCHAR(40))
    PostalCode = Column(NVARCHAR(10))
    Phone = Column(NVARCHAR(24))
    Fax = Column(NVARCHAR(24))
    Email = Column(NVARCHAR(60), nullable=False)
    SupportRepId = Column(ForeignKey('employees.EmployeeId'), index=True)

    employee = relationship('Employee')


class Invoice(Base):
    __tablename__ = 'invoices'

    InvoiceId = Column(Integer, primary_key=True)
    CustomerId = Column(ForeignKey('customers.CustomerId'), nullable=False, index=True)
    InvoiceDate = Column(DateTime, nullable=False)
    BillingAddress = Column(NVARCHAR(70))
    BillingCity = Column(NVARCHAR(40))
    BillingState = Column(NVARCHAR(40))
    BillingCountry = Column(NVARCHAR(40))
    BillingPostalCode = Column(NVARCHAR(10))
    Total = Column(Numeric(10, 2), nullable=False)

    customer = relationship('Customer')


class Track(Base):
    __tablename__ = 'tracks'

    TrackId = Column(Integer, primary_key=True)
    Name = Column(NVARCHAR(200), nullable=False)
    AlbumId = Column(ForeignKey('albums.AlbumId'), index=True)
    MediaTypeId = Column(ForeignKey('media_types.MediaTypeId'), nullable=False, index=True)
    GenreId = Column(ForeignKey('genres.GenreId'), index=True)
    Composer = Column(NVARCHAR(220))
    Milliseconds = Column(Integer, nullable=False)
    Bytes = Column(Integer)
    UnitPrice = Column(Numeric(10, 2), nullable=False)

    album = relationship('Album')
    genre = relationship('Genre')
    media_type = relationship('MediaType')


class InvoiceItem(Base):
    __tablename__ = 'invoice_items'

    InvoiceLineId = Column(Integer, primary_key=True)
    InvoiceId = Column(ForeignKey('invoices.InvoiceId'), nullable=False, index=True)
    TrackId = Column(ForeignKey('tracks.TrackId'), nullable=False, index=True)
    UnitPrice = Column(Numeric(10, 2), nullable=False)
    Quantity = Column(Integer, nullable=False)

    invoice = relationship('Invoice')
    track = relationship('Track')
```
</div>
</div>
</div>



> We can now copy-paste the generated source for these classes into our code so we can start using it   



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
from sqlalchemy import Column, DateTime, ForeignKey, Integer, NVARCHAR, Numeric
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata

class Artist(Base):
    __tablename__ = 'artists'

    ArtistId = Column(Integer, primary_key=True)
    Name = Column(NVARCHAR(120))


class Employee(Base):
    __tablename__ = 'employees'

    EmployeeId = Column(Integer, primary_key=True)
    LastName = Column(NVARCHAR(20), nullable=False)
    FirstName = Column(NVARCHAR(20), nullable=False)
    Title = Column(NVARCHAR(30))
    ReportsTo = Column(ForeignKey('employees.EmployeeId'), index=True)
    BirthDate = Column(DateTime)
    HireDate = Column(DateTime)
    Address = Column(NVARCHAR(70))
    City = Column(NVARCHAR(40))
    State = Column(NVARCHAR(40))
    Country = Column(NVARCHAR(40))
    PostalCode = Column(NVARCHAR(10))
    Phone = Column(NVARCHAR(24))
    Fax = Column(NVARCHAR(24))
    Email = Column(NVARCHAR(60))

    parent = relationship('Employee', remote_side=[EmployeeId])


class Genre(Base):
    __tablename__ = 'genres'

    GenreId = Column(Integer, primary_key=True)
    Name = Column(NVARCHAR(120))


class MediaType(Base):
    __tablename__ = 'media_types'

    MediaTypeId = Column(Integer, primary_key=True)
    Name = Column(NVARCHAR(120))


class Album(Base):
    __tablename__ = 'albums'

    AlbumId = Column(Integer, primary_key=True)
    Title = Column(NVARCHAR(160), nullable=False)
    ArtistId = Column(ForeignKey('artists.ArtistId'), nullable=False, index=True)

    artist = relationship('Artist')


class Customer(Base):
    __tablename__ = 'customers'

    CustomerId = Column(Integer, primary_key=True)
    FirstName = Column(NVARCHAR(40), nullable=False)
    LastName = Column(NVARCHAR(20), nullable=False)
    Company = Column(NVARCHAR(80))
    Address = Column(NVARCHAR(70))
    City = Column(NVARCHAR(40))
    State = Column(NVARCHAR(40))
    Country = Column(NVARCHAR(40))
    PostalCode = Column(NVARCHAR(10))
    Phone = Column(NVARCHAR(24))
    Fax = Column(NVARCHAR(24))
    Email = Column(NVARCHAR(60), nullable=False)
    SupportRepId = Column(ForeignKey('employees.EmployeeId'), index=True)

    employee = relationship('Employee')


class Invoice(Base):
    __tablename__ = 'invoices'

    InvoiceId = Column(Integer, primary_key=True)
    CustomerId = Column(ForeignKey('customers.CustomerId'), nullable=False, index=True)
    InvoiceDate = Column(DateTime, nullable=False)
    BillingAddress = Column(NVARCHAR(70))
    BillingCity = Column(NVARCHAR(40))
    BillingState = Column(NVARCHAR(40))
    BillingCountry = Column(NVARCHAR(40))
    BillingPostalCode = Column(NVARCHAR(10))
    Total = Column(Numeric(10, 2), nullable=False)

    customer = relationship('Customer')


class Track(Base):
    __tablename__ = 'tracks'

    TrackId = Column(Integer, primary_key=True)
    Name = Column(NVARCHAR(200), nullable=False)
    AlbumId = Column(ForeignKey('albums.AlbumId'), index=True)
    MediaTypeId = Column(ForeignKey('media_types.MediaTypeId'), nullable=False, index=True)
    GenreId = Column(ForeignKey('genres.GenreId'), index=True)
    Composer = Column(NVARCHAR(220))
    Milliseconds = Column(Integer, nullable=False)
    Bytes = Column(Integer)
    UnitPrice = Column(Numeric(10, 2), nullable=False)

    album = relationship('Album')
    genre = relationship('Genre')
    media_type = relationship('MediaType')


class InvoiceItem(Base):
    __tablename__ = 'invoice_items'

    InvoiceLineId = Column(Integer, primary_key=True)
    InvoiceId = Column(ForeignKey('invoices.InvoiceId'), nullable=False, index=True)
    TrackId = Column(ForeignKey('tracks.TrackId'), nullable=False, index=True)
    UnitPrice = Column(Numeric(10, 2), nullable=False)
    Quantity = Column(Integer, nullable=False)

    invoice = relationship('Invoice')
    track = relationship('Track')

```
</div>

</div>



> lets create a new engine and new orm session to use with this metadata (it is different from the automap metadata)



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
from sqlalchemy import create_engine
engine = create_engine('sqlite:///chinook.db')
conn = engine.connect()
metadata.reflect(engine)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()

```
</div>

</div>



> lets make a simple query



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# lets get the first album and print it out
first_track = session.query(Track).first()
print(type(first_track))
print('Song:', first_track.Name, '| Album:', first_track.album.Title, '| Artist:', first_track.album.artist.Name)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
<class '__main__.Track'>
Song: For Those About To Rock (We Salute You) | Album: For Those About To Rock We Salute You | Artist: AC/DC
```
</div>
</div>
</div>



# Further reading
- [Toward Data Science' SQLAlchemy tutorial](https://towardsdatascience.com/sqlalchemy-python-tutorial-79a577141a91)
- [SQLAlchemy Object Relational Tutorial](https://docs.sqlalchemy.org/en/13/orm/tutorial.html)
- [SQLAlchemy Expression Language Tutorial](https://docs.sqlalchemy.org/en/13/core/tutorial.html)
- [SQLAlchemy ORM Tutorial for Python Developers](https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/)
- [sqlalchemy-explore](https://pypi.org/project/sqlalchemy-explore/)
- Sample databases
  - https://github.com/jpwhite3/northwind-SQLite3
  - https://github.com/arjunchndr/Analyzing-Chinook-Database-using-SQL-and-Python

