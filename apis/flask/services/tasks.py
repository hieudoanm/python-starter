"""
Tasks
"""


import uuid
from libs.postgres import get_connection


SCHEMA_NAME = "public"
TABLE_NAME = "tasks"
TABLE = f"{SCHEMA_NAME}.{TABLE_NAME}"


SELECT_TASKS = "SELECT * FROM public.tasks;"
CREATE_TASK = "INSERT INTO public.tasks (id, title, description, list_id, completed) VALUES ('%s', '%s', '%s', '%s', %s) RETURNING *;"
SELECT_TASK = "SELECT * FROM public.tasks WHERE id = '%s';"
UPDATE_TASK = "UPDATE public.tasks SET title = '%s', description = '%s', list_id = '%s', completed = %s WHERE id = '%s' RETURNING *;"
DELETE_TASK = "DELETE FROM public.tasks WHERE id = '%s';"


def get_tasks():
    """
    Get Tasks
    """
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(SELECT_TASKS)
    rows = cursor.fetchall()
    tasks = list(map(lambda columns: {
        "id": columns[0],
        "title": columns[1],
        "description": columns[2],
        "list_id": columns[3],
        "completed": columns[4],
    }, rows))
    cursor.close()
    connection.close()
    return tasks


def create_task(task):
    """
    Create Task
    """
    connection = get_connection()
    cursor = connection.cursor()
    new_id = str(uuid.uuid4())
    title = task.get('title', '')
    description = task.get('description', '')
    list_id = task.get('list_id', '')
    completed = bool(task.get('completed', False))
    CREATE_TASK_QUERY = CREATE_TASK % (
        new_id, title, description, list_id, completed)
    cursor.execute(CREATE_TASK_QUERY)
    connection.commit()
    [columns] = cursor.fetchall()
    new_title = columns[1]
    new_description = columns[2]
    new_list_id = columns[3]
    new_completed = columns[4]
    cursor.close()
    connection.close()
    return {
        "id": new_id,
        "title": new_title,
        "description": new_description,
        "list_id": new_list_id,
        "completed": new_completed
    }


def get_task(task_id):
    """
    Get Task
    """
    connection = get_connection()
    cursor = connection.cursor()
    SELECT_TASK_QUERY = SELECT_TASK % (task_id)
    cursor.execute(SELECT_TASK_QUERY)
    [columns] = cursor.fetchall()
    task_id = columns[0]
    title = columns[1]
    description = columns[2]
    list_id = columns[3]
    completed = columns[4]
    cursor.close()
    connection.close()
    return {
        "id": task_id,
        "title": title,
        "description": description,
        "list_id": list_id,
        "completed": completed
    }


def update_task(task_id, task):
    """
    Update Task
    """
    connection = get_connection()
    cursor = connection.cursor()
    title = task.get('title', '')
    description = task.get('description', '')
    list_id = task.get('list_id', '')
    completed = bool(task.get('completed', False))
    UPDATE_TASK_QUERY = UPDATE_TASK % (
        title, description, list_id, completed, task_id)
    cursor.execute(UPDATE_TASK_QUERY)
    connection.commit()
    [columns] = cursor.fetchall()
    updated_title = columns[1]
    updated_description = columns[2]
    updated_list_id = columns[3]
    updated_completed = columns[4]
    cursor.close()
    connection.close()
    return {
        "id": task_id,
        "title": updated_title,
        "description": updated_description,
        "list_id": updated_list_id,
        "completed": updated_completed
    }


def delete_task(task_id):
    """
    Delete Task
    """
    connection = get_connection()
    cursor = connection.cursor()
    DELETE_TASK_QUERY = DELETE_TASK % (task_id)
    cursor.execute(DELETE_TASK_QUERY)
    connection.commit()
    cursor.close()
    connection.close()
    return {}
