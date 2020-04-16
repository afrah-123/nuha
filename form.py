from flask_wtf import FlaskForm
from wtforms import TextField, TextAreaField, validators, StringField, SubmitField


class ReviewForm(FlaskForm):
   fname = StringField("Name", validators=[validators.data_required()])
   product = StringField("Name of Product", validators=[validators.data_required()])
   review = TextAreaField("Review of Product", validators=[validators.data_required()])
   submit = SubmitField('submit')



