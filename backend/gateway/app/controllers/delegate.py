from flask import Blueprint, abort, request

from app.delegate.delegate_service_integration import DelegateServiceIntegration

controller = Blueprint('delegate_controller', __name__, url_prefix='/delegate')


@controller.route('/', methods=['POST'])
def do_create_delegate():
    request_data = request.get_json()

    result = DelegateServiceIntegration.do_create_delegate(request_data=request_data)
    return "true" if result is True else abort(400)
