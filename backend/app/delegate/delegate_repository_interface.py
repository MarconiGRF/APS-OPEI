import datetime


class InstitutionRepositoryInterface:

    @staticmethod
    def get_delegate_exists(cpf: str) -> bool:
        pass

    @staticmethod
    def register_delegate(cpf: str, name: str, email: str, birthdate: datetime.date) -> bool:
        pass
