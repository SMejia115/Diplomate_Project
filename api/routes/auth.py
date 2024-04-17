from models.models import Users as UserModel
from schemas.schemas import UsersBase as User
from fastapi.responses import JSONResponse
from utils.jwt_manager import create_token, decode_token
from fastapi.encoders import jsonable_encoder
from config.dbconnection import session as Session
from fastapi import APIRouter, Depends, HTTPException 
from typing import Annotated
from jwt import PyJWTError

auth_router = APIRouter()

# Función para obtener un usuario por su nombre de usuario desde la base de datos
def get_user(username: str):
    db = Session()
    user = db.query(UserModel).filter(UserModel.userName == username).first()
    return user

@auth_router.post("/login")
def generate_token(username: str, password: str):
    user = get_user(username)
    if not user:
        raise HTTPException(status_code=401, detail="Usuario no encontrado")
    if password != user.password:
        raise HTTPException(status_code=401, detail="Contraseña incorrecta")
    token = create_token({"sub": user.userName})
    return {"access_token": token, "token_type": "bearer"}

@auth_router.post("/register")
def register_user(user: User):
    db = Session()
    new_user = UserModel(
        userName = user.userName,
        password = user.password,
        fullName = user.fullName,
        email = user.email,
        phone = user.phone,
        role = user.role,
        address = user.address
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return JSONResponse(content=jsonable_encoder(new_user), status_code=200)