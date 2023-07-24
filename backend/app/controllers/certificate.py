from flask import Blueprint, abort, request

controller = Blueprint('certificate_controller', __name__, url_prefix='/certificate')


@controller.route('/')
def do_generate_certificate():
    request_data = request.get_json()

    if ('cpf' not in request_data) or (not isinstance(request_data['cpf'], str)):
        abort(400)

    cpf = request_data['cpf']
    return "Howdy from certificate"
