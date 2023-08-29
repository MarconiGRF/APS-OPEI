from app.institution.create_institution import CreateInstitution
from app.institution.institution_model import Institution
from app.rfb_subsystem.rfb import RFBIntegrationSubsystem


class InstitutionControl:

    @staticmethod
    def do_create_institution(institution: Institution) -> bool:
        exists = CreateInstitution.get_institution_exists(institution.cnpj)

        if exists:
            return False
        else:
            (name, address, isPublic) = RFBIntegrationSubsystem.get_cnpj_exists(institution.cnpj)
            institution.name = name
            institution.address = address
            institution.isPublic = isPublic
            success = CreateInstitution.register_institution(institution)
            if success:
                return True
            pass
