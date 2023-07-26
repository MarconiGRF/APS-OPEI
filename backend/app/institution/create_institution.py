from app.institution.institution_model import Institution
from app.factories.institution_repository_factory import InstitutionRepositoryFactory

class CreateInstitution:

    @staticmethod
    def get_institution_exists(cnpj: str) -> bool:
        return InstitutionRepositoryFactory().get_repo().get_institution_exists(cnpj)

    @staticmethod
    def register_institution(name: str, address: str, cnpj: str, is_public: bool) -> bool:
        institution = Institution(name=name, address=address, cnpj=cnpj, isPublic=is_public)
        return InstitutionRepositoryFactory().get_repo().register_institution(institution)
