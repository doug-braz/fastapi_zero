from pydantic import BaseModel, ConfigDict, EmailStr


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
