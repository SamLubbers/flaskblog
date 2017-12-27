from flaskblog import app
from flaskblog.db_manager import get_db
from flask import render_template, request, session, redirect, url_for

@app.route('/')
def blog_entries():
    db = get_db()
    cur = db.execute('select title, text from blogentries order by id desc')
    entries = cur.fetchall()
    return render_template('blog_entries.html', entries=entries)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form.get('username') != app.config['USERNAME']:
            error = 'invalid username'
        elif request.form.get('password') != app.config['PASSWORD']:
            error = 'invalid password'
        else:
            session['logged_in'] = True
            return redirect(url_for('blog_entries'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('blog_entries'))
