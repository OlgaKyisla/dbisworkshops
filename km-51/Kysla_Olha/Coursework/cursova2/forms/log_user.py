from flask_wtf import Form
from wtforms import StringField, SubmitField,  PasswordField
from wtforms import validators


class LogForm(Form):

   password = PasswordField("Password:", [
                                             validators.DataRequired("Please enter your password."),
                                             validators.Length(3, 20, "Password should be from 3 to 20 symbols.")
                                          ])
   email = StringField("Email: ", [
                                 validators.DataRequired("Please enter your name."),
                                 validators.Email("Wrong email format")
                                 ])
   submit = SubmitField("Login")
