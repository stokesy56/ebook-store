from oop_connection import *

server = 'localhost,1433'
database = 'books_db'
username = 'SA'
password = 'Passw0rd2018'

db_books = ConnectMsS(server,database,username,password)
