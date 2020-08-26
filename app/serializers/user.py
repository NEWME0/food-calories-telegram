from pydantic import BaseModel


class UserApiKeyCreate(BaseModel):
    username: str


class UserApiKeyDetail(BaseModel):
    message: str
    api_key: str
