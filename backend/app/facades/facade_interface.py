from app.institution.institution_model import Institution


class FacadeInterface:

    @staticmethod
    def do_create_institution(institution: Institution) -> bool:
        pass
