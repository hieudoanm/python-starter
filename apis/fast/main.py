"""
FastAPI
"""


from fastapi import FastAPI


app = FastAPI(
    title="FastAPI",
    version="0.0.1",
    contact={
        "name": "Hieu Doan",
        "url": "https://hieudoanm.github.io",
        "email": "hieumdoan@gmail.com",
    }, license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT"
    }
)


@app.get("/health", tags=['Health'])
def get_health():
    """
    Get Health
    """
    return {"status": "healthy"}


@app.get("/users", tags=["Users"])
def get_users():
    """
    Get Users
    """
    return []


@app.post("/users", tags=["Users"])
def create_user():
    """
    Create User
    """
    return {}


@app.get("/users/{user_id}", tags=["Users"])
def get_user(user_id):
    """
    Get User
    """
    return {"id": user_id}


@app.put("/users/{user_id}", tags=["Users"])
def update_user(user_id):
    """
    Update User
    """
    return {"id": user_id}


@app.delete("/users/{user_id}", tags=["Users"])
def delete_user(user_id):
    """
    Delete User
    """
    return {"id": user_id}


@app.get("/lists", tags=["Lists"])
def get_lists():
    """
    Get Lists
    """
    return []


@app.post("/lists", tags=["Lists"])
def create_list():
    """
    Create list
    """
    return {}


@app.get("/lists/{list_id}", tags=["Lists"])
def get_list(list_id):
    """
    Get List
    """
    return {"id": list_id}


@app.put("/lists/{list_id}", tags=["Lists"])
def update_list(list_id):
    """
    Update List
    """
    return {"id": list_id}


@app.delete("/lists/{list_id}", tags=["Lists"])
def delete_list(list_id):
    """
    Delete List
    """
    return {"id": list_id}


@app.get("/tasks", tags=["Tasks"])
def get_tasks():
    """
    Get tasks
    """
    return []


@app.post("/tasks", tags=["Tasks"])
def create_task():
    """
    Create task
    """
    return {}


@app.get("/tasks/{task_id}", tags=["Tasks"])
def get_task(task_id):
    """
    Get task
    """
    return {"id": task_id}


@app.put("/tasks/{task_id}", tags=["Tasks"])
def update_task(task_id):
    """
    Update Task
    """
    return {"id": task_id}


@app.delete("/tasks/{task_id}", tags=["Tasks"])
def delete_task(task_id):
    """
    Delete Task
    """
    return {"id": task_id}
