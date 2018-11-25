from flask_wtf import Form
from wtforms import StringField, FileField, SubmitField

class upForm(Form):
    file = FileField('file')
    submit = SubmitField('submit')