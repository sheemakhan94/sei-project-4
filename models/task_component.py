from app import db, ma
from .base import BaseModel, BaseSchema

class Component(db.Model, BaseModel):

    __tablename__ = 'components'

    step = db.Column(db.String(128))

class ComponentSchema(ma.ModelSchema, BaseSchema):

    class Meta:
        model = Component
