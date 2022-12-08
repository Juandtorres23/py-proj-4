from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class TeamForm(FlaskForm):
    team_name = StringField("team name")
    submit = SubmitField("submit")