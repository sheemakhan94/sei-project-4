from datetime import datetime
from app import db, ma
from marshmallow import fields
from .base import BaseModel, BaseSchema
# pylint: disable=W0611
from .user import User, UserSchema



class Entry(db.Model, BaseModel):

    __tablename__ = 'entries'

    date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    what = db.Column(db.Text, nullable=False)
    image = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User', backref="user_entries")

class EntrySchema(ma.ModelSchema, BaseSchema):

    user = fields.Nested('UserSchema', only=('id', 'username'))
    date = fields.DateTime(format='%Y-%m-%d')


    class Meta:
        model = Entry
