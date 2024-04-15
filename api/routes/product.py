from fastapi import APIRouter,Path
from fastapi.responses import JSONResponse
from config.dbconnection import session
from models.models import Products as ProductModel
from fastapi.encoders import jsonable_encoder
from schemas.schemas import ProductsBase as ProductSchema

product_router = APIRouter()

@product_router.get("/products/{productID}", tags=['products'], response_model=ProductSchema, status_code=200)
def get_product(productID: int = Path(...)):
    db = session()
    result = db.query(ProductModel).filter(ProductModel.productID == productID).first()
    db.close()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))