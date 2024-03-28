from pydantic import BaseModel, EmailStr, constr, confloat

from datetime import datetime

from typing import Optional, List


class UserBase(BaseModel):

    firstname: str
    lastname: str
    email: EmailStr


class CreateUser(UserBase):

    password: str


class UserLogin(BaseModel):

    email: EmailStr
    password: str


class Token(BaseModel):
    
    access_token: str
    token_type: str


class TokenData(BaseModel):

    id: Optional[str] = None