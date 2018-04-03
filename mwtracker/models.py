"""SQLAlchemy models for MyAstroBase."""

from mwtracker import db

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.DateTime)
    kind_id = db.Column(db.Integer, db.ForeignKey('kind.id'))
    comment = db.Column(db.String(500))

class Kind(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))

    def __repr__(self):
        return '<Kind id={} name={}>'.format(str(self.id), str(self.name))
