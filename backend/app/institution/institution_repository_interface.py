from sqlalchemy import select

from backend.app.util.database_setup import DatabaseHelper
from backend.app.institution.institution_model import Institution


class InstitutionRepositoryInterface:

    @staticmethod
    def get_institution_exists(cnpj: str) -> bool:
        session = DatabaseHelper.get_session()
        selection = select(Institution).where(Institution.cnpj.is_(cnpj))
        session.close()
        return len(session.scalars(selection).all()) == 1

    @staticmethod
    def register(institution: Institution) -> bool:
        try:
            session = DatabaseHelper.get_session()
            session.add(institution)
            session.commit()
            session.close()
        except:
            return False

        return True