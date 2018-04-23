
import datetime
import json

from flask import Blueprint, redirect
from sqlalchemy.orm.exc import NoResultFound


from . import db
from .models import Event, Kind

api = Blueprint('api', __name__)

def _delete(event_id):
    try:
        this_event = Event.query.filter(Event.id == event_id).one()
    except NoResultFound:
        return('"Event {} not found."'.format(event_id), 404)
    db.session.delete(this_event)
    db.session.commit()
    return ('', 204)


@api.route('/event/<int:event_id>', methods=['DELETE'])
def delete(event_id):
    """Delete an event from the database."""
    return _delete(event_id)


@api.route('/delete/<int:event_id>')
def delete_get(event_id):
    return _delete(event_id)


def _default_encoder(obj):
    """JSON encoder function for SQLAlchemy special classes."""
    if isinstance(obj, datetime.datetime):
        return obj.isoformat()


@api.route('/')
def events():
    events = (db.session.query(Event.time, Event.comment, Event.id)
              .join(Kind).add_columns(Kind.name)
              .order_by(Event.time.desc())
              )
    def _create_dict(r):
        return {c.get('name'): getattr(r, c.get('name')) for c in events.column_descriptions}
    return json.dumps([_create_dict(row) for row in events], default=_default_encoder)
