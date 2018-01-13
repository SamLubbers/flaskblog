from flaskblog import app
import datetime
import re

@app.context_processor
def text_processing():
    def trim(text):
        """function used to trim blog text in templates"""
        if len(text) > 160:
            text = text[:160].rstrip()
            text = re.sub('\W$','',text)
            text = text + '...'
            return text
        else:
            return text
    def format_date(date):
        date = date.strftime('%H:%M %m/%d/%Y')
        return date

    return dict(trim=trim, format_date=format_date)
