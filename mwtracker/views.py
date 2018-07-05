
"""Views for app."""

from flask import (redirect,
                   render_template,
                   url_for,
                  )

from . import app, db
from .models import Event, Kind
from .forms import AddForm

@app.route('/')
def index():
    return render_template('main.html',
						   title='Events',
						   kinds=[(row.id, row.name) for row in Kind.query.all()]
					 	  )
