from pydantic import BaseModel

class UsersBase(BaseModel):
    first_name: str
    last_name: str
    date_of_birth: str
    gender: str
    email: str
    cell: str
    address: str

class UsersCreate(UsersBase):
    pass

class UsersRead(UsersBase):
    id: int

    class Config:
        orm_mode = True

class UserCredentialBase(BaseModel):
    username: str
    password: str
    designation: str
    user_id: int

class UserCredentialCreate(UserCredentialBase):
    pass

class UserCredentialsRead(UserCredentialBase):
    id: int

    class Config:
        orm_mode = True

class SuppliersBase(BaseModel):
    supplier_name: str
    contact: str
    address: str
    email: str
class SuppliersCreate(SuppliersBase):
    pass

class SuppliersRead(SuppliersBase):
    id: int

    class Config:
        orm_mode = True

class ProductsBase(BaseModel):
    product_name: str
    quantity: int
    weight: float
    price_zwl: float
    price_usd: float
    measurement_category: str

class ProductsCreate(ProductsBase):
    pass

class ProductsRead(ProductsBase):
    id: int

    class Config:
        orm_mode = True

class DrawersBase(BaseModel):
    date: str
    operator: str
    opening_time: str
    float_zwl: float
    float_usd: float
    status: str
    expected_zwl: float
    actual_zwl: float
    expected_usd: float
    actual_usd: float
    card_sales: float
    ecocash_sales: float
    closing_time: str

class DrawersCreate(DrawersBase):
    pass

class DrawersRead(DrawersBase):
    id: int

    class Config:
        orm_mode = True

class SalesBase(BaseModel):
    receipt_number: str
    date: str
    product_name: str
    quantity: int
    weight: float
    price_zwl: float
    price_usd: float
    total_amount: float
    payment_method: str
    tellor: str
    drawer_id: int
    time_sold: str

class SalesCreate(SalesBase):
    pass

class SalesRead(SalesBase):
    id: int

    class Config:
        orm_mode = True

class CustomersBase(BaseModel):
    title: str
    last_name: str
    first_name: str
    contact: str
    email: str
    address: str

class CustomersCreate(CustomersBase):
    pass

class CustomersRead(CustomersBase):
    id: int

    class Config:
        orm_mode = True