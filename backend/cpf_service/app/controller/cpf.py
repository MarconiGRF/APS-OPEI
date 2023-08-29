from flask import Blueprint, abort, request

from app.adapters.rfb_integration_adapter_pet_commons import RFBIntegrationAdapterPetCommons as integration

controller = Blueprint('cpf_controller', __name__, url_prefix='/person')


@controller.route('/', methods=['GET'])
def get_person_info():
    cpf = request.args.get('cpf')
    birthdate = request.args.get('birthdate')

    if (cpf is None) or (birthdate is None):
        abort(400)

    person_info = integration.get_cpf_exists(cpf, birthdate)

    return person_info if person_info is True else abort(400)