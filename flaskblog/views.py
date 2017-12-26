from flaskblog import app
from flaskblog.db_manager import get_db
from flask import render_template

@app.route('/')
def index():
    return render_template('base.html')
