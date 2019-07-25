from datetime import datetime, timedelta
import jwt
from sqlalchemy.ext.hybrid import hybrid_property
from marshmallow import validates_schema, ValidationError, fields
from app import db, ma, bcrypt
from config.environment import secret
from .base import BaseModel, BaseSchema
# pylint: disable=W0611
# from .entry import Entry
# from .task import Task
# from .event import Event

# user_entries = db.Table(
#     'user_entries',
#     db.Column('user_id', db.Integer, db.ForeignKey('user_journals.id')),
#     db.Column('entry_id', db.Integer, db.ForeignKey('entries.id'))
# )

# user_tasks = db.Table(
#     'user_tasks',
#     db.Column('user_id', db.Integer, db.ForeignKey('user_journals.id')),
#     db.Column('task_id', db.Integer, db.ForeignKey('tasks.id'))
# )

# user_events = db.Table(
#     'user_events',
#     db.Column('user_id', db.Integer, db.ForeignKey('user_journals.id')),
#     db.Column('event_id', db.Integer, db.ForeignKey('events.id'))
# )

class User(db.Model, BaseModel):

    __tablename__ = 'user_journals'

    username = db.Column(db.String(40), nullable=False, unique=True)
    email = db.Column(db.String(128), nullable=False, unique=True)
    password_hash = db.Column(db.String(128), nullable=False)
    # entries = db.relationship('Entry', secondary=user_entries, backref='user_journals')
    # tasks = db.relationship('Task', secondary=user_tasks, backref='user_journals')
    # events = db.relationship('Component', secondary=user_events, backref='user_journals')

    @hybrid_property
    def password(self):
        pass

    @password.setter
    def password(self, plaintext):
        self.password_hash = bcrypt.generate_password_hash(plaintext).decode('utf-8')

    def validate_password(self, plaintext):
        return bcrypt.check_password_hash(self.password_hash, plaintext)

    def generate_token(self):
        payload = {
            'exp': datetime.utcnow() + timedelta(days=7),
            'iat': datetime.utcnow(),
            'sub': self.id
        }

        token = jwt.encode(
        payload,
        secret,
        'HS256'
        ).decode('utf-8')

        return token

class UserSchema(ma.ModelSchema, BaseSchema):

    @validates_schema
    # pylint: disable= R0201
    def check_passwords_match(self, data):
        if data.get('password') != data.get('password_confirmation'):
            raise ValidationError(
            'Passwords do not match',
            'password_confirmation'
            )

    password = fields.String(required=True)
    password_confirmation = fields.String(required=True)

    # Next 1 line
    user_entries = fields.Nested('EntrySchema', exclude=('updated_at'))
    user_tasks = fields.Nested('TaskSchema', only=('id', 'to_do', 'components', 'due_date'))
    user_events = fields.Nested('EventSchema', only=('id', 'event_name', 'event_date', 'event_location'))

    class Meta:
        model = User
        exclude = ('password_hash', )
