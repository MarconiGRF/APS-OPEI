from flask import Blueprint, request, abort

from app.institution.create_institution import CreateInstitution
from app.rfb_subsystem.rfb import RFBIntegrationSubsystem

controller = Blueprint('institution_controller', __name__, url_prefix='/institution')


@controller.route('/', methods=['POST'])
def do_create_institution():
    request_data = request.get_json()

    if ('cnpj' not in request_data) or (not isinstance(request_data['cnpj'], str)):
        abort(400)

    cnpj = request_data['cnpj']
    exists = CreateInstitution.get_institution_exists(cnpj)

    if exists:
        abort(400)
    else:
        (name, address, isPublic) = RFBIntegrationSubsystem.get_cnpj_exists(cnpj)
        success = CreateInstitution.register_institution(name, address, cnpj, isPublic)
        if success:
            return "ok"

        return abort(500)
