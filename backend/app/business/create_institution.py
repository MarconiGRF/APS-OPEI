from backend.app.models.institution import Institution
from backend.app.repositories.institution import InstitutionRepository

class CreateInstitution:

    @staticmethod
    def get_institution_exists(cnpj: str) -> bool:
        return InstitutionRepository.get_institution_exists(cnpj)

    @staticmethod
    def register_institution(name: str, address: str, cnpj: str, is_public: bool) -> bool:
        institution = Institution(name=name, address=address, cnpj=cnpj, isPublic=is_public)
        return InstitutionRepository.register(institution)
