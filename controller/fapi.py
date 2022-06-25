from fastapi import FastAPI, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session

from . import models
from controller.routers import users, credentials, suppliers, products, drawers, customers
from .database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)
app.include_router(credentials.router)
app.include_router(suppliers.router)
app.include_router(products.router)
app.include_router(drawers.router)
app.include_router(customers.router)