from .connection import Connection


c = Connection().getCursor()

c.execute("""
    CREATE DATABASE IF NOT EXIST netsweepers;
""")