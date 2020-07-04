from flask_wtf import FlaskForm, RecaptchaField
from wtforms import (StringField,
                     TextField,
                     TextAreaField,
                     SubmitField,
                     PasswordField,
                     DateField,
                     SelectField)
from wtforms.validators import (DataRequired,
                                Email,
                                EqualTo,
                                Length,
                                URL)

class ContactForm(FlaskForm):
    """Contact form."""
    name = StringField('Name', [
        DataRequired()])
    email = StringField('Email', [
        Email(message=('Not a valid email address.')),
        DataRequired()])
    body = TextField('Message', [
        DataRequired(),
        Length(min=4, message=('Your message is too short.'))])
    recaptcha = RecaptchaField()
    submit = SubmitField('Submit')



class SignupForm(FlaskForm):
    """Sign up for a user account."""
    name = StringField('Name', [
        DataRequired()])
    email = StringField('Email', [
        Email(message='Not a valid email address.'),
        DataRequired()])
    password = PasswordField('Password', [
        DataRequired(message="Please enter a password."),
    ])
    confirmPassword = PasswordField('Repeat Password', [
            EqualTo(password, message='Passwords must match.')
            ])
    title = SelectField('Title', [DataRequired()],
                        choices=[('Interviewee', 'interviewee'),
                                 ('Interviewer', 'Interviewer')])
    time1 = DateField('Time slot 1', [
                            DataRequired()])
    time2 = DateField('Time slot 2', [
                            DataRequired()])
    time3 = DateField('Time slot 3', [
                            DataRequired()])
    #recaptcha = RecaptchaField()
    submit = SubmitField('Submit')