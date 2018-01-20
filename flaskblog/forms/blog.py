from wtforms import Form, StringField, validators
from wtforms.widgets import TextArea


class NewBlogForm(Form):
    blog_title = StringField('title',
                             [validators.DataRequired(message='Did you forget the title?')],
                             render_kw={"placeholder": 'Title'})
    blog_text = StringField('blog',
                            [validators.DataRequired(message='Did you forget to write your blog post?')],
                            widget=TextArea(),
                            render_kw={"placeholder": 'Write your story'})