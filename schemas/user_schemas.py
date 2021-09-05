from pydantic import BaseModel, constr

from schemas.validators import EmailStrToLower


class UserBase(BaseModel):
    email: EmailStrToLower
    name: str
    is_active: bool = False


class User(UserBase):
    id: int

    class Config:
        orm_mode = True


class UserUpdate(UserBase):
    pass


class UserCreate(UserUpdate):
    password: constr(min_length=8)
