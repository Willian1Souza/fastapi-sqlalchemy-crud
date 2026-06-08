from sqlalchemy.orm import Session

from models import Usuario


class UsuarioRepository:
    """
    Repositório responsável pelas operações de persistência da entidade Usuario.
    Centraliza as consultas ao banco de dados utilizando a sessão do SQLAlchemy.
    """

    @staticmethod
    def find_all(db: Session, skip: int = 0, limit: int = 100, nome: str | None = None) -> list[Usuario]:
        """
        Busca os usuários cadastrados com suporte a paginação.
        """
        query = db.query(Usuario)

        if nome:
            # ilike faz uma busca que ignora maiúsculas/minúsculas
            query = query.filter(Usuario.nome.ilike(f"%{nome}%"))

        return query.offset(skip).limit(limit).all()

    @staticmethod
    def save(db: Session, usuario: Usuario) -> Usuario:
        """
        Realiza a persistência de um usuário.
        Se o objeto já possuir um ID, utiliza o 'merge' para atualizar o registro existente.
        Caso contrário, utiliza o 'add' para criar um novo registro no banco.
        """
        if usuario.id:
            usuario = db.merge(usuario)
        else:
            db.add(usuario)

        db.commit()
        db.refresh(usuario)
        return usuario

    @staticmethod
    def find_by_id(db: Session, id: int) -> Usuario | None:
        """
        Busca um único usuário através do seu identificador primário (ID).
        Retorna a instância do Usuario ou None caso não seja encontrado.
        """
        return db.query(Usuario).filter(Usuario.id == id).first()

    @staticmethod
    def exists_by_id(db: Session, id: int) -> bool:
        """
        Verifica a existência de um usuário por ID de forma performática.
        Útil para validações antes de operações de atualização ou exclusão.
        """
        return db.query(Usuario).filter(Usuario.id == id).first() is not None

    @staticmethod
    def delete_by_id(db: Session, id: int) -> None:
        """
        Exclui um usuário do banco de dados com base no ID fornecido.
        """
        usuario = db.query(Usuario).filter(Usuario.id == id).first()

        if usuario is not None:
            db.delete(usuario)
            db.commit()
