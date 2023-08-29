import requests
import os


class RFBIntegrationPetCommons:
    
    @classmethod
    def get_person_info(cls, cpf: str, birthdate: str):
        request = requests.get(f'{os.getenv("CPF_API_ADDR")}/{cpf}?birthdate={birthdate}')
        data = request.json()

        return data
