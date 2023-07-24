import requests
import os


class RFBService:

    @classmethod
    def get_cnpj_exists(cls, cnpj: str):
        request = requests.get(f'{os.getenv("CNPJ_API_ADDR")}/{cnpj}')
        data = request.json()

        return (
            data['nome_fantasia'],
            data['descricao_tipo_de_logradouro'] +
            ' ' + data['logradouro'] +
            ', ' + data['numero'] +
            ', cep ' + data['cep'] +
            ', ' + data['municipio'],
            False
        )
