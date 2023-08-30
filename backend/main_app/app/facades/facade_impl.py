from app.facades.facade_interface import FacadeInterface
from app.delegate.delegate_control import DelegateControl
from app.delegate.delegate_model import Delegate

class FacadeImpl(FacadeInterface):

    @staticmethod
    def do_create_delegate(delegate: Delegate) -> bool:
        return DelegateControl.do_create_delegate(delegate)
