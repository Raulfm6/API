from flask_restx import Resource
from flask import request
from src.core.domain.entities.client import Client
from src.API.models.api_models import ApiWrapper
from src.API.entrypoint.endpoints.request_checker import RequestChecker
from src.logger import Logger
from src.settings import SqlAlchemyConfig
from src.core.infrastructure.database.client_repository import ClienteRepository

class ClientResource(Resource, RequestChecker):
    
    def __init__(self, api=None, *args, **kwargs) -> None:
        self.logger = Logger()
        self.session = SqlAlchemyConfig.getPersistenceSessionContext()
        self.SUCCESS_OPERATION = dict(
            status=200, 
            result="Operation Succeded"
        ), 200
        super().__init__(api, *args, **kwargs)
    
    @ApiWrapper.Api.expect(ApiWrapper.ClientModel, validate=True)   
    @ApiWrapper.Api.doc('Allow to register new client in data base') 
    def post(self):
        body = request.get_json()
        client = Client(**body)
        self.check_dni(dni=client.dni)
        self.check_email(email=client.email)
        
        client_repository = ClienteRepository(session=self.session)
        exist_client = client_repository.check_if_dni_exist(client.dni)
        if exist_client:
            return dict(status=500, result="DNI Already in Data Base"), 500
        
        client_repository.add_client(client=client)
        return self.SUCCESS_OPERATION
        
    @ApiWrapper.Api.expect(ApiWrapper.DNIModel, validate=True) 
    @ApiWrapper.Api.doc('Allow to get client info') 
    def get(self):
        body = request.get_json()
        dni = body.get('dni').upper()
        self.check_dni(dni=dni)
        
        client = ClienteRepository(session=self.session).get_by_dni(dni=dni)
        if not client:
            return dict(status=404, result="There isn´t a client for this DNI"), 404
        
        return dict(status=200, resultr=repr(client)), 200
    
    @ApiWrapper.Api.expect(ApiWrapper.ModifyClientModel, validate=True)   
    @ApiWrapper.Api.doc('Allow to modify data from client') 
    def put(self):
        body = request.get_json()
        dni = body.get('dni').upper()
        self.check_dni(dni=dni)

        params_to_update = body.get('params_to_update')
        email = params_to_update.get('email')
        if email:
            self.check_email(email=email)
        
        client_repository = ClienteRepository(session=self.session)
        exist_client = client_repository.check_if_dni_exist(dni)
        if not exist_client:
            return dict(status=404, result="There isn´t a client for this DNI"), 404
        
        client_repository.update_client(dni=dni, params_to_update=params_to_update)
        return self.SUCCESS_OPERATION
    
    @ApiWrapper.Api.expect(ApiWrapper.DNIModel, validate=True) 
    @ApiWrapper.Api.doc('Allow to delete client from data base') 
    def delete(self):
        body = request.get_json()
        dni = body.get('dni').upper()
        self.check_dni(dni=dni)

        client_repository = ClienteRepository(session=self.session)
        client = client_repository.get_by_dni(dni=dni)
        client_repository.delete_client(client=client)
        return self.SUCCESS_OPERATION