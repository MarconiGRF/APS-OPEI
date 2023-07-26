from flask import Blueprint, abort, request

from app.delegate.create_delegate import CreateDelegate
from app.rfb_subsystem.rfb import RFBIntegrationSubsystem

controller = Blueprint('delegate_controller', __name__, url_prefix='/delegate')


@controller.route('/', methods=['POST'])
def do_create_delegate():
    request_data = request.get_json()

    if ('cpf' not in request_data) or \
        ('birthdate' not in request_data) or \
        (not isinstance(request_data['cpf'], str)):
        abort(400)

    cpf = request_data['cpf'].replace('-', '').replace('.', '')
    birthdate = request_data['birthdate'].split('-')
    birthdate.reverse()
    birthdate = '-'.join(birthdate)
    exists = CreateDelegate.get_delegate_exists(cpf)

    if exists:
        abort(400, "delegate already exists")
    else:
        name = RFBIntegrationSubsystem.get_cpf_exists(cpf, birthdate)
        success = CreateDelegate.register_delegate(name, cpf, birthdate)
        if success:
            return "ok"

    return abort(500)
