import re


def trim(text):
    """trim blog text in index page"""
    if len(text) > 160:
        text = text[:160].rstrip()
        text = re.sub('\W$','',text)
        text = text + '...'
        return text
    else:
        return text

def format_date(date):
    """format the date of blog to correct format"""
    date = date.strftime('%H:%M %m/%d/%Y')
    return date
