from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField, SubmitField, SelectField, IntegerField)
from wtforms.validators import Required

class AddPitch(FlaskForm):
    comment = StringField("Waiting for your pitch !")
    category = SelectField(u'Category', choices=[('Sports', 'Sports'), 
                                                ('Tech', 'Tech'),
                                                ('Music', 'Music'),
                                                ('Other', 'Other') ])
    submit = SubmitField('Add Pitch')

class DelPitch(FlaskForm):
     id = IntegerField("ID number of pitch you would like to delete")
     submit = SubmitField("Remove Pitch")

class UpdateProfile(FlaskForm):
    bio = TextAreaField("Tell us about yourself")
    submit = SubmitField("Update")