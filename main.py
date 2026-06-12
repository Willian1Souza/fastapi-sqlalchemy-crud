from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session

from models import Usuario
from database import engine, Base, get_db
from repositories import UsuarioRepository
from schemas import UsuarioRequest, UsuarioResponse
from fastapi.middleware.cors import CORSMiddleware



Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post(
    "/api/usuarios",
    response_model=UsuarioResponse,
    status_code=status.HTTP_201_CREATED
)
def create(
    request: UsuarioRequest,
    db: Session = Depends(get_db)
):
    usuario = UsuarioRepository.save(
        db,
        Usuario(**request.model_dump())
    )

    return UsuarioResponse.model_validate(usuario)

@app.get("/api/usuarios", response_model=list[UsuarioResponse])
def find_all(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    nome: str | None = None
):
    usuarios = UsuarioRepository.find_all(db, skip=skip, limit=limit, nome=nome)
    # Validamos cada objeto da lista para garantir a integridade dos dados
    return [UsuarioResponse.model_validate(u) for u in usuarios]

@app.get("/api/usuarios/{id}", response_model=UsuarioResponse)
def find_by_id(id: int, db: Session = Depends(get_db)):
    usuario = UsuarioRepository.find_by_id(db, id)

    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario não encontrado"
        )

    return UsuarioResponse.model_validate(usuario)


@app.delete("/api/usuarios/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_by_id(id: int, db: Session = Depends(get_db)):
    if not UsuarioRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario não encontrado"
        )

    UsuarioRepository.delete_by_id(db, id)


@app.put("/api/usuarios/{id}", response_model=UsuarioResponse)
def update(id: int, request: UsuarioRequest, db: Session = Depends(get_db)):
    if not UsuarioRepository.exists_by_id(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario não encontrado"
        )

    # Extrai os dados e garante que o ID da URL seja o ID do objeto
    dados_atualizados = request.model_dump()
    usuario = UsuarioRepository.save(
        db,
        Usuario(id=id, **dados_atualizados)
    )

    return UsuarioResponse.model_validate(usuario)


@app.get("/")
def home():
    return {"mensagem": "API funcionando"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
