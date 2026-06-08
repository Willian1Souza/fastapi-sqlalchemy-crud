from sqlalchemy import Column, Integer, String

from database import Base

class Usuario(Base):
    __tablename__ = "Usuarios"

    id: int = Column(Integer, primary_key=True, index=True)
    nome: str = Column(String(100), nullable=False)
    email: str = Column(String(255), nullable=False)
    telefone: str = Column(String(20), nullable=False)
    senha: str = Column(String(255), nullable=False)