from wtforms import Form, StringField, validators, PasswordField


class SignUpForm(Form):
    username = StringField('Username', [validators.DataRequired(), validators.Length(min=3, max=25)])
    password = PasswordField('New Password', [validators.DataRequired(),
                                              validators.EqualTo('confirm', message='passwords must match')])
    confirm = PasswordField('Repeat password')


class SignInForm(Form):
    username = StringField('Username', [validators.DataRequired(), validators.Length(min=3, max=25)])
    password = PasswordField('Password', [validators.DataRequired()])
