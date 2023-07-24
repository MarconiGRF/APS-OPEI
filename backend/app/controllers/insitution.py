from flask import Blueprint, request, abort

from backend.app.business.create_institution import CreateInstitution
from backend.app.services.rfb import RFBService

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
        (name, address, isPublic) = RFBService.get_cnpj_exists(cnpj)
        return CreateInstitution.register_institution(name, address, cnpj, isPublic)
