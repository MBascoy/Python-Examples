
from app.controllers.tasks_controller import create_task, get_tasks


def include_routers(app):
    
    app.route('/tasks', methods=['POST'])(create_task)
    app.route('/tasks', methods=['GET'])(get_tasks)