from fastapi import APIRouter, Depends, Path, Query, File, UploadFile
from fastapi.responses import JSONResponse
from typing import List
from config.dbconnection import session
from models.models import Products as ProductModel
from fastapi.encoders import jsonable_encoder
from schemas.schemas import ProductsBase as ProductSchema
from models.models import ProductsImages as ProductsImagesModel
from schemas.schemas import ProductsImagesBase as ProductsImagesBaseSchema
from schemas.schemas import ProductsUrlImage as ProductsUrlImageSchema
from middlewares.jwt_bearer import JWTBearer
import cloudinary.uploader
from config.cloudinary import cloudinary

products_router = APIRouter()

#Get all products
@products_router.get("/products", tags=['products'], response_model=List[ProductsUrlImageSchema], status_code=200)
def get_products():
    db = session()
    result = (
        db.query(
            ProductModel.productID,
            ProductModel.productName,
            ProductModel.description,
            ProductModel.price,
            ProductModel.category,
            ProductsImagesModel.imageURL.label('imageURL'),
            ProductsImagesModel.isFront.label('isFront')
        )
        .join(ProductsImagesModel, ProductModel.productID == ProductsImagesModel.productID)
        .all()
    )
    if not result:
        return JSONResponse(status_code=404, content={"message": "No products found"})
    products_list = [
    ProductsUrlImageSchema(
        productID = row.productID,
        productName = row.productName,
        description = row.description,
        price = row.price,
        category = row.category,
        imageURL = row.imageURL,
        isFront = row.isFront
    ) for row in result
    ]
    db.close()
    return JSONResponse(status_code=200, content=jsonable_encoder(products_list))

#Get product
@products_router.get("/products/{productID}", tags=['products'], response_model=ProductsUrlImageSchema, status_code=200)
def get_product(productID: int = Path(...)):
    db = session()
    result = (
        db.query(
            ProductModel.productID,
            ProductModel.productName,
            ProductModel.description,
            ProductModel.price,
            ProductModel.category,
            ProductsImagesModel.imageURL.label('imageURL'),
            ProductsImagesModel.isFront.label('isFront')
        )
        .join(ProductsImagesModel, ProductModel.productID == ProductsImagesModel.productID)
        .filter(ProductModel.productID == productID)
        .all()
    )
    if not result:
        return JSONResponse(status_code=404, content={"message": "No products found"})
    products_list = [
    ProductsUrlImageSchema(
        productID = row.productID,
        productName = row.productName,
        description = row.description,
        price = row.price,
        category = row.category,
        imageURL = row.imageURL,
        isFront = row.isFront
    ) for row in result
    ]
    db.close()
    return JSONResponse(status_code=200, content=jsonable_encoder(products_list))

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
    result = cloudinary.uploader.upload(imageURL)
    imageURL = result.get('url')
    new_product = ProductsImagesModel(productID=productID, isFront=isFront, imageURL=imageURL)
    db.add(new_product)
    db.commit()
    return JSONResponse(content={'productID': productID, 'isFront': isFront, 'imageURL': imageURL}, status_code=200)

#Update product
@products_router.put("/products/update/{productID}", tags=['products'], response_model=ProductSchema, status_code=200)# dependencies=[Depends(JWTBearer())]
def update_product(productID: int = Path(...), productName: str = Query(...), description: str = Query(...), price: float = Query(...), category: str = Query(...)):
    db = session()
    product = db.query(ProductModel).filter(ProductModel.productID == productID).first()
    if not product:
        return JSONResponse(status_code=404, content={"message": f"Product with ID {productID} not found"})
    product.productName = productName
    product.description = description
    product.price = price
    product.category = category
    db.commit()
    return JSONResponse(content=jsonable_encoder(product), status_code=200)