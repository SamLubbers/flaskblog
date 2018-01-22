from wtforms import Form, StringField, validators, PasswordField

class SignUp(Form):
    username = StringField('Username', [validators.DataRequired(), validators.Length(min=3, max=25)])
    password = PasswordField('New Password', [validators.DataRequired(),
                                              validators.EqualTo('confirm', message='passwords must match')])

    confirm = PasswordField('Repeat password')
    