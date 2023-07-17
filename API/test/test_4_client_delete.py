from base_test import BaseTest
from src.settings import OperationResult

class TestClientDelete(BaseTest):
            
    def setup_method(self, method):
        self.setup_client()
    
    def test_delete_ok(self):
        request_body = {
            "dni": "00000000T"
        }
        response = self.test_client.delete(self.ENDPOINT, json=request_body)
        assert response.status_code == OperationResult.SUCCESS_CODE
        assert response.json['result'] == OperationResult.SUCCESS_RESULT['result']
    
    def test_delete_client_not_exist(self):
        response = self.client_not_exist(method='delete')
        assert response.status_code == OperationResult.NOT_FOUND_CODE
        assert response.json['result'] == OperationResult.CLIENT_NOT_EXIST_RESULT['result']
        
    def test_delete_dni_invalid_incorrect_lenght(self):
        response = self.dni_invalid_incorrect_lenght(method='delete')
        assert response.status_code == OperationResult.ERROR_CODE
        assert response.json['result'] == OperationResult.DNI_INCORRECT_RESULT['result']
        
    def test_delete_dni_invalid_incorrect_letter(self):
        response = self.dni_invalid_incorrect_letter(method='delete')
        assert response.status_code == OperationResult.ERROR_CODE
        assert response.json['result'] == OperationResult.DNI_INCORRECT_RESULT['result']