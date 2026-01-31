from enum import Enum
from fastapi import FastAPI


app = FastAPI()

from fastapi import FastAPI

app = FastAPI()

@app.post("/register")
async def register(name:str, email:str, password:str):
    return {"message": "Registered successfully"}

@app.post("/login")
async def login(email:str, password:str):
    return {"message": "Logged in"}

@app.post("/todos")
async def create_task(title: str, description: str):
    return {"title": title, "description": description}

@app.put("/todos/{id}")
async def update_task(id:int, title:str, description:str):
    return {"id": id, "title": title, "description": description}

@app.delete("/todos/{id}")
async def delete_task(id:int):
    return {"id": id}

@app.get("/todos/{id}/")
async def get_tasks(id:int, limit: int = 10):
    return {"id": id, "limit": limit}