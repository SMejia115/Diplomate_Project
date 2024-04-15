from fastapi import APIRouter, Depends, Path, Query
from fastapi.responses import JSONResponse
from typing import List
from config.dbconnection import sessionlocal
from models.models import Products as ProductModel
from fastapi.encoders import jsonable_encoder
from schemas.schemas import Product as ProductSchema


products_router = APIRouter()

@products_router.get("/products", tags=['products'], response_model=List[ProductSchema], status_code=200)
def get_recommender():
    db = sessionlocal()
    result = db.query(ProductModel).all()
    db.close()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))