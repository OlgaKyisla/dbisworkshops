from flask_wtf import Form
from wtforms import StringField, SubmitField,  PasswordField, IntegerField
from wtforms import validators


class AdminAdd(Form):

   name = StringField("Makeup name:", [
        validators.DataRequired("Please enter Makeup name"),
        validators.Length(3, 35, "Name should be from 3 to 35 symbols.")
    ])

   price = IntegerField("Makeup price: ", [
       validators.DataRequired("Please enter Makeup price"),
        validators.NumberRange(min=0, max=10)
    ])

   quantity = IntegerField("Makeup quantity: ", [
       validators.DataRequired("Please enter Makeup quantity"),
        validators.NumberRange(min=0, max=10)
   ])

   description = StringField("Makeup description: ", [
        validators.DataRequired("Please enter Makeup description."),
        validators.Length(3, 200, "Description should be from 3 to 20 symbols.")
   ])
   submit = SubmitField("ADD MAKEUP")
