from pydantic import BaseModel, ConfigDict, EmailStr, Field


# Ao definir o schema, garantimos o tipo de dados esperados, e isso também
# reflete na documentação da API
class Message(BaseModel):
    message: str


class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserPublic(BaseModel):
    username: str
    email: EmailStr
    id: int
    model_config = ConfigDict(from_attributes=True)


class UserList(BaseModel):
    users: list[UserPublic]


class FilterPage(BaseModel):
    offset: int = Field(0, ge=0)
    limit: int = Field(100, ge=1)


class Token(BaseModel):
    access_token: str
    token_type: str
