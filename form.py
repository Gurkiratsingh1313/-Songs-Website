from wtforms import SubmitField, BooleanField, StringField, PasswordField, validators, PasswordField, validators, \
    SelectField
from flask_wtf import Form
from wtforms.validators import DataRequired


class FlaskForm(Form):
  song_name = StringField('Song Name',
                 [validators.DataRequired()])
  link = StringField('Spotify (URL)',
                 [validators.DataRequired(), validators.URL()])
  song_rating = SelectField("Song Rating", choices=["⭐️", "⭐⭐", "⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"],
                              validators=[DataRequired()])
  explicit = SelectField("Explicit", choices=["Yes", "No"],
                            validators=[DataRequired()])
  genre = SelectField("Genre", validators=[DataRequired()], choices=["Rock", "Sad", "Dancing", "Hindi certified", "Romantic", "Punjabi hit", "Chill", "Lofi", "POP", "Kpop", "Rap", "Melody", "Electronic", "Folk", "Hip hop", "Jazz", "Rock(Heavy Metal)"])
  submit = SubmitField('Submit')