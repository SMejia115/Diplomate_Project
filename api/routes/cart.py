from fastapi import APIRouter, Depends, HTTPException, Query, Path
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from config.dbconnection import session
from models.models import shoppingCart as ShoppingCartModel, Products as ProductsModel
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

# Add a product to the cart
@cart_router.post("/cart/{user_id}", response_model=ShoppingCartBase, tags=["cart"], status_code=201)
def add_to_cart(user_id: int = Path(...), productID: int = Query(...), quantity: int = Query(...)):
    db = session()
    # Buscar el producto en la tabla de productos
    product = db.query(ProductsModel).filter(ProductsModel.productID == productID).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    # Verificar si el producto ya está en el carrito
    cart_item = db.query(ShoppingCartModel).filter(ShoppingCartModel.userID == user_id, ShoppingCartModel.productID == productID).first()
    if cart_item:
        raise HTTPException(status_code=400, detail="Product already in cart")
    # Crear un nuevo objeto de carrito
    new_cart_item = ShoppingCartModel(userID=user_id, productID=productID, quantity=quantity)
    db.add(new_cart_item)
    db.commit()
    db.close()
    return JSONResponse(status_code=201, content=jsonable_encoder(new_cart_item))

# Remove a product from the cart
@cart_router.delete("/cart/{user_id}/{product_id}", tags=["cart"], status_code=200)
def remove_from_cart(user_id: int = Path(...), product_id: int = Path(...)):
    db = session()
    # Buscar el producto en el carrito
    cart_item = db.query(ShoppingCartModel).filter(ShoppingCartModel.userID == user_id, ShoppingCartModel.productID == product_id).first()
    if not cart_item:
        raise HTTPException(status_code=404, detail="Product not found in the cart")
    # Eliminar el producto del carrito
    db.delete(cart_item)
    db.commit()
    db.close()
    return JSONResponse(status_code=200, content={"message": "Product removed from cart"})

# Update the quantity of a product in the cart
@cart_router.put("/cart/{user_id}/{product_id}", response_model=ShoppingCartBase, tags=["cart"], status_code=200)
def update_cart_item(user_id: int = Path(...), product_id: int = Path(...), quantity: int = Query(...)):
    db = session()
    # Buscar el producto en el carrito
    cart_item = db.query(ShoppingCartModel).filter(ShoppingCartModel.userID == user_id, ShoppingCartModel.productID == product_id).first()
    if not cart_item:
        raise HTTPException(status_code=404, detail="Product not found in the cart")
    # Actualizar la cantidad del producto
    cart_item.quantity = quantity
    db.commit()
    db.close()
    return JSONResponse(status_code=200, content={"message": "Product quantity updated"})