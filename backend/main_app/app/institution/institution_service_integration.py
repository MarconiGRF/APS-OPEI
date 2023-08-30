import json
import requests
from app.institution.institution_service_interface import InstitutionServiceInterface


class InstitutionServiceIntegration(InstitutionServiceInterface):
    
    @classmethod
    def do_create_institution(cls, request_data: dict):
        headers = {
           "Content-Type": "application/json"
        }
        url = 'http://institutionservice:5000/institution-service/create'
        json_data = json.dumps(request_data)
        response = requests.post(url=url, data=json_data, headers=headers)
        if response.ok:
            return True
        else:
            return False

    @classmethod
    def do_edit_institution_name(cls, request_data: dict):
        headers = {
           "Content-Type": "application/json"
        }
        url = 'http://institutionservice:5000/institution-service/update-name'
        json_data = json.dumps(request_data)
        response = requests.patch(url=url, data=json_data, headers=headers)
        if response.ok:
            return True
        else:
            return False
