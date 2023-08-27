from flask import Blueprint, abort, request

from app.adapters.rfb_integration_adapter import RFBIntegrationAdapter as integration

controller = Blueprint('rfb_controller', __name__, url_prefix='/rfb')


@controller.route('/institution', methods=['GET'])
def get_institution_info():
    cnpj = request.args.get('cnpj')

    if (cnpj is None):
        abort(400)

    institution_info = integration.get_cnpj_exists(cnpj)

    return institution_info if institution_info is True else abort(400)


@controller.route('/delegate', methods=['GET'])
def get_delegate_info():
    cpf = request.args.get('cpf')
    birthdate = request.args.get('birthdate')

    if (cpf is None) or (birthdate is None):
        abort(400)

    delegate_info = integration.get_cpf_exists(cpf, birthdate)

    return delegate_info if delegate_info is True else abort(400)