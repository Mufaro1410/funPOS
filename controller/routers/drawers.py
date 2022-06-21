from fastapi import APIRouter, Depends, HTTPException, status, Response
from numpy import product
from sqlalchemy.orm import Session

from .. import schemas, models
from ..database import get_db

router = APIRouter(prefix='/drawers', tags=['Drawers'])

# create Drawer
@router.post('/', response_model=schemas.DrawersRead)
def create_drawer(drawer: schemas.DrawersCreate, db: Session = Depends(get_db)):
    new_drawer = models.Drawers(**drawer.dict())
    db.add(new_drawer)
    db.commit()
    db.refresh(new_drawer)
    return new_drawer

# get Drawers
@router.get('/', response_model=list[schemas.DrawersRead])
def get_drawers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    drawers = db.query(models.Drawers).offset(skip).limit(limit).all()
    return drawers

# get Drawer
@router.get('/{id}', response_model=schemas.DrawersRead)
def get_drawer(id: int, db: Session = Depends(get_db)):
    drawer = db.query(models.Drawers).filter(models.Drawers.id == id).first()
    return drawer

# update Drawer
@router.put('/{id}', response_model=schemas.DrawersRead)
def update_drawer(id: int, updated_drawer: schemas.DrawersCreate, db: Session = Depends(get_db)):
    drawer_query = db.query(models.Drawers).filter(models.Drawers.id == id)
    if drawer_query.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Drawer with id: {id} not found')
    drawer_query.update(updated_drawer.dict(), synchronize_session=False)
    db.commit()
    return drawer_query.first()

# delete Drawer
@router.delete('/{id}', response_model=schemas.DrawersRead)
def delete_drawer(id: int, db: Session = Depends(get_db)):
    drawer = db.query(models.Drawers).filter(models.Drawers.id == id)
    if drawer.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Drawer with id: {id} does not exist")
    drawer.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)