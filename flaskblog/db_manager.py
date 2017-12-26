import sqlite3
from flaskblog import app

def connect_db(db):
    """connect to a specific sqlite3 database"""
    con = sqlite3.connect(db)
    con.row_factory = sqlite3.Row # index based and case-insensitive name-based access to columns with no overhead
    return con
