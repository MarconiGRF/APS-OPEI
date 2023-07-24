from sqlalchemy import select

from backend.app.data.database_setup import DatabaseHelper
from backend.app.models.institution import Institution


class InstitutionRepository:

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