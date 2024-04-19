from fastapi import APIRouter, Depends, Path, Query, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from typing import List
from config.dbconnection import session
from models.models import Inventory as InventoryModel
from fastapi.encoders import jsonable_encoder
from schemas.schemas import InventoryBase as InventorySchema
from middlewares.jwt_bearer import JWTBearer

inventory_router = APIRouter()


# Get all inventory
@inventory_router.get("/inventory", tags=["inventory"], response_model=List[InventorySchema], status_code=200)
def get_inventory():
    db = session()
    inventory = db.query(InventoryModel).all()
    if not inventory:
        raise HTTPException(status_code=404, detail="Inventory not found")
    return JSONResponse(status_code=200, content=jsonable_encoder(inventory))


# Create inventory
@inventory_router.post("/inventory", response_model=InventorySchema, tags=["inventory"], status_code=201)
def create_inventory(inventoryID: int = Query(...), productID: int = Query(...), quantity: int = Query(...), stockMin: int = Query(...), stockMax: int = Query(...)):
    db = session()
    new_inventory = InventoryModel(inventoryID = inventoryID, productID = productID, quantity = quantity, stockMin = stockMin, stockMax = stockMax)
    db.add(new_inventory)
    db.commit()
    db.close()
    return JSONResponse(content={"message": "Product added to inventory"}, status_code=201)

# Add quantity to a product
@inventory_router.put("/inventory/add/{productID}", response_model=InventorySchema, tags=["inventory"], status_code=200)
def add_quantity(productID: int = Path(...), quantity: int = Query(...)):
    db = session()
    product = db.query(InventoryModel).filter(InventoryModel.productID == productID).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    if product.quantity + quantity > product.stockMax:
        raise HTTPException(status_code=400, detail="Quantity exceeds stock max")
    product.quantity += quantity
    db.commit()
    db.close()
    return JSONResponse(status_code=200, content={"message": "Product quantity updated"})

# Rest quantity to a product
@inventory_router.put("/inventory/rest/{productID}", response_model=InventorySchema, tags=["inventory"], status_code=200)
def rest_quantity(productID: int = Path(...), quantity: int = Query(...)):
    db = session()
    product = db.query(InventoryModel).filter(InventoryModel.productID == productID).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    if product.quantity - quantity < product.stockMin:
        raise HTTPException(status_code=400, detail="Quantity is less than stock min")
    product.quantity -= quantity
    db.commit()
    db.close()
    return JSONResponse(status_code=200, content={"message": "Product quantity updated"})

# Update inventory
@inventory_router.put("/inventory/{inventoryID}", response_model=InventorySchema, tags=["inventory"], status_code=200)
def update_inventory(inventoryID: int = Path(...), productID: int = Query(...), quantity: int = Query(...), stockMin: int = Query(...), stockMax: int = Query(...)):
    db = session()
    inventory = db.query(InventoryModel).filter(InventoryModel.inventoryID == inventoryID).first()
    if not inventory:
        raise HTTPException(status_code=404, detail="Inventory not found")
    inventory.productID = productID
    inventory.quantity = quantity
    inventory.stockMin = stockMin
    inventory.stockMax = stockMax
    db.commit()
    db.close()
    return JSONResponse(status_code=200, content={"message": "Inventory updated"})
