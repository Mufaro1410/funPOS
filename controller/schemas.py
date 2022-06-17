from pydantic import BaseModel

class Users(BaseModel):
    id: int
    first_name: str
    last_name: str
    date_of_birth: str
    gender: str
    email: str
    cell: str
    address: str
    username: str
    password: str
    designation: str