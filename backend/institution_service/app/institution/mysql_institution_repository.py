from app.models.institution_model import Institution
from app.repositories.institution_repository_interface import InstitutionRepositoryInterface


class MySQLInstitutionRepository(InstitutionRepositoryInterface):
    __db_host: str

    def __init__(self, db_host):
        self.__db_host = db_host

    def get_institution_exists(self, cnpj: str) -> bool:
        pass

    def register_institution(self, institution: Institution) -> bool:
        pass

    def edit_institution_name(self, institution: Institution) -> bool:
        pass

    def check_host_schemas(self):
        pass
