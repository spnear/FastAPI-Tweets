#Python imports
from uuid import UUID
from datetime import date, datetime

#FastAPI imports
from typing import Optional

from fastapi import FastAPI

#Pydantic imports
from pydantic import BaseModel, EmailStr, Field


app = FastAPI()


#Models
class UserBase(BaseModel):

    user_id: UUID = Field(...)
    email: EmailStr = Field(...)

class userLogin(UserBase):

    password: str = Field(
        ...,
        min_length=8,
        max_length=64
    )


class User(UserBase):

    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    birth_date: Optional[date] = Field(default=None)


class Tweets(BaseModel):
    tweet_id: UUID = Field(...)
    content: str = Field(
        ...,
        min_length=1,
        max_length=256
    )
    created_at: datetime = Field(default=datetime.now())
    updated_at: Optional[datetime] = Field(default=datetime.now())
    by: User = Field(...)

@app.get(path="/")
def home():
    return {"Twitter API": "Working!"}