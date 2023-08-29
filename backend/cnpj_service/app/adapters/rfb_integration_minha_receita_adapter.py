import json
from app.integrations.rfb_integration_minha_receita import RFBIntegrationMinhaReceita
from app.integrations.rfb_integration_interface import RFBIntegrationInferface


class RFBIntegrationMinhaReceitaAdapter(RFBIntegrationInferface, RFBIntegrationMinhaReceita):

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
