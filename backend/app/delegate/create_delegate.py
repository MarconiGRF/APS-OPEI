from datetime import datetime

from app.delegate.delegate_model import Delegate
from app.delegate.delegate_repository_interface import DelegateRepositoryInterface

class CreateDelegate:

    @staticmethod
    def get_delegate_exists(cpf: str) -> bool:
        return DelegateRepositoryInterface.get_delegate_exists(cpf)

    @staticmethod
    def register_delegate(name: str, cpf: str, birthdate_str: str) -> bool:
        birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d").date()
        delegate = Delegate(name=name, cpf=cpf, birthdate=birthdate)
        
        return DelegateRepositoryInterface.register_delegate(delegate)
