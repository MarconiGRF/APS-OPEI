import json
import requests
from app.delegate.delegate_service_interface import DelegateServiceInterface


class DelegateServiceIntegration(DelegateServiceInterface):
    
    @classmethod
    def do_create_delegate(cls, request_data: dict):
        headers = {
           "Content-Type": "application/json"
        }
        url = 'http://delegateservice:5000/delegate-service/create'
        json_data = json.dumps(request_data)
        response = requests.post(url=url, data=json_data, headers=headers)
        if response.ok:
            return True
        else:
            return False
