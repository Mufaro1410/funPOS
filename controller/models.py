from sqlalchemy import Column, ForeignKey, Integer, String, Date, Float, Time
from sqlalchemy.orm import relationship

from .database import Base

class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    date_of_birth = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    email = Column(String, unique=True)
    cell = Column(String, unique=True)
    address = Column(String)

    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    designation = Column(String, nullable=False)
    #created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))