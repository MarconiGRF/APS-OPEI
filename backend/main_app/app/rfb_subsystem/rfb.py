import requests
import os

from app.rfb_subsystem.rfb_integration_interface import RFBIntegrationInterface

class RFBIntegrationSubsystem(RFBIntegrationInterface):

    @classmethod
    def get_cnpj_exists(cls, cnpj: str):
        params = {'cnpj': cnpj}
        request = requests.get('http://cnpjservice:5000/rfb-cnpj/institution/', params=params)
        data = request.json()

        return (
            data['nome_fantasia'],
            data['endereço'],
            data['publica']
        )
    
    @classmethod
    def get_cpf_exists(cls, cpf: str, birthdate: str):
        params = {'cpf': cpf, 'birthdate': birthdate}
        request = requests.get('http://cpfservice:5000/rfb-cpf/person/', params=params)
        print(request)
        data = request.json()

        return data['nome']
