from pydantic import BaseModel, ConfigDict, field_validator

class UsuarioBase(BaseModel):
    nome: str
    email: str
    telefone: str
    senha: str

class UsuarioRequest(UsuarioBase):
    pass

class UsuarioResponse(BaseModel):
    id: int
    nome: str
    email: str
    telefone: str

    model_config = ConfigDict(from_attributes=True)

    @field_validator("telefone", mode="before")
    def cast_telefone_to_str(cls, value):
        return str(value)