
from routes.users import user_router
from routes.auth import auth_router
from fastapi import FastAPI, Body, Query, Request, HTTPException, Depends, Path
from fastapi.responses import HTMLResponse, JSONResponse
from typing import Optional, List
from utils.jwt_manager import create_token, decode_token
from fastapi.security import HTTPBearer
from schemas.schemas import UsersBase
from config.dbconnection import Base, engine, session
from models.models import Users as UsersModel
from fastapi.encoders import jsonable_encoder
from routes.auth import auth_router
from routes.cart import cart_router
from routes.inventory import inventory_router
from routes.order import order_router
from middlewares.jwt_bearer import JWTBearer
from middlewares.error_handler import ErrorHandler
from routes.products import products_router
from fastapi.middleware.cors import CORSMiddleware

# Create FastAPI instance
app = FastAPI()

app.title = "CapClocks API"

# Include routers
app.add_middleware(ErrorHandler)
app.include_router(products_router)
app.include_router(user_router)
app.include_router(cart_router)
app.include_router(auth_router)
app.include_router(inventory_router)
app.include_router(order_router)

Base.metadata.create_all(bind=engine)

# Configurar los orígenes permitidos para CORS
origins = [
    "http://localhost",
    "http://localhost:4200",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware, 
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", tags=["root"])
async def read_root():
    return "Bienvenido a CapClocks Api"
