from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

# Define the schemas for the API

class UsersBase(BaseModel):
    userID: Optional[int]
    userName: str
    password: str
    fullName: str
    email: EmailStr
    phone: Optional[str]
    role: str = 'client'
    address: Optional[str]

    class Config:
        orm_mode = True

class ProductsBase(BaseModel):
    productID: Optional[int]
    productName: str
    description: str
    price: float
    category: str

    class Config:
        orm_mode = True

class ProductsImagesBase(BaseModel):
    imageID: Optional[int]
    productID: int
    isFront: bool = False
    imageURL: str

    class Config:
        orm_mode = True

class InventoryBase(BaseModel):
    inventoryID: Optional[int]
    productID: int
    quantity: int
    stockMin: int
    stockMax: int

    class Config:
        orm_mode = True

class ShoppingCartBase(BaseModel):
    cartID: Optional[int]
    userID: int
    productID: int
    quantity: int
    cartStatus: str = 'active'

    class Config:
        orm_mode = True

class OrdersBase(BaseModel):
    orderID: Optional[int]
    userID: int
    orderDate: Optional[datetime]
    orderStatus: str = 'pending'
    totalPrice: float
    shippingAddress: str

    class Config:
        orm_mode = True
