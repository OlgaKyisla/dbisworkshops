from flask_wtf import Form
from wtforms import StringField, SubmitField,  PasswordField

from wtforms import validators


class RegForm(Form):

   name = StringField("Name: ", [
                                    validators.DataRequired("Please enter your name."),
                                    validators.Length(3, 20, "Name should be from 3 to 20 symbols")
                                 ])

   password = PasswordField("Password:", [
                                             validators.DataRequired("Please enter your password."),
                                             validators.Length(3, 10, "Password should be from 3 to 10 symbols")
                                          ])
   email = StringField("Email: ", [
                                 validators.DataRequired("Please enter your name."),
                                 validators.Email("Wrong email format")
                                 ])
   submit = SubmitField("Registration")
