from fastapi import FastAPI, HTTPException
from typing import List
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id:int
    name:str
    e_mail:str

my_db:List[User] = []

@app.get("/users", response_model=List[User], status_code=200)
def get_all_uesrs():
    return my_db

@app.post("/users", response_model=User, status_code=201)
def create_user(user:User):
    if len(my_db) == 0:
        my_db.append(user)
        return user
    for person in my_db:
        if person.id == user.id:
            raise HTTPException(status_code=400, detail=f"User with ID {person.id} already exist!")
    my_db.append(user)
    return user

@app.put("/users/{user_id}", response_model=User, status_code=201)
def edit_user(user_id:int, updated_user:User):
    for index, user in enumerate(my_db):
        if user.id == user_id:
            my_db[index] = updated_user
            return updated_user
    raise HTTPException(status_code=404, detail=f"User with ID {user_id} not found!")

@app.delete("/users/{user_id}", status_code=204)
def delete_user(user_id:int):
    for index, user in enumerate(my_db):
        if user.id == user_id:
            del my_db[index]
            return 
    raise HTTPException(status_code=404, detail=f"User with ID {user_id} not found!")
        