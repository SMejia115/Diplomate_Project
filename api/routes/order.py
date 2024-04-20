from fastapi import APIRouter, Depends, HTTPException, Query, Path
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from config.dbconnection import session
from models.models import shoppingCart as ShoppingCartModel, Products as ProductsModel
from schemas.schemas import ShoppingCartBase, UsersBase
from models.models import Orders as OrdersModel
from schemas.schemas import OrdersBase
from middlewares.jwt_bearer import JWTBearer
from typing import List
from datetime import datetime

order_router = APIRouter()

# Create Order
@order_router.post("/order", tags=['order'], response_model=OrdersBase, status_code=200)
def create_order(user_id: int = Query(...), order_status: str = Query(...), total_price: float = Query(...), shipping_addres: str = Query(...)):
    db = session()
    try:
        # Get all products in the cart
        cart_items = db.query(ShoppingCartModel).filter(ShoppingCartModel.userID == user_id).all()
        if not cart_items:
            return JSONResponse(status_code=404, content={"message": "Shopping cart is empty"})
        # Get the current date
        order_date = datetime.now()
        # Create a new order
        new_order = OrdersModel(userID=user_id, orderDate=order_date, orderStatus=order_status, totalPrice=total_price, shippingAddress=shipping_addres)
        db.add(new_order)
        db.commit()
        db.close()
        return JSONResponse(status_code=201, content={"message": "Order created successfully"})
    except Exception as e:
        print(e)
        return JSONResponse(status_code=500, content={"message": "Internal Server Error"})
    
# Get all orders
@order_router.get("/orders", tags=['order'], response_model=List[OrdersBase], status_code=200)
def get_orders():
    db = session()
    try:
        orders = db.query(OrdersModel).all()
        if not orders:
            return JSONResponse(status_code=404, content={"message": "No orders found"})
        return JSONResponse(status_code=200, content=jsonable_encoder(orders))
    except Exception as e:
        print(e)
        return JSONResponse(status_code=500, content={"message": "Internal Server Error"})
    
# Get order by ID
@order_router.get("/order/{order_id}", tags=['order'], response_model=OrdersBase, status_code=200)
def get_order(order_id: int = Path(...)):
    db = session()
    try:
        order = db.query(OrdersModel).filter(OrdersModel.orderID == order_id).first()
        if not order:
            return JSONResponse(status_code=404, content={"message": "Order not found"})
        return JSONResponse(status_code=200, content=jsonable_encoder(order))
    except Exception as e:
        print(e)
        return JSONResponse(status_code=500, content={"message": "Internal Server Error"})
    
#get products by order
@order_router.get("/order/{order_id}/products", tags=['order'], response_model=List[ShoppingCartBase], status_code=200)
def get_products_by_order(order_id: int = Path(...)):
    db = session()
    try:
        user_id = db.query(OrdersModel).filter(OrdersModel.orderID == order_id).first().userID
        cart_items = db.query(ShoppingCartModel).filter(ShoppingCartModel.userID == user_id).first().productID
        if not cart_items:
            return JSONResponse(status_code=404, content={"message": "No products found in this order"})
        return JSONResponse(status_code=200, content=jsonable_encoder(cart_items))
    except Exception as e:
        print(e)
        return JSONResponse(status_code=500, content={"message": "Internal Server Error"})

#Posible status values: pending, processing, shipped, delivered, cancelled    
# Update order status
@order_router.put("/order/{order_id}", tags=['order'], response_model=OrdersBase, status_code=200)
def update_order_status(order_id: int = Path(...), order_status: str = Query(...)):
    db = session()
    try:
        order = db.query(OrdersModel).filter(OrdersModel.orderID == order_id).first()
        if not order:
            return JSONResponse(status_code=404, content={"message": "Order not found"})
        order.orderStatus = order_status
        db.commit()
        db.close()
        return JSONResponse(status_code=200, content={"message": "Order status updated successfully"})
    except Exception as e:
        print(e)
        return JSONResponse(status_code=500, content={"message": "Internal Server Error"})
    
# get order by user
@order_router.get("/order/user/{user_id}", tags=['order'], response_model=List[OrdersBase], status_code=200)
def get_order_by_user(user_id: int = Path(...)):
    db = session()
    try:
        orders = db.query(OrdersModel).filter(OrdersModel.userID == user_id).all()
        if not orders:
            return JSONResponse(status_code=404, content={"message": "No orders found for this user"})
        return JSONResponse(status_code=200, content=jsonable_encoder(orders))
    except Exception as e:
        print(e)
        return JSONResponse(status_code=500, content={"message": "Internal Server Error"})

# Posible status values: pending, processing, shipped, delivered, cancelled
# Get order by status
@order_router.get("/order/status/{order_status}", tags=['order'], response_model=List[OrdersBase], status_code=200)
def get_order_by_status(order_status: str = Path(...)):
    db = session()
    try:
        orders = db.query(OrdersModel).filter(OrdersModel.orderStatus == order_status).all()
        if not orders:
            return JSONResponse(status_code=404, content={"message": "No orders found with this status"})
        return JSONResponse(status_code=200, content=jsonable_encoder(orders))
    except Exception as e:
        print(e)
        return JSONResponse(status_code=500, content={"message": "Internal Server Error"})