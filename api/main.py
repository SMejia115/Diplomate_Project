
from routes.users import user_router
from routes.auth import auth_router
from fastapi import FastAPI, Body, Query, Request, HTTPException, Depends, Path
from pydantic import BaseModel, Field
from fastapi.responses import HTMLResponse, JSONResponse
from typing import Optional, List
from utils.jwt_manager import create_token, decode_token
import jwt
import time
from fastapi.security import HTTPBearer
from schemas.schemas import UsersBase
from config.dbconnection import Base, engine, session
from models.Models import Users as UsersModel
from fastapi.encoders import jsonable_encoder
from routes.auth import auth_router
from middlewares.jwt_bearer import JWTBearer
from middlewares.error_handler import ErrorHandler

# Create FastAPI instance
app = FastAPI()

app.title = "CapClocks API"

# Include routers
app.add_middleware(ErrorHandler)
app.include_router(user_router)
app.include_router(auth_router)
Base.metadata.create_all(bind=engine)

@app.get("/", tags=["root"])
async def read_root():
    return "Bienvenido a CapClocks Api"