
import datetime as dt

from flask_wtf import FlaskForm
from wtforms import (DateTimeField,
                     StringField,
                     SubmitField,
                    )
from wtforms.validators import Required

class AddForm(FlaskForm):
    kind = StringField('Kind', validators=[Required()])
    time = DateTimeField('Time',
                         default=dt.datetime.utcnow(),
                         validators=[Required()])
    comment = StringField('Comment')
    submit = SubmitField('Add')

