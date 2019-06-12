# =============================================================================
# Import Libraries
# =============================================================================
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.auth.models import User


# =============================================================================
# Functions
# =============================================================================
def duplicate_check(form, field):
    email = User.query.filter_by(user_email = field.data).first()
    if email:
        raise ValidationError('Email Already Exists')


# =============================================================================
# Create the Form
# =============================================================================
class RegistrationForm(FlaskForm):
    name = StringField('Please Enter Your Name', validators=[DataRequired(), Length(3,5, message='between 3 to 15 characters')]) #String is form label
    email = StringField('Please Enter Your Email', validators=[DataRequired(), Email(),duplicate_check])
    password = PasswordField('Please Enter Your Password', validators=[DataRequired(), Length(5), EqualTo('confirm', message='Password must match')])
    confirm = PasswordField('Please Re-Type Your Password', validators=[DataRequired()])
    submit = SubmitField('Register')
    
    
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    stay_loggedin = BooleanField('Stay Logged-in')
    submit = SubmitField('LogIn')
