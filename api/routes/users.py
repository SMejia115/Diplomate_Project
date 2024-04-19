from fastapi import APIRouter, HTTPException, Path, Query, dependencies, Depends
from fastapi.responses import JSONResponse
from typing import List
from config.dbconnection import session
from models.models import Users as UsersModel
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer
from schemas.schemas import *

user_router = APIRouter()

# Create a new user
@user_router.post("/users", tags=["users"], response_model=dict, status_code=201)
def create_user(user: RegisterUserBase):
    db = session()
    new_user = UsersModel(**user.model_dump())
    db.add(new_user)
    db.commit()
    return JSONResponse(content={"message": "User created successfully"}, status_code=201)

# Get all users
@user_router.get("/users", tags=["users"], response_model=List[dict], status_code=200)
def get_users():
    db = session()
    users = db.query(UsersModel).all()
    return JSONResponse(content=jsonable_encoder(users), status_code=200)

