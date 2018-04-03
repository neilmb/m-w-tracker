
import datetime as dt

from flask_wtf import FlaskForm
from wtforms_sqlalchemy.fields import QuerySelectField
from wtforms import (DateTimeField,
                     SelectField,
                     StringField,
                     SubmitField,
                    )
from wtforms.validators import (DataRequired,
                                Required,
                               )

from . import models

class AddForm(FlaskForm):
    kind = SelectField('Kind',
                       validators=[DataRequired()],
                       coerce=int)
    time = DateTimeField('Time',
                         default=dt.datetime.utcnow(),
                         validators=[Required()])
    comment = StringField('Comment')
    submit = SubmitField('Add')

