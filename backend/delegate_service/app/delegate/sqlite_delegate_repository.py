import os

from sqlalchemy import select, create_engine, Engine
from sqlalchemy.orm import Session

from app.models.delegate_model import Delegate
from app.repositories.delegate_repository_interface import DelegateRepositoryInterface


class SQLiteDelegateRepository(DelegateRepositoryInterface):
    __db_path: str

    def __init__(self, db_path):
        self.__db_path = db_path

    def get_delegate_exists(self, cpf: str) -> bool:
        session = self.get_session()
        selection = select(Delegate).where(Delegate.cpf.is_(cpf))
        session.close()
        return len(session.scalars(selection).all()) == 1

    def register_delegate(self, delegate: Delegate) -> bool:
        try:
            session = self.get_session()
            session.add(delegate)
            session.commit()
            session.close()
        except:
            return False
        
        return True

    def check_db_file(self) -> None:
        if not os.path.exists(self.__db_path):
            open(self.__db_path, "x")

    def get_engine(self) -> Engine:
        return create_engine(f'sqlite:///{self.__db_path}')

    def get_session(self) -> Session:
        return Session(self.get_engine())
