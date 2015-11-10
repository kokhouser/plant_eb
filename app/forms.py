from flask.ext.wtf import Form
from app import models
from models import User
from wtforms.fields import StringField, BooleanField, PasswordField, SubmitField
from wtforms.validators import Required

class LoginForm(Form):
    username = StringField('Username', validators=[Required("Please enter your username.")])
    password = PasswordField('Password', validators=[Required("Please enter your password.")])
    submit = SubmitField("Login")

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        self.user = None

    def validate(self):
        rv = Form.validate(self)
        if not rv:
            return False

        user = User.query.filter_by(
            nickname=self.username.data).first()
        if user is None:
            self.username.errors.append('Unknown username')
            return False

        if not (user.password==self.password.data):
            self.password.errors.append('Invalid password')
            return False

        self.user = user
        return True
