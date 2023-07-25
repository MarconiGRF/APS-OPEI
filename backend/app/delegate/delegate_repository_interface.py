import datetime
from sqlalchemy import select

from app.util.database_setup import DatabaseHelper
from app.delegate.delegate_model import Delegate

class DelegateRepositoryInterface:

    @staticmethod
    def get_delegate_exists(cpf: str) -> bool:
        session = DatabaseHelper.get_session()
        selection = select(Delegate).where(Delegate.cpf.is_(cpf))
        session.close()
        return len(session.scalars(selection).all()) == 1

    @staticmethod
    def register_delegate(delegate: Delegate) -> bool:
        try:
            session = DatabaseHelper.get_session()
            session.add(delegate)
            session.commit()
            session.close()
        except:
            return False
        
        return True
