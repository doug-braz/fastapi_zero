from pydantic import BaseModel


# Ao definir o schema, garantimos o tipo de dados esperados, e isso também
# reflete na documentação da API
class Message(BaseModel):
    message: str
