import os

from sqlalchemy import create_engine, Engine

from app.models.delegate_model import Delegate
from app.delegate.mysql_delegate_repository import MySQLDelegateRepository
from app.delegate.sqlite_delegate_repository import SQLiteDelegateRepository
from app.repositories.delegate_repository_interface import DelegateRepositoryInterface


class DelegateRepositoryFactory:
    __db_path: str = f'{os.getcwd()}/app/repositories/opei2023.db'
    __mysql_host: str = f'mysql:///{os.getenv("MYSQL_HOST")}:3306'
    db_type: str

    def __init__(self):
        pass

    def get_repo(self) -> DelegateRepositoryInterface:
        self.db_type = os.getenv("DB_TYPE")
        if self.db_type == 'sqlite':
            repo = SQLiteDelegateRepository(self.__db_path)
            repo.check_db_file()
            self._create_tables()
            return repo
        elif self.db_type == 'mysql':
            repo = MySQLDelegateRepository(self.__mysql_host)
            repo.check_host_schemas()
            self._create_tables()
            return repo

    def get_engine(self) -> Engine:
        if self.db_type == 'sqlite':
            return create_engine(f'sqlite:///{self.__db_path}')
        elif self.db_type == 'mysql':
            return create_engine(self.__mysql_host)

    def _create_tables(self) -> None:
        engine = self.get_engine()
        Delegate.metadata.create_all(engine)
