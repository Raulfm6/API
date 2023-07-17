from base_test import BaseTest
from src.settings import OperationResult
from src.core.domain.entities.client import Client

class TestClientGet(BaseTest):
            
    def setup_method(self, method):
        self.setup_client()
    
    def test_get_ok(self):
        request_body = {
            "dni": "99999999R"
        }
        assert_client = Client(id=1, dni='99999999R', name='Otro', email='otro@otro.es', capital=100.0)
        response = self.test_client.get(self.ENDPOINT, json=request_body)
        assert response.status_code == OperationResult.SUCCESS_CODE
        assert response.json['result'] == assert_client.toJson()
    
    def test_get_client_not_exist(self):
        response = self.client_not_exist(method='get')
        assert response.status_code == OperationResult.NOT_FOUND_CODE
        assert response.json['result'] == OperationResult.CLIENT_NOT_EXIST_RESULT['result']
        
    def test_get_dni_invalid_incorrect_lenght(self):
        response = self.dni_invalid_incorrect_lenght(method='get')
        assert response.status_code == OperationResult.ERROR_CODE
        assert response.json['result'] == OperationResult.DNI_INCORRECT_RESULT['result']
        
    def test_get_dni_invalid_incorrect_letter(self):
        response = self.dni_invalid_incorrect_letter(method='get')
        assert response.status_code == OperationResult.ERROR_CODE
        assert response.json['result'] == OperationResult.DNI_INCORRECT_RESULT['result']