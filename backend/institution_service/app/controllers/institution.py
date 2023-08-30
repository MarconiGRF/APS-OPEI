from flask import Blueprint, request, abort

from app.facades.facade_impl import FacadeImpl
from app.models.institution_model import Institution

controller = Blueprint('institution_controller', __name__)


@controller.route('/create', methods=['POST'])
def do_create_institution():
    request_data = request.get_json()

    if ('institution' not in request_data) or (not isinstance(request_data['institution']['cnpj'], str)):
        abort(400)

    institution = Institution(cnpj=request_data['institution']['cnpj'])
    result = FacadeImpl.do_create_institution(institution)
    return "true" if result is True else abort(400)


@controller.route('/update-name', methods=['PATCH'])
def do_edit_institution_name():
    request_data = request.get_json()

    if ('institution' not in request_data) or (not isinstance(request_data['institution']['cnpj'], str)) or \
        (not isinstance(request_data['institution']['name'], str)):
        abort(400)

    institution = Institution(cnpj=request_data['institution']['cnpj'], name=request_data['institution']['name'])
    result = FacadeImpl.do_edit_institution_name(institution)
    return "true" if result is True else abort(400)