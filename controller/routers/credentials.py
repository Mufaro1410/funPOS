from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from .. import models, schemas
from ..database import get_db

router = APIRouter(prefix='/credentials', tags=['Credentials'])

@router.post('/', response_model=schemas.UserCredentialsRead)
def create_user_credential(user_credentials: schemas.UserCredentialCreate, db: Session = Depends(get_db)):
    new_user_credential = models.UserCredentials(**user_credentials.dict())
    db.add(new_user_credential)
    db.commit()
    db.refresh(new_user_credential)
    return new_user_credential

@router.get('/', response_model=list[schemas.UserCredentialsRead])
def get_users_credentials(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    get_users_credentials = db.query(models.UserCredentials).offset(skip).limit(limit).all()
    return get_users_credentials

@router.get('/{id}', response_model=schemas.UserCredentialsRead)
def get_user_credential(id: int, db: Session = Depends(get_db)):
    user_credential = db.query(models.UserCredentials).filter(models.UserCredentials.id == id).first()
    return user_credential

# update User Credential
@router.put('/{id}', response_model=schemas.UserCredentialsRead)
def update_user_credentials(id: int, updated_user_credentials: schemas.UserCredentialCreate, db: Session = Depends(get_db)):
    user_credential_query = db.query(models.UserCredentials).filter(models.UserCredentials.id == id)
    if user_credential_query.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User credential with id: {id} not found')
    user_credential_query.update(updated_user_credentials.dict(), synchronize_session=False)
    db.commit()
    return user_credential_query.first()

# delete User Credentials
@router.delete('/{id}', response_model=schemas.UserCredentialsRead)
def delete_user_credentials(id: int, db: Session = Depends(get_db)):
    user = db.query(models.UserCredentials).filter(models.UserCredentials.id == id)
    if user.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User credential with id: {id} does not exist")
    user.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)