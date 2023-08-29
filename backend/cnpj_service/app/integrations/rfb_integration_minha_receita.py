import requests
import os


class RFBIntegrationMinhaReceita:

    @classmethod
    def get_institution_info(cls, cnpj: str):
        request = requests.get(f'{os.getenv("CNPJ_API_ADDR")}/{cnpj}')
        data = request.json()

        return data
    
