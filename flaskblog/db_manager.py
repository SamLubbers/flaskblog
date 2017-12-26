import sqlite3
import os
from flaskblog import app

def connect_db():
    """connect to a sqlite3 database defined in configuration"""
    # to avoid errors make sure all directories leading to db location exist
    db = app.config['DATABASE']
    path_to_db = os.path.dirname(db)
    if not os.path.exists(path_to_db):
        os.makedirs(path_to_db)

    # establish connection
    con = sqlite3.connect(db)
    con.row_factory = sqlite3.Row # index based and case-insensitive name-based access to columns with no overhead
    return con
