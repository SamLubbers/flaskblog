import re

def trim(text):
    """function used to trim blog_bp text in templates"""
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