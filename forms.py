from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    # username field + parameters
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    #email field + paramaters
    password = PasswordField('Password', validators=[DataRequired()])
    # password field + parameters
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    #confirm password matches password
    submit = SubmitField('Sign Up')
    # sign up


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    # email field
    password = PasswordField('Password', validators=[DataRequired()])
    # password field
    remember = BooleanField('Remember Me')
    # remember me checkbox
    submit = SubmitField('Login')
    # login button 