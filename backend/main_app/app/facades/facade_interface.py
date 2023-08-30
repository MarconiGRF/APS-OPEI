from app.delegate.delegate_model import Delegate

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class FacadeInterface(metaclass=Singleton):

    @staticmethod
    def do_create_delegate(delegate: Delegate) -> bool:
        pass
