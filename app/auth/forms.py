from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError,IntegerField,HiddenField
from wtforms.validators import DataRequired, Email, EqualTo, URL

from ..models import User

class RegistrationForm(FlaskForm):
    """
    Form for users to create new account
    """
    username = StringField('Username', validators=[DataRequired()])
    flat_num = StringField('Flat Number', validators=[DataRequired()])
    door_num = StringField('Locality', validators=[DataRequired()])
    webcamurl = StringField('WebCamera URL', validators=[DataRequired(), URL()])
    location = StringField('Enter the location', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(),EqualTo('confirm_password')])
    confirm_password = PasswordField('Confirm Password')
    contact = IntegerField('Phone Number', validators=[DataRequired()])
    latitude = HiddenField('latitude')
    longitude = HiddenField()
    submit = SubmitField('Register')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username is already in use.')

class LoginForm(FlaskForm):
    """
    Form for users to login
    """
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
	