import json
from app.integrations.rfb_integration import RFBIntegration
from app.integrations.rfb_integration_interface import RFBIntegrationInferface


class RFBIntegrationAdapter(RFBIntegrationInferface, RFBIntegration):

    @classmethod
    def get_cnpj_exists(cls, cnpj: str):
        data = cls.get_institution_info(cnpj)

        json_dict = {
            'nome_fantasia': data['nome_fantasia'],
            'endereço': data['descricao_tipo_de_logradouro'] +
            ' ' + data['logradouro'] +
            ', ' + data['numero'] +
            ', cep ' + data['cep'] +
            ', ' + (data['municipio'] if data['municipio'] else ''),
            'publica': False
        }
        
        return json.dumps(json_dict)

    @classmethod
    def get_cpf_exists(cls, cpf: str, birthdate: str):
        data = cls.get_person_info(cpf, birthdate)

        json_dict = {'nome': data['nome']}

        return json.dumps(json_dict)