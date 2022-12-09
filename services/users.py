"""
Users
"""


import uuid
from libs.postgres import get_connection


SCHEMA_NAME = "public"
TABLE_NAME = "users"
TABLE = f"{SCHEMA_NAME}.{TABLE_NAME}"


SELECT_USERS = "SELECT * FROM public.users;"
CREATE_USER = "INSERT INTO public.users (id, username, password) VALUES ('%s', '%s', '%s') RETURNING *;"
SELECT_USER = "SELECT * FROM public.users WHERE id = '%s';"
UPDATE_USER = "UPDATE public.users SET username = '%s', password = '%s' WHERE id = '%s' RETURNING *;"
DELETE_USER = "DELETE FROM public.users WHERE id = '%s';"


def get_users():
    """
    Get Users
    """
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(SELECT_USERS)
    rows = cursor.fetchall()
    users = list(map(lambda columns: {
        "id": columns[0],
        "username": columns[1],
        "password": columns[2],
    }, rows))
    cursor.close()
    connection.close()
    return users


def create_user(user):
    """
    Create User
    """
    connection = get_connection()
    cursor = connection.cursor()
    new_id = str(uuid.uuid4())
    username = user.get('username', '')
    password = user.get('password', '')
    CREATE_USER_QUERY = CREATE_USER % (
        new_id, username, password)
    cursor.execute(CREATE_USER_QUERY)
    connection.commit()
    [columns] = cursor.fetchall()
    new_username = columns[1]
    new_password = columns[2]
    cursor.close()
    connection.close()
    return {
        "id": new_id,
        "username": new_username,
        "password": new_password
    }


def get_user(user_id):
    """
    Get User
    """
    connection = get_connection()
    cursor = connection.cursor()
    SELECT_USER_QUERY = SELECT_USER % (user_id)
    cursor.execute(SELECT_USER_QUERY)
    [columns] = cursor.fetchall()
    user_id = columns[0]
    username = columns[1]
    password = columns[2]
    cursor.close()
    connection.close()
    return {
        "id": user_id,
        "username": username,
        "password": password
    }


def update_user(user_id, user):
    """
    Update User
    """
    connection = get_connection()
    cursor = connection.cursor()
    username = user.get('username', '')
    password = user.get('password', '')
    UPDATE_USER_QUERY = UPDATE_USER % (
        username, password, user_id)
    cursor.execute(UPDATE_USER_QUERY)
    connection.commit()
    [columns] = cursor.fetchall()
    updated_username = columns[1]
    updated_password = columns[2]
    cursor.close()
    connection.close()
    return {
        "id": user_id,
        "username": updated_username,
        "password": updated_password
    }


def delete_user(user_id):
    """
    Delete User
    """
    connection = get_connection()
    cursor = connection.cursor()
    DELETE_USER_QUERY = DELETE_USER % (user_id)
    cursor.execute(DELETE_USER_QUERY)
    connection.commit()
    cursor.close()
    connection.close()
    return {}
