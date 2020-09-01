from datetime import datetime, date
from pydantic import BaseModel


class UserApiKeyCreate(BaseModel):
    username: str


class UserApiKeyDetail(BaseModel):
    message: str
    api_key: str


class UserProfileDetail:
    id: int
    date_created: datetime
    date_modified: datetime
    gender: str
    height: int
    weight: int
    date_of_birth: date
    user: int


class UserTarget:
    pass
