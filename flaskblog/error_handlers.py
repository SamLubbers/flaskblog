from flaskblog import app
from flask import render_template


server_error_code = 500
@app.errorhandler(server_error_code)
def server_error(e):
    return render_template('error.html', code=server_error_code), server_error_code

gone_code = 410
@app.errorhandler(gone_code)
def gone(e):
    return render_template('error.html', code=gone_code), gone_code

not_found_code = 404
@app.errorhandler(not_found_code)
def not_found(e):
    return render_template('error.html', code=not_found_code), not_found_code

forbidden_code = 403
@app.errorhandler(forbidden_code)
def forbidden(e):
    return render_template('error.html', code=forbidden_code), forbidden_code
