
"""Views for app."""

from flask import escape, render_template

from mwtracker import app
from .models import Event

@app.route('/')
def home():
    app_str = escape(repr(app))
    return render_template('index.html', title='Home', parameter=app_str)

@app.route('/events')
def events():
    events = Event.query.all()
    return render_template('events.html', title='Events', events=events)
