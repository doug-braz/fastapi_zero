from pydantic import BaseModel, EmailStr


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


class UserDB(UserSchema):
    id: int


class UserList(BaseModel):
    users: list[UserPublic]
