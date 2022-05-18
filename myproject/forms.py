from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class PlayerIdForm(FlaskForm):
    player_id = StringField('Player Id', validators=[DataRequired()])
    submit = SubmitField('Submit')


class RefreshForm(FlaskForm):
    submit = SubmitField('Refresh')   