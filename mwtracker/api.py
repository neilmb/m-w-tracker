
import datetime
import json

from flask import (Blueprint,
                   current_app,
                   jsonify,
                   make_response,
                   request
                   )
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

@api.route('/event/<int:event_id>', methods=['GET', 'DELETE'])
def event(event_id):
    """Delete an event from the database."""
    if request.method == 'DELETE':
        return _delete(event_id)
    event = db.session.query(Event).filter_by(id=event_id).first()
    return jsonify(event.to_dict())


def _default_encoder(obj):
    """JSON encoder function for SQLAlchemy special classes."""
    if isinstance(obj, datetime.datetime):
        return obj.isoformat()


@api.route('/', methods=['GET', 'POST'])
def events():
    if request.method == 'GET':
        current_app.logger.info('Got request to list events')
        events = (db.session.query(Event.time, Event.comment, Event.id)
                .join(Kind).add_columns(Kind.name)
                .order_by(Event.time.desc())
                )
        def _create_dict(r):
            return {c.get('name'): getattr(r, c.get('name')) for c in events.column_descriptions}
        return json.dumps([_create_dict(row) for row in events], default=_default_encoder)
    else:
        return create_event()

def create_event():
    current_app.logger.info('Got request to create event')
    data = json.loads(request.data)
    new_event = Event(kind_id=data['kind'],
                      time=data['time'],
                      comment=data['comment'])
    db.session.add(new_event)
    db.session.commit()
    db.session.refresh(new_event)

    resp = make_response(json.dumps({'id': new_event.id}))
    resp.headers['Location'] = '/event/{}'.format(new_event.id)
    return resp


@api.route('/kinds', methods=['GET'])
def kinds():
    current_app.logger.info('Got request to list kinds')
    return jsonify([(row.id, row.name) for row in Kind.query.all()])
