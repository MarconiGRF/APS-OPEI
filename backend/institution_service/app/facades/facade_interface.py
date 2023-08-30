from app.models.institution_model import Institution

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class FacadeInterface(metaclass=Singleton):

    @staticmethod
    def do_create_institution(institution: Institution) -> bool:
        pass

    @staticmethod
    def do_edit_institution_name(institution: Institution) -> bool:
        pass

