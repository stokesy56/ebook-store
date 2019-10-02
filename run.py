from oop_connection import *
from books_class import *

server = 'localhost,1433'
database = 'books_db'
username = 'SA'
password = 'Passw0rd2018'

db_books = Books(server,database,username,password)
db_books.print_all_entries()
print(db_books.find_book('Stormbreaker'))