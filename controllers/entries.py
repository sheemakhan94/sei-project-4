from flask import Blueprint, jsonify, request, g
from models.entry import Entry, EntrySchema
from lib.secure_route import secure_route


api = Blueprint('entries', __name__)
entry_schema = EntrySchema()

@api.route('/entries', methods=['GET'])
def index():
    entries = Entry.query.all()
    return entry_schema.jsonify(entries, many=True), 200

@api.route('/entries/<int:entry_id>', methods=['GET'])
def show(entry_id):
    entry = Entry.query.get(entry_id)
    if not entry:
        return jsonify({'message': 'not found'}), 404
    return entry_schema.jsonify(entry), 200

@api.route('/entries', methods=['POST'])
@secure_route
def create():
    data = request.get_json()
    entry, errors = entry_schema.load(data)
    if errors:
        return jsonify(errors), 422
    entry.user = g.current_user
    entry.save()
    return entry_schema.jsonify(entry), 201

@api.route('/entries/<int:entry_id>', methods=['PUT'])
def update(entry_id):
    entry = Entry.query.get(entry_id)
    if not entry:
        return jsonify({'message': 'not found'}), 404
    data = request.get_json()
    entry, errors = entry_schema.load(data, instance=entry, partial=True)
    if errors:
        return jsonify(errors), 422
    entry.save()
    return entry_schema.jsonify(entry), 202

@api.route('/entries/<int:entry_id>', methods=['DELETE'])
def delete(entry_id):
    entry = Entry.query.get(entry_id)
    if not entry:
        return jsonify({'message': 'Not Found'}), 404
    entry.remove()
    return '', 204
