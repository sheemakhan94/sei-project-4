from flask import Blueprint, jsonify, request, g
from models.event import Event, EventSchema
from lib.secure_route import secure_route

api = Blueprint('events', __name__)
event_schema = EventSchema()

@api.route('/events', methods=['GET'])
def index():
    events = Event.query.all()
    return event_schema.jsonify(events, many=True), 200

@api.route('/events/<int:event_id>', methods=['GET'])
def show(event_id):
    event = Event.query.get(event_id)
    if not event:
        return jsonify({'message': 'not found'}), 404
    return event_schema.jsonify(event), 200


@api.route('/events', methods=['POST'])
@secure_route
def create():
    data = request.get_json()
    event, errors = event_schema.load(data)
    if errors:
        return jsonify(errors), 422
    event.user = g.current_user
    event.save()
    return event_schema.jsonify(event), 201

@api.route('/events/<int:event_id>', methods=['PUT'])
def update(event_id):
    event = Event.query.get(event_id)
    if not event:
        return jsonify({'message': 'not found'}), 404
    data = request.get_json()
    event, errors = event_schema.load(data, instance=event, partial=True)
    if errors:
        return jsonify(errors), 422
    event.save()
    return event_schema.jsonify(event), 202

@api.route('/events/<int:event_id>', methods=['DELETE'])
def delete(event_id):
    event = Event.query.get(event_id)
    if not event:
        return jsonify({'message': 'Not Found'}), 404
    event.remove()
    return '', 204
