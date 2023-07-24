import os

from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import Session
from backend.app.models.delegate import Delegate
from backend.app.models.institution import Institution


class DatabaseHelper:
    __db_path = f'{os.getcwd()}/app/data/opei2023.db'

    @classmethod
    def get_engine(cls) -> Engine:
        return create_engine(f'sqlite:///{cls.__db_path}', echo=True)

    @classmethod
    def create_tables(cls) -> None:
        engine = cls.get_engine()
        Delegate.metadata.create_all(engine)
        Institution.metadata.create_all(engine)

    @classmethod
    def check_db_file(cls) -> None:

        if not os.path.exists(cls.__db_path):
            open(cls.__db_path, "x")
            cls.create_tables()

    @classmethod
    def get_session(cls) -> Session:
        cls.check_db_file()

        return Session(cls.get_engine())
