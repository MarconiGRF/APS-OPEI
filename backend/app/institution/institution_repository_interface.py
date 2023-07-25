from sqlalchemy import select

from app.util.database_setup import DatabaseHelper
from app.institution.institution_model import Institution


class InstitutionRepositoryInterface:

    @staticmethod
    def get_institution_exists(cnpj: str) -> bool:
        session = DatabaseHelper.get_session()
        selection = select(Institution).where(Institution.cnpj.is_(cnpj))
        session.close()
        return len(session.scalars(selection).all()) == 1

    @staticmethod
    def register_institution(institution: Institution) -> bool:
        try:
            session = DatabaseHelper.get_session()
            session.add(institution)
            session.commit()
            session.close()
        except:
            return False

        return True