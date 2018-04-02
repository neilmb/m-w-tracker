"""SQLAlchemy models for MyAstroBase."""

from app import db

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.DateTime)
    kind = db.Column(db.String(30))
    comment = db.Column(db.String(500))
