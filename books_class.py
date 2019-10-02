from oop_connection import *

class Books(ConnectMsS):

    def print_all_entries(self):
        query_rows = self.filter_query(f"SELECT * FROM books")
        while True:
            record = query_rows.fetchone()
            if record is None:
                break
            print(f"-> {record[0]}) title: {record[1]} - Author: {record[2]} - Date: {record[3]}")