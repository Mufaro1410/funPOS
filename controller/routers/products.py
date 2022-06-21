from fastapi import APIRouter, Depends, HTTPException, status, Response
from numpy import product
from sqlalchemy.orm import Session

from .. import schemas, models
from ..database import get_db

router = APIRouter(prefix='/products', tags=['Products'])

# create Product
@router.post('/', response_model=schemas.ProductsRead)
def create_product(product: schemas.ProductsCreate, db: Session = Depends(get_db)):
    new_product = models.Products(**product.dict())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

# get Products
@router.get('/', response_model=list[schemas.ProductsRead])
def get_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    products = db.query(models.Products).offset(skip).limit(limit).all()
    return products

# get Product
@router.get('/{id}', response_model=schemas.ProductsRead)
def get_product(id: int, db: Session = Depends(get_db)):
    product = db.query(models.Products).filter(models.Products.id == id).first()
    return product

# update Product
@router.put('/{id}', response_model=schemas.ProductsRead)
def update_product(id: int, updated_product: schemas.ProductsCreate, db: Session = Depends(get_db)):
    product_query = db.query(models.Products).filter(models.Products.id == id)
    if product_query.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Product with id: {id} not found')
    product_query.update(updated_product.dict(), synchronize_session=False)
    db.commit()
    return product_query.first()

# delete Product
@router.delete('/{id}', response_model=schemas.ProductsRead)
def delete_product(id: int, db: Session = Depends(get_db)):
    product = db.query(models.Products).filter(models.Products.id == id)
    if product.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Product with id: {id} does not exist")
    product.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)