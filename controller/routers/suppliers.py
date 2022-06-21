from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session

from .. import schemas, models
from ..database import get_db

router = APIRouter(prefix='/suppliers', tags=['Suppliers'])

# create Supplier
@router.post('/', response_model=schemas.SuppliersRead)
def create_supplier(supplier: schemas.SuppliersCreate, db: Session = Depends(get_db)):
    new_supplier = models.Suppliers(**supplier.dict())
    db.add(new_supplier)
    db.commit()
    db.refresh(new_supplier)
    return new_supplier

# get Suppliers
@router.get('/', response_model=list[schemas.SuppliersRead])
def get_suppliers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    suppliers = db.query(models.Suppliers).offset(skip).limit(limit).all()
    return suppliers

# get Supplier
@router.get('/{id}', response_model=schemas.SuppliersRead)
def get_supplier(id: int, db: Session = Depends(get_db)):
    supplier = db.query(models.Suppliers).filter(models.Suppliers.id == id).first()
    return supplier

# update Supplier
@router.put('/{id}', response_model=schemas.SuppliersRead)
def update_supplier(id: int, updated_supplier: schemas.SuppliersCreate, db: Session = Depends(get_db)):
    supplier_query = db.query(models.Suppliers).filter(models.Suppliers.id == id)
    if supplier_query.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Supplier with id: {id} not found')
    supplier_query.update(updated_supplier.dict(), synchronize_session=False)
    db.commit()
    return supplier_query.first()

# delete Supplier
@router.delete('/{id}', response_model=schemas.SuppliersRead)
def delete_supplier(id: int, db: Session = Depends(get_db)):
    supplier = db.query(models.Suppliers).filter(models.Suppliers.id == id)
    if supplier.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Supplier with id: {id} does not exist")
    supplier.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)