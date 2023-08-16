from app.facades.facade_interface import FacadeInterface
from app.delegate.delegate_control import DelegateControl
from app.delegate.delegate_model import Delegate
from app.institution.institution_control import InstitutionControl
from app.institution.institution_model import Institution

class FacadeImpl(FacadeInterface):

    @staticmethod
    def do_create_institution(institution: Institution) -> bool:
        return InstitutionControl.do_create_institution(institution)

    @staticmethod
    def do_create_delegate(delegate: Delegate) -> bool:
        return DelegateControl.do_create_delegate(delegate)
