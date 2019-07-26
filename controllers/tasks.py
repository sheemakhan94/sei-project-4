from flask import Blueprint, jsonify, request, g
from models.task import Task, TaskSchema
from models.task_component import Component
from lib.secure_route import secure_route

api = Blueprint('tasks', __name__)
task_schema = TaskSchema()

@api.route('/tasks', methods=['GET'])
def index():
    tasks = Task.query.all()
    return task_schema.jsonify(tasks, many=True), 200

@api.route('/tasks/<int:task_id>', methods=['GET'])
def show(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({'message': 'not found'}), 404
    return task_schema.jsonify(task), 200

@api.route('/tasks', methods=['POST'])
@secure_route
def create():
    data = request.get_json()
    task, errors = task_schema.load(data)
    if errors:
        return jsonify(errors), 422
    components = data['component_id']
    for component in components:
        task.components.append(Component.query.get(component))
    task.user = g.current_user
    task.save()
    return task_schema.jsonify(task), 201

@api.route('/tasks/<int:task_id>', methods=['PUT'])
def update(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({'message': 'not found'}), 404
    data = request.get_json()
    task, errors = task_schema.load(data, instance=task, partial=True)
    if errors:
        return jsonify(errors), 422
    task.save()
    return task_schema.jsonify(task), 202

@api.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({'message': 'Not Found'}), 404
    task.remove()
    return '', 204
