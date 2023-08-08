 
from flask import jsonify, request
from app.models.task import Task, db

def get_tasks():
    tasks = Task.query.all()
    task_list = []
    for task in tasks:
        task_list.append({
            'id': task.id,
            'title': task.title,
            'description': task.description
        })
    return jsonify(task_list)

def create_task():
    data = request.json
    title = data.get('title')
    description = data.get('description')
    task = Task(title=title, description=description)
    db.session.add(task)
    db.session.commit()
    return jsonify({'message': 'Task created successfully'}), 201
