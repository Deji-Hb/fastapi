#this is the schema
from datetime import datetime
from typing import Optional, Literal
from pydantic import BaseModel, EmailStr

#from pydantic.types import conint


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes=True
 

#this inherits the objects from PostBase
class PostRequest(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

    class Config:
        from_attributes=True

class PostOut(BaseModel):
    Post: PostRequest
    votes: int

    class Config:
        from_attributes=True

class UserCreate(BaseModel):
    #using a library that validates email
    email: EmailStr
    password: str

    class Config:
        from_attributes=True

class UserLogin(BaseModel):
    email: EmailStr
    password: str

    class Config:
        from_attributes=True

class Token(BaseModel):
    access_token: str
    token_type: str

    class Config:
        from_attributes=True

class TokenData(BaseModel):
    id: Optional[str] = None

    class Config:
        from_attributes=True

class Vote(BaseModel):
    post_id: int
    dir: Literal[0, 1]
    # dir: conint(le=1)
    # dir: Annotated[int, Field(le=1)]
