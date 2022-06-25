from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from .. import models, schemas
from ..database import get_db

router = APIRouter(prefix='/customers', tags=['Customers'])

# create Customer
@router.post('/', response_model=schemas.CustomersRead)
def create_customer(customer: schemas.CustomersCreate, db: Session = Depends(get_db)):
    new_customer = models.Customers(**customer.dict())
    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)
    return new_customer

# get Customers
@router.get('/', response_model=list[schemas.CustomersRead])
def get_customers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    get_customers = db.query(models.Customers).offset(skip).limit(limit).all()
    return get_customers

# get Customer
@router.get('/{id}', response_model=schemas.CustomersRead)
def get_customer(id: int, db: Session = Depends(get_db)):
    customer = db.query(models.Customers).filter(models.Customers.id == id).first()
    return customer

# update Customer
@router.put('/{id}', response_model=schemas.CustomersRead)
def update_customer(id: int, updated_customer: schemas.CustomersCreate, db: Session = Depends(get_db)):
    customer_query = db.query(models.Customers).filter(models.Customers.id == id)
    if customer_query.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Customer with id: {id} not found')
    customer_query.update(updated_customer.dict(), synchronize_session=False)
    db.commit()
    return customer_query.first()

# delete Customer
@router.delete('/{id}', response_model=schemas.CustomersRead)
def delete_customer(id: int, db: Session = Depends(get_db)):
    customer = db.query(models.Customers).filter(models.Customers.id == id)
    if customer.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Customer with id: {id} does not exist")
    customer.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)