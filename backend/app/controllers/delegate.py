from flask import Blueprint, abort, request

controller = Blueprint('delegate_controller', __name__, url_prefix='/delegate')


@controller.route('/', methods=['POST'])
def do_create_delegate():
    request_data = request.get_json()

    if ('cpf' not in request_data) or (not isinstance(request_data['cpf'], str)):
        abort(400)

    cpf = request_data['cpf']
    return "Howdy from delegate"
