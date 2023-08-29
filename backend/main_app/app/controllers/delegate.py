from flask import Blueprint, abort, request

from app.delegate.delegate_model import Delegate
from app.facades.facade_impl import FacadeImpl

controller = Blueprint('delegate_controller', __name__, url_prefix='/delegate')


@controller.route('/', methods=['POST'])
def do_create_delegate():
    request_data = request.get_json()

    if ('delegate' not in request_data) or (not isinstance(request_data['delegate']['birthdate'], str)) or \
        (not isinstance(request_data['delegate']['cpf'], str)):
        abort(400)

    cpf = request_data['delegate']['cpf'].replace('-', '').replace('.', '')
    birthdate = request_data['delegate']['birthdate'].split('-')
    birthdate.reverse()
    birthdate = '-'.join(birthdate)

    delegate = Delegate(cpf=cpf, birthdate=birthdate)
    result = FacadeImpl.do_create_delegate(delegate)
    return "true" if result is True else abort(400)
