# Import the sqlalchemy parts
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
#from .config import settings

# Create a database url for sqlalchemy
SQLALCHEMY_DATABASE_URL = f"sqlite:///./funPOS.db"

# Create an sqlalchemy engine
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread":False})

#Create a SessionLocal class 
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class
Base = declarative_base()

# Dependency ~ opening & closing a connection to a database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()