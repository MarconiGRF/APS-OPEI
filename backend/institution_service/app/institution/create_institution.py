from app.models.institution_model import Institution
from app.factories.institution_repository_factory import InstitutionRepositoryFactory

class CreateInstitution:

    @staticmethod
    def get_institution_exists(cnpj: str) -> bool:
        return InstitutionRepositoryFactory().get_repo().get_institution_exists(cnpj)

    @staticmethod
    def register_institution(institution: Institution) -> bool:
        return InstitutionRepositoryFactory().get_repo().register_institution(institution)
    
    @staticmethod
    def edit_institution_name(institution: Institution) -> bool:
        return InstitutionRepositoryFactory().get_repo().edit_institution_name(institution)
