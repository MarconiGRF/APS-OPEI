from app.facades.facade_interface import FacadeInterface
from app.institution.institution_control import InstitutionControl
from app.models.institution_model import Institution

class FacadeImpl(FacadeInterface):

    @staticmethod
    def do_create_institution(institution: Institution) -> bool:
        return InstitutionControl.do_create_institution(institution)
    
    @staticmethod
    def do_edit_institution_name(institution: Institution) -> bool:
        return InstitutionControl.do_edit_institution_name(institution)

