from src.API.entrypoint.api import ApiRest

class BaseTest():
    
    test_client = ApiRest.init_api().test_client()
    REQUEST_TYPE = dict(
            post = test_client.post,
            get = test_client.get,
            put = test_client.put,
            patch = test_client.patch,
            delete = test_client.delete
        )
    
    def setup_client(self):
        self.ENDPOINT = '/api/client'
        self.test_client = BaseTest.test_client
        self.test_client.testing = True
    
    def setup_simulation(self):
        self.ENDPOINT = '/api/simulation'
        self.test_client = BaseTest.test_client
        self.test_client.testing = True
    
    def client_not_exist(self,method):
        request_body = {
            "dni": "73856515L"
        }
        response = BaseTest.REQUEST_TYPE[method](self.ENDPOINT, json=request_body)
        return response
        
    def dni_invalid_incorrect_lenght(self,method):
        request_body = {
            "dni": "0000000T",
            "name": "Nombre",
            "email": "email@email.com",
            "capital": 145
        }
        response = BaseTest.REQUEST_TYPE[method](self.ENDPOINT, json=request_body)
        return response
        
    def dni_invalid_incorrect_letter(self, method):
        request_body = {
            "dni": "00000000Z",
            "name": "Nombre",
            "email": "email@email.com",
            "capital": 145
        }
        response = BaseTest.REQUEST_TYPE[method](self.ENDPOINT, json=request_body)
        return response
        
    def email_invalid(self, method):
        request_body = {
            "dni": "00000000T",
            "name": "Nombre",
            "email": "email#email.com",
            "capital": 145
        }
        response = BaseTest.REQUEST_TYPE[method](self.ENDPOINT, json=request_body)
        return response
        