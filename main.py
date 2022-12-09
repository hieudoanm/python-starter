"""
Python - Back-end Starter
"""


from flask import Flask, request
from services import get_tasks, create_task, get_task, update_task, delete_task


app = Flask(__name__)


@app.route("/tasks", methods=['GET', 'POST'])
def handle_tasks():
    """
    Handle Tasks
    """
    if request.method == 'GET':
        tasks = get_tasks()
        return tasks
    elif request.method == "POST":
        new_task = create_task(request.get_json())
        return new_task


@app.route("/tasks/<string:task_id>", methods=['GET', 'PUT', 'DELETE'])
def handle_task(task_id):
    """
    Handle Task
    """
    if request.method == 'GET':
        task = get_task(task_id)
        return task
    elif request.method == "PUT":
        updated_task = update_task(task_id, request.get_json())
        return updated_task
    elif request.method == "DELETE":
        delete_task(task_id)
        return {}


if __name__ == "__main__":
    PORT = 8080
    app.run(debug=True, port=PORT)
