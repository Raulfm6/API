
from werkzeug.exceptions import BadRequest, MethodNotAllowed
from flask_restx import Api, fields
from flask import request
from src.logger import Logger

class ApiWrapper:
    
    Api = Api(version='1.0', title='API', description='Mi API para clientes', doc='', prefix='/api')
    
    ClientModel = Api.model('Client model', {
        'dni': fields.String(required=True, description='Client`s DNI'),
        'name': fields.String(required=True, description='Client´s name'),
        'email': fields.String(required=True, description='Client´s email'),
        'capital': fields.Float(required=True, description='Client´s capital'),
    })
    
    DNIModel = Api.model('DNI model', {
        'dni': fields.String(required=True, description='Client`s DNI'),
    })
    
    
    ClientUpdateParams = Api.model('Params to update client information', {
        'name': fields.String(required=False, description='Client´s name'),
        'email': fields.String(required=False, description='Client´s email'),
        'capital': fields.Float(required=False, description='Client´s capital'),
    })
    
    ModifyClientModel = Api.model('Modify client model', {
        'dni': fields.String(required=True, description='Client`s DNI'),
        'params_to_update': fields.Nested(ClientUpdateParams, required=True, description='Client params to update'),
    })
    
    SimulationModel = Api.model('Simulation model', {
        'dni': fields.String(required=True, description='Client`s DNI'),
        'tae': fields.Float(required=True, description='Mortgage`s TAE'),
        'term': fields.Integer(required=True, description='Amortization term'),
    })
    
    #! - - - - - - - - - - - - - - - - - - - - - - Custom Exceptions - - - - - - - - - - - - - - - - - - - - - - - - - - - !#
    #! - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - !#
    
    @staticmethod
    @Api.errorhandler(BadRequest)
    def bad_request_allowed_error_handler(error):

        if not error.response:
            error.response = 'Request body cannot be null'
            
        errorMessage = error.description
        message = f'{error.code} BadRequest'
        logMessage = f'{message}. {errorMessage}'
        
        Logger().error(f'{logMessage}')
        
        response = dict(
            status='KO',
            result=error.response
        )

        return response, error.code

    @staticmethod
    @Api.errorhandler(MethodNotAllowed)
    def method_not_allowed_error_handler(error):
        path = request.path
        method = request.method
        
        errorMessage = f'Method {method} not allowed for {path} endpoint'
        message = f'{error.code} Method Not Allowed'
        logMessage = f'{message}. {errorMessage}'
        
        Logger().error(f'{logMessage}')
        
        response = dict(
            status='KO',
            result=errorMessage
        )

        return response, error.code

    