from config.dbconnection import Base 
from sqlalchemy import Column, Integer, String, Float, Enum, Text, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


class Users(Base):
    __tablename__ = "users"

    userID = Column(Integer, primary_key=True, autoincrement=True)
    userName = Column(String(50), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    fullName = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    phone = Column(String(20))
    role = Column(Enum('client', 'admin'), nullable=False, default='client')
    address = Column(Text)

    cart = relationship("shoppingCart", back_populates="user")
    orders = relationship("Orders", back_populates="user")

class ProductsImages(Base):
    __tablename__ = "productsImages"

    imageID = Column(Integer, primary_key=True, autoincrement=True)
    productID = Column(Integer, ForeignKey('products.productID'), nullable=False)
    isFront = Column(Boolean, nullable=False,server_default='0')
    imageURL = Column(String(500), nullable=False)

    product = relationship("Products", back_populates="images")

class Products(Base):
    __tablename__ = "products"

    productID = Column(Integer, primary_key=True, autoincrement=True)
    productName = Column(String(50), nullable=False)
    description = Column(Text, nullable=False)
    price = Column(Float, nullable=False)
    category = Column(Enum('clock', 'cap'), nullable=False)

    images = relationship("ProductsImages", back_populates="product")
    inventory = relationship("Inventory", back_populates="product")
    cart = relationship("shoppingCart", back_populates="product")


class Inventory(Base):
    __tablename__ = "inventory"

    inventoryID = Column(Integer, primary_key=True, autoincrement=True)
    productID = Column(Integer, ForeignKey('products.productID'), nullable=False)
    quantity = Column(Integer, nullable=False)
    stockMin = Column(Integer, nullable=False)
    stockMax = Column(Integer, nullable=False)

    product = relationship("Products", back_populates="inventory")

class shoppingCart(Base):
    __tablename__ = "shoppingCart"

    cartID = Column(Integer, primary_key=True, autoincrement=True)
    userID = Column(Integer, ForeignKey('users.userID'), nullable=False)
    productID = Column(Integer, ForeignKey('products.productID'), nullable=False)
    quantity = Column(Integer, nullable=False)
    cartStatus = Column(Enum('active', 'inactive', 'cancelled'), nullable=False, default='active')
    
    user = relationship("Users", back_populates="cart")
    product = relationship("Products", back_populates="cart")

class Orders(Base):
    __tablename__ = "orders"

    orderID = Column(Integer, primary_key=True, autoincrement=True)
    userID = Column(Integer, ForeignKey('users.userID'), nullable=False)
    orderDate = Column(DateTime, nullable=False, server_default= func.now())
    orderStatus = Column(Enum('pending', 'processing', 'shipped', 'delivered', 'cancelled'), nullable=False, default='pending')
    totalPrice = Column(Float, nullable=False)
    shoppingAddress = Column(String(150), nullable=False)

    user = relationship("Users", back_populates="orders")
