from base_test import BaseTest
from src.settings import OperationResult

class TestClientPut(BaseTest):
            
    def setup_method(self, method):
        self.setup_client()
    
    def test_put_ok(self):
        request_body = {
            "dni": "00000000T",
            "params_to_update": {
                "name": "Update",
                "email": "update@update.es",
                "capital": 999
            }
        }
        response = self.test_client.put(self.ENDPOINT, json=request_body)
        assert response.status_code == OperationResult.SUCCESS_CODE
        assert response.json['result'] == OperationResult.SUCCESS_RESULT['result']
    
    def test_put_client_not_exist(self):
        request_body = {
            "dni": "73856515L",
            "params_to_update": {
                "name": "Nombre",
                "email": "email@email.com",
                "capital": 145
            }
        }
        response = self.test_client.put(self.ENDPOINT, json=request_body)
        assert response.status_code == OperationResult.NOT_FOUND_CODE
        assert response.json['result'] == OperationResult.CLIENT_NOT_EXIST_RESULT['result']
        
    def test_put_dni_invalid_incorrect_lenght(self):
        request_body = {
            "dni": "000000T",
            "params_to_update": {
                "name": "Nombre",
                "email": "email@email.com",
                "capital": 145
            }
        }
        response = self.test_client.put(self.ENDPOINT, json=request_body)
        assert response.status_code == OperationResult.ERROR_CODE
        assert response.json['result'] == OperationResult.DNI_INCORRECT_RESULT['result']
        
    def test_put_dni_invalid_incorrect_letter(self):
        request_body = {
            "dni": "00000000Z",
            "params_to_update": {
                "name": "Nombre",
                "email": "email@email.com",
                "capital": 145
            }
        }
        response = self.test_client.put(self.ENDPOINT, json=request_body)
        assert response.status_code == OperationResult.ERROR_CODE
        assert response.json['result'] == OperationResult.DNI_INCORRECT_RESULT['result']
        
    def test_put_email_invalid(self):
        request_body = {
            "dni": "00000000T",
            "params_to_update": {
                "name": "Nombre",
                "email": "email#email.com",
                "capital": 145
            }
        }
        response = self.test_client.put(self.ENDPOINT, json=request_body)
        assert response.status_code == OperationResult.ERROR_CODE
        assert response.json['result'] == OperationResult.EMAIL_INCORRECT_RESULT['result']