from sqlalchemy import Engine
from sqlalchemy.orm import Session

from app.delegate.delegate_model import Delegate


class DelegateRepositoryInterface:
    def get_delegate_exists(self, cpf: str) -> bool:
        pass
    def register_delegate(self, delegate: Delegate) -> bool:
        pass
    def get_engine(self) -> Engine:
        pass
    def get_session(self) -> Session:
        pass
