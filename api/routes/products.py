from fastapi import APIRouter, Depends, Path, Query, File, UploadFile
from fastapi.responses import JSONResponse
from typing import List
from config.dbconnection import session
from models.models import Products as ProductModel
from fastapi.encoders import jsonable_encoder
from schemas.schemas import ProductsBase as ProductSchema
from models.models import ProductsImages as ProductsImagesModel
from models.models import Inventory as inventoryModel
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
    try:
        products = db.query(ProductModel).all()

        productsWithImages = []
        for product in products:
            productsImages = db.query(ProductsImagesModel).filter(ProductsImagesModel.productID == product.productID).all()
            productsImages = [{"ImageURL": image['imageURL'], "isFront": image['isFront']} for image in jsonable_encoder(productsImages)]
            product = jsonable_encoder(product)
            product['images'] = productsImages
            productsWithImages.append(product)
        if not productsWithImages:
            return JSONResponse(status_code=404, content={"message": "No products found"})
        return JSONResponse(status_code=200, content=productsWithImages)
    except Exception as e:
        print(e)
        return JSONResponse(status_code=500, content={"message": "Internal Server Error"})

#Get product with images
@products_router.get("/products/{productID}", tags=['products'], response_model=ProductsUrlImageSchema, status_code=200)
def get_product_individual(productID: int = Path(...)):
    db = session()
    try:
        product = db.query(ProductModel).filter(ProductModel.productID == productID).first()
        if not product:
            return JSONResponse(status_code=404, content={"message": f"Product with ID {productID} not found"})
        productsImages = db.query(ProductsImagesModel).filter(ProductsImagesModel.productID == product.productID).all()
        quantity = db.query(inventoryModel).filter(inventoryModel.productID == product.productID).first()
        productsImages = [{"ImageURL": image['imageURL'], "isFront": image['isFront']} for image in jsonable_encoder(productsImages)]
        product = jsonable_encoder(product)
        product['quantity'] = quantity.quantity
        product['images'] = productsImages
        return JSONResponse(status_code=200, content=product)
    except Exception as e:
        print(e)
        return JSONResponse(status_code=500, content={"message": "Internal Server Error"})

#Get productImages
@products_router.get("/products/images/{productID}", tags=['products'], response_model=List[ProductsImagesBaseSchema], status_code=200)
def get_product_images(productID: int = Path(...)):
    db = session()
    result = db.query(ProductsImagesModel).filter(ProductsImagesModel.productID == productID).all()
    if not result:
        return JSONResponse(status_code=404, content={"message": f"Product with ID {productID} not found"})
    db.close()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

#Get product by category cap
@products_router.get("/products/category/cap", tags=['products'], response_model=List[ProductsUrlImageSchema], status_code=200)
def get_products_Category_Cap():
    try:
        db = session() 
        products = (
            db.query(ProductModel)
            .filter(ProductModel.category == 'cap')
            .all()
        )

        productsWithImages = []
        for product in products:
            productsImages = (
                db.query(ProductsImagesModel)
                .filter(ProductsImagesModel.productID == product.productID)
                .all()
            )
            productsImages = [{"ImageURL": image['imageURL'], "isFront": image['isFront']} for image in jsonable_encoder(productsImages)]
            product = jsonable_encoder(product)
            product['images'] = productsImages
            productsWithImages.append(product)
        
        if not productsWithImages:
            return JSONResponse(status_code=404, content={"message": "No products found in category 'cap'"})
        
        return JSONResponse(status_code=200, content=productsWithImages)
    except Exception as e:
        print(e)
        return JSONResponse(status_code=500, content={"message": "Internal Server Error"})

#Get product by category clock
@products_router.get("/products/category/clock", tags=['products'], response_model=List[ProductsUrlImageSchema], status_code=200)
def get_products_Category_Clock():
    try:
        db = session() 
        products = (
            db.query(ProductModel)
            .filter(ProductModel.category == 'clock')
            .all()
        )

        productsWithImages = []
        for product in products:
            productsImages = (
                db.query(ProductsImagesModel)
                .filter(ProductsImagesModel.productID == product.productID)
                .all()
            )
            productsImages = [{"ImageURL": image['imageURL'], "isFront": image['isFront']} for image in jsonable_encoder(productsImages)]
            product = jsonable_encoder(product)
            product['images'] = productsImages
            productsWithImages.append(product)
        
        if not productsWithImages:
            return JSONResponse(status_code=404, content={"message": "No products found in category 'clock'"})
        
        return JSONResponse(status_code=200, content=productsWithImages)
    except Exception as e:
        print(e)
        return JSONResponse(status_code=500, content={"message": "Internal Server Error"})
    
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

#Update productImages
@products_router.put("/products/updateImages/{imageID}", tags=['products'], response_model=ProductsImagesBaseSchema, status_code=200)# dependencies=[Depends(JWTBearer())]
def update_product_images(imageID: int = Path(...), isFront: bool = Query(...), imageURL: str = Query(...)):
    db = session()
    productImage = db.query(ProductsImagesModel).filter(ProductsImagesModel.imageID == imageID).first()
    if not productImage:
        return JSONResponse(status_code=404, content={"message": f"Product with ID {imageID} not found"})
    result = cloudinary.uploader.upload(imageURL)
    imageURL = result.get('url')
    productImage.isFront = isFront
    productImage.imageURL = imageURL
    db.commit()
    return JSONResponse(content={'imageID': imageID, 'isFront': isFront, 'imageURL': imageURL}, status_code=200)


