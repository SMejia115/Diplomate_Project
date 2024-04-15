from fastapi import APIRouter, Depends, HTTPException, Query, Path
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from config.dbconnection import session
from models.models import shoppingCart as ShoppingCartModel
from schemas.schemas import ShoppingCartBase, UsersBase
from middlewares.jwt_bearer import JWTBearer
from typing import List

cart_router = APIRouter()


# Get all products in the cart
@cart_router.get("/cart/{user_id}", response_model=List[ShoppingCartBase], tags=["cart"], status_code=200)
def get_cart(user_id: int = Path(...)):
    db = session()
    # Buscar los elementos del carrito del usuario dado
    cart_items = db.query(ShoppingCartModel).filter(ShoppingCartModel.userID == user_id).all()
    db.close()
    if not cart_items:
        raise HTTPException(status_code=404, detail="Shopping cart is empty")
    return JSONResponse(status_code=200, content=jsonable_encoder(cart_items))