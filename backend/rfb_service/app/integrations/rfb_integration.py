import requests
import os


class RFBIntegration:

    @classmethod
    def get_institution_info(cls, cnpj: str):
        request = requests.get(f'{os.getenv("CNPJ_API_ADDR")}/{cnpj}')
        data = request.json()

        return (
            data['nome_fantasia'],
            data['descricao_tipo_de_logradouro'] +
            ' ' + data['logradouro'] +
            ', ' + data['numero'] +
            ', cep ' + data['cep'] +
            ', ' + (data['municipio'] if data['municipio'] else ''),
            False
        )
    
    @classmethod
    def get_person_info(cls, cpf: str, birthdate: str):
        request = requests.get(f'{os.getenv("CPF_API_ADDR")}/{cpf}?birthdate={birthdate}')
        data = request.json()

        return data['nome']
