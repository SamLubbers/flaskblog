from flaskblog import app
from flaskblog.db_manager import get_db
from flask import render_template

@app.route('/')
def index():
    db = get_db()
    cur = db.execute('select title, text from blogentries order by id desc')
    entries = cur.fetchall()
    return render_template('blog_entries.html', entries=entries)
