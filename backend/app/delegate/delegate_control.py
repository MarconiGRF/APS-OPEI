from app.delegate.create_delegate import CreateDelegate
from app.delegate.delegate_model import Delegate
from app.rfb_subsystem.rfb import RFBIntegrationSubsystem


class DelegateControl:

    @staticmethod
    def do_create_delegate(delegate: Delegate) -> bool:
        exists = CreateDelegate.get_delegate_exists(delegate.cpf)

        if exists:
            return False

        delegate.name = RFBIntegrationSubsystem.get_cpf_exists(delegate.cpf, delegate.birthdate)
        success = CreateDelegate.register_delegate(delegate)
        if success:
            return True