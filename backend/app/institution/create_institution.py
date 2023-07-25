from backend.app.institution.institution_model import Institution
from backend.app.institution.institution_repository_interface import InstitutionRepositoryInterface

class CreateInstitution:

    @staticmethod
    def get_institution_exists(cnpj: str) -> bool:
        return InstitutionRepositoryInterface.get_institution_exists(cnpj)

    @staticmethod
    def register_institution(name: str, address: str, cnpj: str, is_public: bool) -> bool:
        institution = Institution(name=name, address=address, cnpj=cnpj, isPublic=is_public)
        return InstitutionRepositoryInterface.register(institution)
