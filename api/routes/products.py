from fastapi import APIRouter, Depends, Path, Query, File, UploadFile
from fastapi.responses import JSONResponse
from typing import List
from config.dbconnection import session
from models.models import Products as ProductModel
from fastapi.encoders import jsonable_encoder
from schemas.schemas import ProductsBase as ProductSchema
from models.models import ProductsImages as ProductsImagesModel
from schemas.schemas import ProductsImagesBase as ProductsImagesBaseSchema
from middlewares.jwt_bearer import JWTBearer
import cloudinary.uploader
from config.cloudinary import cloudinary

products_router = APIRouter()

#Get all products
@products_router.get("/products", tags=['products'], response_model=List[ProductSchema], status_code=200)
def get_products():
    db = session()
    result = db.query(ProductModel).all()
    db.close()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

#Get product
@products_router.get("/products/{productID}", tags=['products'], response_model=ProductSchema, status_code=200)
def get_product(productID: int = Path(...)):
    db = session()
    result = db.query(ProductModel).filter(ProductModel.productID == productID).first()
    if not result:
        return JSONResponse(status_code=404, content={"message": "No product found"})
    db.close()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

#Get productImages
@products_router.get("/products/images/{productID}", tags=['products'], response_model=List[ProductsImagesBaseSchema], status_code=200)
def get_product_images(productID: int = Path(...)):
    db = session()
    result = db.query(ProductsImagesModel).filter(ProductsImagesModel.productID == productID).all()
    if not result:
        return JSONResponse(status_code=404, content={"message": f"Product with ID {productID} not found"})
    db.close()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

#Post product
@products_router.post("/products/post", tags=['products'], response_model=ProductSchema, status_code=200)# dependencies=[Depends(JWTBearer())]
def create_product(productID: int = Query(...), productName: str = Query(...), description: str = Query(...), price: float = Query(...), category: str = Query(...)):
    db = session()
    new_product = ProductModel(productID=productID, productName=productName, description=description, price=price, category=category)
    db.add(new_product)
    db.commit()
    return JSONResponse(content=jsonable_encoder(new_product), status_code=200)

#Post productImages
@products_router.post("/products/postImages", tags=['products'], response_model=ProductsImagesBaseSchema, status_code=200) #dependencies=[Depends(JWTBearer())]
def create_product_image(productID: int = Query(...), isFront: bool = Query(...), imageURL: str = Query(...)):
    db = session()
    product = db.query(ProductModel).filter(ProductModel.productID == productID).first()
    if not product:
        return JSONResponse(status_code=404, content={"message": f"Product with ID {productID} not found"})
    result = cloudinary.uploader.upload(imageURL.file)
    imageURL = result.get('url')
    new_product = ProductsImagesModel(productID=productID, isFront=isFront, imageURL=imageURL)
    db.add(new_product)
    db.commit()
    return JSONResponse(content={'productID': productID, 'isFront': isFront, 'imageURL': imageURL}, status_code=200)

