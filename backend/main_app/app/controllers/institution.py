from flask import Blueprint, request, abort

from app.facades.facade_impl import FacadeImpl
from app.institution.institution_model import Institution

controller = Blueprint('institution_controller', __name__, url_prefix='/institution')


@controller.route('/', methods=['POST'])
def do_create_institution():
    request_data = request.get_json()

    if ('institution' not in request_data) or (not isinstance(request_data['institution']['cnpj'], str)):
        abort(400)

    institution = Institution(cnpj=request_data['institution']['cnpj'])
    result = FacadeImpl.do_create_institution(institution)
    return "true" if result is True else abort(400)
