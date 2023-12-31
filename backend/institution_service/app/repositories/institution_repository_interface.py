from sqlalchemy import Engine
from sqlalchemy.orm import Session

from app.models.institution_model import Institution


class InstitutionRepositoryInterface:
    def get_institution_exists(self, cnpj: str) -> bool:
        pass
    def register_institution(self, institution: Institution) -> bool:
        pass
    def edit_institution_name(self, institution: Institution) -> bool:
        pass
    def get_engine(self) -> Engine:
        pass
    def get_session(self) -> Session:
        pass