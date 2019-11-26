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
     id = IntegerField("ID number of pitch you would like to delete " )
     submit = SubmitField("Remove Pitch")

class FeedbackForm(FlaskForm):
    feedback = TextAreaField("Don't be shy ! This is a free space...")
    submit = SubmitField("Submit Comment")

