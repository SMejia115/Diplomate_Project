from fastapi import APIRouter, Depends, HTTPException, Query, Path
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from config.dbconnection import session
from models.models import shoppingCart as ShoppingCartModel, Products as ProductsModel, ProductsImages as ProductsImagesModel
from schemas.schemas import ShoppingCartBase, UsersBase, ShoppingCartProducts
from middlewares.jwt_bearer import JWTBearer
from typing import List

cart_router = APIRouter()


# Get all products in the cart
@cart_router.get("/cart/{user_id}", response_model=List[ShoppingCartProducts], tags=["cart"], status_code=200)
def get_cart(user_id: int = Path(...)):
    db = session()
    try:
        # Realizar una consulta para obtener los elementos del carrito y los productos asociados
        cart_items = db.query(ShoppingCartModel).filter(ShoppingCartModel.userID == user_id).all()
        if not cart_items:
            raise HTTPException(status_code=404, detail="Shopping cart is empty")

        # Recopilar la información del carrito y los productos asociados
        cart_info = []
        for cart_item in cart_items:
            # if cart_item.cartStatus == "active":
                product = db.query(ProductsModel).filter(ProductsModel.productID == cart_item.productID).first()
                if product:
                    # Obtener las imágenes asociadas al producto
                    product_images = db.query(ProductsImagesModel).filter(ProductsImagesModel.productID == product.productID).all()
                    images = [{"ImageURL": image.imageURL} for image in product_images]
                    # Crear un diccionario con la información del carrito y el producto
                    cart_info.append({
                        "cartID": cart_item.cartID,
                        "userID": cart_item.userID,
                        "productID": cart_item.productID,
                        "quantity": cart_item.quantity,
                        "cartStatus": cart_item.cartStatus,
                        "productName": product.productName,
                        "description": product.description,
                        "price": product.price,
                        "images": images
                    })
        return JSONResponse(status_code=200, content=cart_info)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Internal Server Error")

# Add a product to the cart
@cart_router.post("/cart/newProduct/{user_id}", response_model=ShoppingCartBase, tags=["cart"], status_code=201)
def add_to_cart(user_id: int = Path(...), productID: int = Query(...), quantity: int = Query(...)):
    db = session()
    # Buscar el producto en la tabla de productos
    product = db.query(ProductsModel).filter(ProductsModel.productID == productID).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    # Verificar si el producto ya está en el carrito
    cart_item = db.query(ShoppingCartModel).filter(ShoppingCartModel.userID == user_id, ShoppingCartModel.productID == productID).first()
    if cart_item:
        if cart_item.cartStatus == "active":
            raise HTTPException(status_code=400, detail="Product already in cart")
        elif cart_item.cartStatus == "inactive":
            cart_item.cartStatus = "active"
            cart_item.quantity = quantity
            db.commit()
            db.close()
            return JSONResponse(status_code=201, content={"message": "Product added to cart"})
    # Crear un nuevo objeto de carrito
    new_cart_item = ShoppingCartModel(userID=user_id, productID=productID, quantity=quantity)
    db.add(new_cart_item)
    db.commit()
    db.close()
    return JSONResponse(status_code=201, content={"message": "Product added to cart"})

# Remove a product from the cart
@cart_router.put("/cart/remove/{user_id}/{product_id}", tags=["cart"], status_code=200)
def remove_from_cart(user_id: int = Path(...), product_id: int = Path(...)):
    db = session()
    # Buscar el producto en el carrito
    cart_item = db.query(ShoppingCartModel).filter(ShoppingCartModel.userID == user_id, ShoppingCartModel.productID == product_id).first()
    if not cart_item:
        raise HTTPException(status_code=404, detail="Product not found in the cart")
    # Eliminar el producto del carrito
    cart_item.cartStatus = "inactive"
    db.commit()
    db.close()
    return JSONResponse(status_code=200, content={"message": "Product removed from cart"})

# Update the quantity of a product in the cart
@cart_router.put("/cart/update/{user_id}/{product_id}/{quantity}", response_model=ShoppingCartBase, tags=["cart"], status_code=200)
def update_cart_item(user_id: int = Path(...), product_id: int = Path(...), quantity: int = Path(...)):
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

# Add quantity to a product in the cart
@cart_router.put("/cart/add/{user_id}/{product_id}", response_model=ShoppingCartBase, tags=["cart"], status_code=200)
def add_to_quantity(user_id: int = Path(...), product_id: int = Path(...), quantity: int = Query(...)):
    db = session()
    # Buscar el producto en el carrito
    cart_item = db.query(ShoppingCartModel).filter(ShoppingCartModel.userID == user_id, ShoppingCartModel.productID == product_id).first()
    if not cart_item:
        raise HTTPException(status_code=404, detail="Product not found in the cart")
    # Añadir la cantidad al producto
    cart_item.quantity += quantity
    db.commit()
    db.close()
    return JSONResponse(status_code=200, content={"message": "Quantity added to product"})

# Rest quantity to a product in the cart
@cart_router.put("/cart/rest/{user_id}/{product_id}", response_model=ShoppingCartBase, tags=["cart"], status_code=200)
def rest_to_quantity(user_id: int = Path(...), product_id: int = Path(...), quantity: int = Query(...)):
    db = session()
    # Buscar el producto en el carrito
    cart_item = db.query(ShoppingCartModel).filter(ShoppingCartModel.userID == user_id, ShoppingCartModel.productID == product_id).first()
    if not cart_item:
        raise HTTPException(status_code=404, detail="Product not found in the cart")
    # Restar la cantidad al producto
    cart_item.quantity -= quantity
    db.commit()
    db.close()
    return JSONResponse(status_code=200, content={"message": "Quantity rest to product"})

# Change the carStatus
@cart_router.put("/cart/status/{user_id}", response_model=ShoppingCartBase, tags=["cart"], status_code=200)
def change_cart_status(user_id: int = Path(...), status: str = Query(...)):
    db = session()
    # Buscar el carrito del usuario
    cart = db.query(ShoppingCartModel).filter(ShoppingCartModel.userID == user_id).all()
    if not cart:
        raise HTTPException(status_code=404, detail="Shopping cart not found")
    # Cambiar el estado del carrito
    for item in cart:
        item.cartStatus = status
    db.commit()
    db.close()
    return JSONResponse(status_code=200, content={"message": "Cart status changed"})

# Change all status to cancelled
@cart_router.put("/cart/cancel/{user_id}", response_model=ShoppingCartBase, tags=["cart"], status_code=200)
def cancel_cart(user_id: int = Path(...)):
    db = session()
    # Buscar el carrito del usuario
    cart = db.query(ShoppingCartModel).filter(ShoppingCartModel.userID == user_id).all()
    if not cart:
        raise HTTPException(status_code=404, detail="Shopping cart not found")
    # Cambiar el estado del carrito
    for item in cart:
        if item.cartStatus == "active":
            item.cartStatus = "cancelled"
    db.commit()
    db.close()
    return JSONResponse(status_code=200, content={"message": "Cart cancelled"})