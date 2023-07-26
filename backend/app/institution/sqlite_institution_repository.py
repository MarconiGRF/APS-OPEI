import os

from sqlalchemy import select, create_engine, Engine
from sqlalchemy.orm import Session

from app.institution.institution_model import Institution
from app.repositories.institution_repository_interface import InstitutionRepositoryInterface


class SQLiteInstitutionRepository(InstitutionRepositoryInterface):
    __db_path: str

    def __init__(self, db_path):
        self.__db_path = db_path

    def get_institution_exists(self, cnpj: str) -> bool:
        session = self.get_session()
        selection = select(Institution).where(Institution.cnpj.is_(cnpj))
        session.close()
        return len(session.scalars(selection).all()) == 1

    def register_institution(self, institution: Institution) -> bool:
        try:
            session = self.get_session()
            session.add(institution)
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
