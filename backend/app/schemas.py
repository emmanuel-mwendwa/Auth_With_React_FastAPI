from pydantic import BaseModel, EmailStr, constr, confloat

from datetime import datetime

from typing import Optional, List


class UserBase(BaseModel):

    firstname: str
    lastname: str
    email: EmailStr

    class Config:

        from_attributes = True


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

class SignUpOut(BaseModel):

    user: UserBase
    token: Token


class LeadBase(BaseModel):

    first_name: str
    last_name: str
    email: str
    company: str
    note: str


class LeadCreate(LeadBase):

    pass

class LeadOut(LeadBase):

    id: int
    owner_id: int
    created_at: datetime
    updated_at: datetime

    class Config:

        from_attributes=True