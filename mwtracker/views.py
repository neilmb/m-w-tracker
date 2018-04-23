
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
    return render_template('events.html', title='Events')


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
        return redirect(url_for('index'))
    return render_template('add.html', title='Add Event', form=form)
