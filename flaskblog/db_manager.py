import sqlite3
import os
from flask import g
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
    con.row_factory = sqlite3.Row  # index based and case-insensitive name-based access to columns with no overhead
    return con


def get_db():
    """opens a database connection if there is none yet for the current application context"""
    if not hasattr(g, 'db'):
        g.db = connect_db()
    return g.db

@app.before_first_request
def init_db():
    """initializes database with tables defined in schema.sql if the database does not exist yet"""
    if not os.path.exists(app.config['DATABASE']):
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
        print('new db initialised')

@app.teardown_appcontext
def close_db(error):
    """closes database connection at the end of a request"""
    if hasattr(g, 'db'):
        g.db.close()
