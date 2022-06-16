
from telnetlib import STATUS
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import uvicorn

app = FastAPI()
from action import Action
A = Action

class User(BaseModel):
    ID: Optional[int]
    name: Optional[str]
    password: Optional[str]
    

class login(BaseModel):
    username: Optional[str]
    password: Optional[str]

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/add_id_password")
async def add_id_password(id,password):
    data = Action.addlogin(id,password)

@app.get("/getAll")
async def getAll():
    data = Action.SelectAll()
    return data

@app.post("/login")
async def login(user: login):
    data = Action.login(user)
    return data

@app.post("/register")
async def registers(user: User):
    data = Action.register(user)
    return data


if __name__ == "__main__":
    uvicorn.run(app, host="10.96.0.34", port=8000)