from datetime import datetime

from app.models.delegate_model import Delegate
from app.factories.delegate_repository_factory import DelegateRepositoryFactory


class CreateDelegate:

    @staticmethod
    def get_delegate_exists(cpf: str) -> bool:
        return DelegateRepositoryFactory().get_repo().get_delegate_exists(cpf)

    @staticmethod
    def register_delegate(delegate: Delegate) -> bool:
        delegate.birthdate = datetime.strptime(delegate.birthdate, "%Y-%m-%d").date()
        return DelegateRepositoryFactory().get_repo().register_delegate(delegate)
