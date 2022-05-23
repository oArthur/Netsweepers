import os
import mysql.connector
from dotenv import load_dotenv
from typing import Tuple, Any


class Connection:
    """Simple mysql.connector abstraction for memory cleanup and cursor factory"""
    def __init__(self):
        load_dotenv('../../.env')
        user = os.environ.get('DB_USER')
        user = os.environ.get('DB_USER') if user != None else 'root'
        password = os.environ.get('DB_PASS')
        password = os.environ.get('DB_PASS') if password != None else 'notASafePassword'
        host = os.environ.get('DB_HOST')
        host = os.environ.get('DB_HOST') if host != None else '127.0.0.1'
        database = os.environ.get('DB_DATABASE')
        database = os.environ.get('DB_DATABASE') if host != None else 'netsweepers'

        self.cnx = mysql.connector.connect(
                        user= user,
                        password=password,
                        host=host,
                        database=database
                    )
    
    def getCursor(self):
        return self.cnx.cursor()
    
    def __del__(self):
        self.cnx.close()



if __name__ == "__main__":
    c = Connection().getCursor()
    print(c)