from flask import Blueprint, abort, request

from app.adapters.rfb_integration_minha_receita_adapter import RFBIntegrationMinhaReceitaAdapter as integration

controller = Blueprint('cnpj_controller', __name__, url_prefix='/institution')


@controller.route('/', methods=['GET'])
def get_institution_info():
    cnpj = request.args.get('cnpj')

    if (cnpj is None):
        abort(400)

    institution_info = integration.get_cnpj_exists(cnpj)

    return institution_info if 'nome_fantasia' in institution_info else abort(400)
