# coding: utf-8
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from wtforms import ValidationError

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(message=u"用户名不能为空")])
    password = PasswordField('Password', validators=[DataRequired(message=u"密码不能为空")])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('LOG IN')

