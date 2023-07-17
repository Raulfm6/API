from base_test import BaseTest
from src.settings import OperationResult
from src.API.entrypoint.endpoints.simulation_endpoints import SimulationResource

class TestSimulationPost(BaseTest):
            
    def setup_method(self, method):
        self.setup_simulation()

    def test_post_ok(self):
        request_body = {
            "dni": "99999999R",
            "tae": 10,
            "term": 10
        }
        client = self.test_client.get('/api/client', json={"dni": "99999999R"}).json['result']
        response = self.test_client.post(self.ENDPOINT, json=request_body)
        quota, term = SimulationResource.calculate_quota_and_return_import(
            capital=client['capital'], 
            tae= request_body['tae'],
            term=request_body['term']
        )
        assert response.status_code == 200
        assert response.json['result'] == f'Quota: {quota}, Importe Total: {term}'
    
    def test_post_client_not_exist(self):
        request_body = {
            "dni": "73856515L",
            "tae": 10,
            "term": 5
        }
        response = self.test_client.post(self.ENDPOINT, json=request_body)
        assert response.status_code == OperationResult.NOT_FOUND_CODE
        assert response.json['result'] == OperationResult.CLIENT_NOT_EXIST_RESULT['result']
        
    def test_post_dni_invalid_incorrect_lenght(self):
        request_body = {
            "dni": "9999999R",
            "tae": 10,
            "term": 5
        }
        response = self.test_client.post(self.ENDPOINT, json=request_body)
        assert response.status_code == OperationResult.ERROR_CODE
        assert response.json['result'] == OperationResult.DNI_INCORRECT_RESULT['result']
        
    def test_post_dni_invalid_incorrect_letter(self):
        request_body = {
            "dni": "99999999Z",
            "tae": 10,
            "term": 5
        }
        response = self.test_client.post(self.ENDPOINT, json=request_body)
        assert response.status_code == OperationResult.ERROR_CODE
        assert response.json['result'] == OperationResult.DNI_INCORRECT_RESULT['result']
    
    def test_post_tae_zero(self):
        request_body = {
            "dni": "99999999R",
            "tae": 0,
            "term": 5
        }
        response = self.test_client.post(self.ENDPOINT, json=request_body)
        assert response.status_code == OperationResult.ERROR_CODE
        assert response.json['result'] == OperationResult.TAE_TERM_INCORRECT_RESULT['result']
        
    def test_post_tae_negative(self):
        request_body = {
            "dni": "99999999R",
            "tae": -10,
            "term": 5
        }
        response = self.test_client.post(self.ENDPOINT, json=request_body)
        assert response.status_code == OperationResult.ERROR_CODE
        assert response.json['result'] == OperationResult.TAE_TERM_INCORRECT_RESULT['result']
        
    def test_post_term_zero(self):
        request_body = {
            "dni": "99999999R",
            "tae": 10,
            "term": 0
        }
        response = self.test_client.post(self.ENDPOINT, json=request_body)
        assert response.status_code == OperationResult.ERROR_CODE
        assert response.json['result'] == OperationResult.TAE_TERM_INCORRECT_RESULT['result']
            
    def test_post_term_negative(self):
        request_body = {
            "dni": "99999999R",
            "tae": 10,
            "term": -5
        }
        response = self.test_client.post(self.ENDPOINT, json=request_body)
        assert response.status_code == OperationResult.ERROR_CODE
        assert response.json['result'] == OperationResult.TAE_TERM_INCORRECT_RESULT['result']