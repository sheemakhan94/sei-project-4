from app import db, ma
from marshmallow import fields
from .base import BaseModel, BaseSchema
# pylint: disable=W0611
from .user import User, UserSchema



class Entry(db.Model, BaseModel):

    __tablename__ = 'entries'

    title = db.Column(db.String(40), nullable=False)
    what = db.Column(db.Text, nullable=False)
    where = db.Column(db.String(40), nullable=False)
    feeling = db.Column(db.String(40), nullable=False)
    significance = db.Column(db.Integer, nullable=False)
    image = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user_journals.id'), nullable=False)
    user = db.relationship('User', backref="user_entries")

class EntrySchema(ma.ModelSchema, BaseSchema):

    user = fields.Nested('UserSchema', only=('id', 'username'))

    class Meta:
        model = Entry
