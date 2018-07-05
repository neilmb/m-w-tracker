"""SQLAlchemy models for MyAstroBase."""

from mwtracker import db

class DictMixin(object):

    def to_dict(self):
        return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}


class Event(db.Model, DictMixin):
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.DateTime)
    kind_id = db.Column(db.Integer, db.ForeignKey('kind.id'))
    comment = db.Column(db.String(500))

class Kind(db.Model, DictMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))

    def __repr__(self):
        return '<Kind id={} name={}>'.format(str(self.id), str(self.name))
