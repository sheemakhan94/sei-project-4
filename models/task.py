from datetime import datetime
from app import db, ma
from marshmallow import fields
from .base import BaseModel, BaseSchema
# pylint: disable=W0611
from .user import User, UserSchema
from .task_component import Component

task_components = db.Table(
    'task_components',
    db.Column('task_id', db.Integer, db.ForeignKey('tasks.id')),
    db.Column('component_id', db.Integer, db.ForeignKey('components.id'))
)

class Task(db.Model, BaseModel):

    __tablename__ = 'tasks'

    to_do = db.Column(db.String(40), nullable=False)
    components = db.relationship('Component', secondary=task_components, backref='tasks')
    due_date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    # Next two lines
    user_id = db.Column(db.Integer, db.ForeignKey('user_journals.id'), nullable=False)
    user = db.relationship('User', backref="user_tasks")

class TaskSchema(ma.ModelSchema, BaseSchema):

    due_date = fields.DateTime(format='%Y-%m-%d %H:%M:%S')
    components = fields.Nested('ComponentSchema', many=True, exclude=('created_at', 'updated_at', 'tasks'))

    # Next 1 line
    user = fields.Nested('UserSchema', only=('id', 'username'))

    class Meta:
        model = Task
