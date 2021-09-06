from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr
    name: str
    is_active: bool = True


class User(UserBase):
    id: int

    class Config:
        orm_mode = True


class UserUpdate(UserBase):
    pass


class UserCreate(UserUpdate):
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str = 'bearer'
