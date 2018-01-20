from wtforms import Form, StringField, validators
from wtforms.widgets import TextArea


class NewBlogForm(Form):
    blog_title = StringField('title',
                             [validators.DataRequired(message='You should provide a great title for your blog')])
    blog_text = StringField('blog',
                            [validators.DataRequired(message='You must write something before you can post your blog')],
                            widget=TextArea())