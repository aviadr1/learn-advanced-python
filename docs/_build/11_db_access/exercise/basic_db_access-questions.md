---
redirect_from:
  - "/11-db-access/exercise/basic-db-access-questions"
interact_link: content/11_db_access/exercise/basic_db_access-questions.ipynb
kernel_name: python3
has_widgets: false
title: 'exercise'
prev_page:
  url: /11_db_access/02_sqlalchemy_orm.html
  title: 'Sqlalchemy Orm'
next_page:
  url: /11_db_access/exercise/basic_db_access-questions.html
  title: 'Basic Db Access-questions'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
<a href="https://colab.research.google.com/github/aviadr1/learn-advanced-python/blob/master/content/11_db_access/exercise/basic_db_access-questions.ipynb" target="_blank">
<img src="https://colab.research.google.com/assets/colab-badge.svg" 
     title="Open this file in Google Colab" alt="Colab"/>
</a>




# Chinook sample SQLite database

in this exercise we're going to experiment with the [Chinook sample DB](http://www.sqlitetutorial.net/sqlite-sample-database/).

![Chinook](http://www.sqlitetutorial.net/wp-content/uploads/2015/11/sqlite-sample-database-color.jpg)

First, run the code below to download the database locally



# 1. open the database
1. connect to the database using the `sqlite3` or `pyodbc` module interface. place the connection object in a variable named `conn`
2. create a cursor object and put it in the variable `cur`



# 2. table names
run an SQL to print out all the table names and their schema



# 3. Tracks
print out the first three tracks in the `tracks` table



# 4. Albums from Tracks
print out the track name and albums title of the first 20 tracks in the `tracks` table





# 5. Tracks sold

1. print out the first 10 track sales from the `invoice_items` table
2. for these first 10 sales, print what are the names of the track sold, and the quantity sold




# 6. Top tracks sold

print the names of top 10 tracks sold, and how many they times they were sold



# 7. top selling artists
Who are the top 10 highest selling artists?

> _hint: you need to join the invoice_items, tracks, albums and artists tables_


