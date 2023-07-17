from base_test import BaseTest
from src.settings import OperationResult


class TestClientPost(BaseTest):
            
    def setup_method(self, method):
        self.setup_client()

    def test_post_ok(self):
        request_body = {
            "dni": "00000000T",
            "name": "Nombre",
            "email": "email@email.com",
            "capital": 145
        }
        response = self.test_client.post(self.ENDPOINT, json=request_body)
        assert response.status_code == OperationResult.SUCCESS_CODE
        assert response.json['result'] == OperationResult.SUCCESS_RESULT['result']
    
    def test_post_client_exist(self):
        request_body = {
            "dni": "00000000T",
            "name": "Nombre",
            "email": "email@email.com",
            "capital": 145
        }
        response = self.test_client.post(self.ENDPOINT, json=request_body)
        assert response.status_code == OperationResult.DATABASE_ERROR_CODE
        assert response.json['result'] == OperationResult.DNI_ALREADY_IN_DATABASE_RESULT['result']
        
    def test_post_dni_invalid_incorrect_lenght(self):
        response = self.dni_invalid_incorrect_lenght(method='post')
        assert response.status_code == OperationResult.ERROR_CODE
        assert response.json['result'] == OperationResult.DNI_INCORRECT_RESULT['result']
        
    def test_post_dni_invalid_incorrect_letter(self):
        response = self.dni_invalid_incorrect_letter(method='post')
        assert response.status_code == OperationResult.ERROR_CODE
        assert response.json['result'] == OperationResult.DNI_INCORRECT_RESULT['result']
        
    def test_post_email_invalid(self):
        response = self.email_invalid(method='post')
        assert response.status_code == OperationResult.ERROR_CODE
        assert response.json['result'] == OperationResult.EMAIL_INCORRECT_RESULT['result']