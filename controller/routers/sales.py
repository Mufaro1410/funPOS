from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session

from .. import schemas, models
from ..database import get_db

router = APIRouter(prefix='/sales', tags=['Sales'])

# create Sales
@router.post('/', response_model=schemas.SalesRead)
def create_sales(sale: schemas.SalesCreate, db: Session = Depends(get_db)):
    new_sale = models.Sales(**sale.dict())
    db.add(new_sale)
    db.commit()
    db.refresh(new_sale)
    return new_sale

# get Sales
@router.get('/', response_model=list[schemas.SalesRead])
def get_sales(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    sales = db.query(models.Sales).offset(skip).limit(limit).all()
    return sales

# get Sale
@router.get('/{receipt_number}', response_model=list[schemas.SalesRead])
def get_sale(receipt_number: str, db: Session = Depends(get_db)):
    sale = db.query(models.Sales).filter(models.Sales.receipt_number == receipt_number).all()
    return sale

# update Sale
@router.put('/{receipt_number}', response_model=list[schemas.SalesRead])
def update_sale(receipt_number: str, updated_sale: schemas.SalesCreate, db: Session = Depends(get_db)):
    sale_query = db.query(models.Sales).filter(models.Sales.receipt_number == receipt_number)
    if sale_query.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Sale with receipt_number: {receipt_number} not found')
    sale_query.update(updated_sale.dict(), synchronize_session=False)
    db.commit()
    return sale_query.all()

# delete Sale
@router.delete('/{receipt_number}', response_model=list[schemas.SalesRead])
def delete_sale(receipt_number: str, db: Session = Depends(get_db)):
    sale = db.query(models.Sales).filter(models.Sales.receipt_number == receipt_number)
    if sale.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Sale with receipt_number: {receipt_number} does not exist")
    sale.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)