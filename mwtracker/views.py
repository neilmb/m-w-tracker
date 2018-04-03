
"""Views for app."""

from flask import (escape,
                   redirect,
                   render_template,
                   request,
                   url_for,
                  )

from . import app, db
from .models import Event, Kind
from .forms import AddForm

@app.route('/')
def events():
    events = (db.session.query(Event.time, Event.comment)
              .join(Kind).add_columns(Kind.name)
              .order_by(Event.time.desc())
              .all())
    return render_template('events.html', title='Events', events=events)

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = AddForm()
    form.kind.choices = [(row.id, row.name) for row in Kind.query.all()]
    if form.validate_on_submit():
        new_event = Event(kind_id=form.kind.data,
                          time=form.time.data,
                          comment=form.comment.data)
        db.session.add(new_event)
        db.session.commit()
        return redirect(url_for('events'))
    return render_template('add.html', title='Add Event', form=form)
