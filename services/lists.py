"""
Lists
"""


import uuid
from libs.postgres import get_connection


SCHEMA_NAME = "public"
TABLE_NAME = "lists"
TABLE = f"{SCHEMA_NAME}.{TABLE_NAME}"


SELECT_LISTS = "SELECT * FROM public.lists;"
CREATE_LIST = "INSERT INTO public.lists (id, title, description, user_id) VALUES ('%s', '%s', '%s', '%s') RETURNING *;"
SELECT_LIST = "SELECT * FROM public.lists WHERE id = '%s';"
UPDATE_LIST = "UPDATE public.lists SET title = '%s', description = '%s', user_id = '%s' WHERE id = '%s' RETURNING *;"
DELETE_LIST = "DELETE FROM public.lists WHERE id = '%s';"


def get_lists():
    """
    Get Lists
    """
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(SELECT_LISTS)
    rows = cursor.fetchall()
    lists = list(map(lambda columns: {
        "id": columns[0],
        "title": columns[1],
        "description": columns[2],
        "user_id": columns[3]
    }, rows))
    cursor.close()
    connection.close()
    return lists


def create_list(list_data):
    """
    Create List
    """
    connection = get_connection()
    cursor = connection.cursor()
    new_id = str(uuid.uuid4())
    title = list_data.get('title', '')
    description = list_data.get('description', '')
    user_id = list_data.get('user_id', '')
    CREATE_LIST_QUERY = CREATE_LIST % (
        new_id, title, description, user_id)
    cursor.execute(CREATE_LIST_QUERY)
    connection.commit()
    [columns] = cursor.fetchall()
    new_title = columns[1]
    new_description = columns[2]
    new_user_id = columns[3]
    cursor.close()
    connection.close()
    return {
        "id": new_id,
        "title": new_title,
        "description": new_description,
        "user_id": new_user_id
    }


def get_list(list_id):
    """
    Get List
    """
    connection = get_connection()
    cursor = connection.cursor()
    SELECT_LIST_QUERY = SELECT_LIST % (list_id)
    cursor.execute(SELECT_LIST_QUERY)
    [columns] = cursor.fetchall()
    list_id = columns[0]
    title = columns[1]
    description = columns[2]
    user_id = columns[3]
    cursor.close()
    connection.close()
    return {
        "id": list_id,
        "title": title,
        "description": description,
        "user_id": user_id
    }


def update_list(list_id, list_data):
    """
    Update List
    """
    connection = get_connection()
    cursor = connection.cursor()
    title = list_data.get('title', '')
    description = list_data.get('description', '')
    user_id = list_data.get('user_id', '')
    UPDATE_LIST_QUERY = UPDATE_LIST % (
        title, description, user_id, list_id)
    cursor.execute(UPDATE_LIST_QUERY)
    connection.commit()
    [columns] = cursor.fetchall()
    updated_title = columns[1]
    updated_description = columns[2]
    updated_user_id = columns[3]
    cursor.close()
    connection.close()
    return {
        "id": list_id,
        "title": updated_title,
        "description": updated_description,
        "user_id": updated_user_id
    }


def delete_list(list_id):
    """
    Delete List
    """
    connection = get_connection()
    cursor = connection.cursor()
    DELETE_LIST_QUERY = DELETE_LIST % (list_id)
    cursor.execute(DELETE_LIST_QUERY)
    connection.commit()
    cursor.close()
    connection.close()
    return {}
