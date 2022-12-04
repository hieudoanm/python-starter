"""
Python - Back-end Starter
"""

import os
import uuid
from dotenv import load_dotenv
from flask import Flask, request
import psycopg2


load_dotenv()  # loads variables from .env file into environment


app = Flask(__name__)
url = os.environ.get("DATABASE_URL")


SELECT_TASKS = "SELECT * FROM public.tasks;"
CREATE_TASK = "INSERT INTO public.tasks (id, title, description, completed) VALUES ('%s', '%s', '%s', %s) RETURNING *;"
SELECT_TASK = "SELECT * FROM public.tasks WHERE id = '%s';"
UPDATE_TASK = "UPDATE public.tasks SET title = '%s', description = '%s', completed = %s WHERE id = '%s' RETURNING *;"
DELETE_TASK = "DELETE FROM public.tasks WHERE id = '%s';"


def get_connection():
    """
    Get Connection
    """
    host = os.environ.get("DB_HOST")
    port = os.environ.get("DB_PORT")
    database = os.environ.get("DB_NAME")
    user = os.environ.get('DB_USER')
    password = os.environ.get('DB_PASS')
    print(host, port, database, user, password)
    return psycopg2.connect(host=host,
                            port=port,
                            database=database,
                            user=user,
                            password=password)


pre_connection = get_connection()
pre_cursor = pre_connection.cursor()
pre_cursor.execute("DROP TABLE IF EXISTS public.tasks;")
pre_cursor.execute("""CREATE TABLE IF NOT EXISTS public.tasks (
    id          TEXT PRIMARY KEY,
    title       TEXT DEFAULT '',
    description TEXT DEFAULT '',
    completed   BOOLEAN DEFAULT false
);""")
pre_cursor.close()
pre_connection.close()


@ app.route("/tasks", methods=['GET', 'POST'])
def handle_tasks():
    """
    Handle Tasks
    """
    connection = get_connection()
    cursor = connection.cursor()
    if request.method == 'GET':
        cursor.execute(SELECT_TASKS)
        rows = cursor.fetchall()
        tasks = list(map(lambda columns: {
            "id": columns[0],
            "title": columns[1],
            "description": columns[2],
            "completed": columns[3],
        }, rows))
        cursor.close()
        connection.close()
        return tasks
    elif request.method == "POST":
        new_id = str(uuid.uuid4())
        data = request.get_json()
        title = data.get('title', '')
        description = data.get('description', '')
        completed = bool(data.get('completed', False))
        print(new_id, title, description, completed)
        CREATE_TASK_QUERY = CREATE_TASK % (
            new_id, title, description, completed)
        print(CREATE_TASK_QUERY)
        cursor.execute(CREATE_TASK_QUERY)
        connection.commit()
        [columns] = cursor.fetchall()
        new_title = columns[1]
        new_description = columns[2]
        new_completed = columns[3]
        cursor.close()
        connection.close()
        return {
            "id": new_id,
            "title": new_title,
            "description": new_description,
            "completed": new_completed,
        }


@ app.route("/tasks/<string:task_id>", methods=['GET', 'PUT', 'DELETE'])
def handle_task(task_id):
    """
    Handle Task
    """
    connection = get_connection()
    cursor = connection.cursor()
    if request.method == 'GET':
        SELECT_TASK_QUERY = SELECT_TASK % (task_id)
        cursor.execute(SELECT_TASK_QUERY)
        [columns] = cursor.fetchall()
        task_id = columns[0]
        title = columns[1]
        description = columns[2]
        completed = columns[3]
        cursor.close()
        connection.close()
        return {
            "id": task_id,
            "title": title,
            "description": description,
            "completed": completed
        }
    elif request.method == "PUT":
        data = request.get_json()
        title = data.get('title', '')
        description = data.get('description', '')
        completed = bool(data.get('completed', False))
        print(task_id, title, description, completed)
        UPDATE_TASK_QUERY = UPDATE_TASK % (
            title, description, completed, task_id)
        print(UPDATE_TASK_QUERY)
        cursor.execute(UPDATE_TASK_QUERY)
        connection.commit()
        [columns] = cursor.fetchall()
        new_title = columns[1]
        new_description = columns[2]
        new_completed = columns[3]
        cursor.close()
        connection.close()
        return {
            "id": task_id,
            "title": new_title,
            "description": new_description,
            "completed": new_completed,
        }
    elif request.method == "DELETE":
        DELETE_TASK_QUERY = DELETE_TASK % (task_id)
        print(DELETE_TASK_QUERY)
        cursor.execute(DELETE_TASK_QUERY)
        connection.commit()
        cursor.close()
        connection.close()
        return {}


if __name__ == "__main__":
    PORT = 8080
    app.run(debug=True, port=PORT)
