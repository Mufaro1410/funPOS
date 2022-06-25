from requests import delete
from sqlalchemy import Column, ForeignKey, Integer, String, Float, Time
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
    #created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

    user_credentials = relationship('UserCredentials', back_populates='users')

class UserCredentials(Base):
    __tablename__ = 'user_credentials'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    designation = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    #created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

    users = relationship('Users', back_populates='user_credentials')
    sales = relationship('Sales', back_populates='user_credentials')
    drawers = relationship('Drawers', back_populates='user_credentials')

class Suppliers(Base):
    __tablename__ = 'suppliers'

    id = Column(Integer, primary_key=True)
    supplier_name = Column(String, unique=True, nullable=False)
    contact = Column(String, nullable=False)
    address = Column(String, nullable=False)
    email = Column(Integer, ForeignKey('users.id'))
    #created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

    #receiving = relationship('Product', back_populates='suppliers')

class Products(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    product_name = Column(String, unique=True, nullable=False)
    quantity = Column(String,)
    weight = Column(Float)
    price_zwl = Column(Float, nullable=False)
    price_usd = Column(Float, nullable=False)
    measurement_category = Column(String, nullable=False)
    #created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

    #changes = relationship('Changes', back_populates='products')

class Drawers(Base):
    __tablename__ = 'drawers'

    id = Column(Integer, primary_key=True)
    date = Column(String, nullable=False)
    operator = Column(String, ForeignKey('user_credentials.id'))
    opening_time = Column(String, nullable=False)
    float_zwl = Column(Float, nullable=False)
    float_usd = Column(Float, nullable=False)
    status = Column(String, nullable=False)
    expected_zwl = Column(Float, nullable=False)
    actual_zwl = Column(Float, nullable=False)
    expected_usd = Column(Float, nullable=False)
    actual_usd = Column(Float, nullable=False)
    card_sales = Column(Float, nullable=False)
    ecocash_sales = Column(Float, nullable=False)
    closing_time = Column(String)
    #created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

    user_credentials = relationship('UserCredentials', back_populates='drawers')
    sales = relationship('Sales', back_populates='drawers')

class Sales(Base):
    __tablename__ = 'sales'

    id = Column(Integer, primary_key=True)
    receipt_number = Column(String, nullable=False)
    date = Column(String, nullable=False)
    product_name = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    weight = Column(Float, nullable=False)
    price_zwl = Column(Float, nullable=False)
    price_usd = Column(Float, nullable=False)
    total_amount = Column(Float, nullable=False)
    payment_method = Column(String, nullable=False)
    tellor = Column(String, ForeignKey('user_credentials.id'), nullable=False)
    drawer_id = Column(Integer, ForeignKey('drawers.id'), nullable=False)
    time_sold = Column(String, nullable=False)
    #created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

    user_credentials = relationship('UserCredentials', back_populates='sales')
    drawers = relationship('Drawers', back_populates='sales')

class Customers(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    last_name = Column(String)
    first_name = Column(String)
    contact = Column(String, unique=True)
    email = Column(String, unique=True)
    address = Column(String)
    #created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))