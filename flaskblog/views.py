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

@app.route('/new', methods=['GET', 'POST'])
def new_blog_entry():
    if request.method == 'POST':
        blog_title = request.form.get('title')
        blog_text = request.form.get('text')
        if blog_title and blog_text: # make sure they are not null, later change this to the client side
            db = get_db()
            db.execute('insert into blogentries (text, title) values (?, ?)', (blog_title, blog_text))
            db.commit()
            return redirect(url_for('blog_entries'))
    return render_template('new_blog_entry.html')
