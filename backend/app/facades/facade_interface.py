from app.delegate.delegate_model import Delegate
from app.institution.institution_model import Institution


class FacadeInterface:

    @staticmethod
    def do_create_institution(institution: Institution) -> bool:
        pass

    @staticmethod
    def do_create_delegate(delegate: Delegate) -> bool:
        pass
