import json
from app.integrations.rfb_integration_pet_commons import RFBIntegrationPetCommons
from app.integrations.rfb_integration_interface import RFBIntegrationInferface


class RFBIntegrationAdapterPetCommons(RFBIntegrationInferface, RFBIntegrationPetCommons):

    @classmethod
    def get_cpf_exists(cls, cpf: str, birthdate: str):
        data = cls.get_person_info(cpf, birthdate)

        json_dict = {'nome': data['nome']}

        return json.dumps(json_dict)