from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    id: int
    email: EmailStr
    class Config:
        from_attributes = True #New syntax for V2

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class UserBase(BaseModel):
    username: str
    email: EmailStr
    role: str = "staff"

class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True
