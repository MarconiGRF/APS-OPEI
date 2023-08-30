from flask import Blueprint, request, abort

from app.institution.institution_service_integration import InstitutionServiceIntegration

controller = Blueprint('institution_controller', __name__, url_prefix='/institution')


@controller.route('/', methods=['POST'])
def do_create_institution():
    request_data = request.get_json()
    
    result = InstitutionServiceIntegration.do_create_institution(request_data=request_data)
    return "true" if result is True else abort(400)


@controller.route('/update-name', methods=['PATCH'])
def do_edit_institution_name():
    request_data = request.get_json()

    result = InstitutionServiceIntegration.do_edit_institution_name(request_data=request_data)
    return "true" if result is True else abort(400)