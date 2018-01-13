from flaskblog import app
import re

@app.context_processor
def text_processing():
    def trim(text):
        """function used to trim blog text in templates"""
        if len(text) > 100:
            text = text[100:].rstrip()
            text = re.sub('\W$','',text)
            text = text + '...'
            return text
        else:
            return text
    return dict(trim=trim)