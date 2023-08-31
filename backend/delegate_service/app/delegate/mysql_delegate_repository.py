from app.models.delegate_model import Delegate
from app.repositories.delegate_repository_interface import DelegateRepositoryInterface


class MySQLDelegateRepository(DelegateRepositoryInterface):
    __db_host: str

    def __init__(self, db_host):
        self.__db_host = db_host

    def get_delegate_exists(self, cpf: str) -> bool:
        pass

    def register_delegate(self, delegate: Delegate) -> bool:
        pass

    def check_host_schemas(self):
        pass
