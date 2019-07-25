from datetime import datetime
from app import db, ma
from marshmallow import fields
from .base import BaseModel, BaseSchema
# pylint: disable=W0611
from .user import User, UserSchema


class Event(db.Model, BaseModel):

    __tablename__ = 'events'

    event_name = db.Column(db.String(40), nullable=False)
    event_date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    event_location = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user_journals.id'), nullable=False)
    user = db.relationship('User', backref="user_events")


class EventSchema(ma.ModelSchema, BaseSchema):

    event_date = fields.DateTime(format='%Y-%m-%d %H:%M:%S')
    user = fields.Nested('UserSchema', only=('id', 'username'))

    class Meta:
        model = Event
