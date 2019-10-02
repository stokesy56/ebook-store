import pyodbc

class ConnectMsS():
    def __init__(self,server,database,username,password):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.conn_books_db = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER= '+self.server+';DATABASE='+self.database+';UID='+self.username+';PWD='+self.password)
        self.cursor = self.conn_books_db.cursor()

    def filter_query(self, query):
        return self.cursor.execute(query)
