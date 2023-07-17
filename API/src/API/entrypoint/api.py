from flask import Flask, Blueprint, request
from src.API.models.api_models import ApiWrapper
from src.API.entrypoint.routes import Namespaces
from src.logger import Logger

class ApiRest:       
         
    logger = Logger()
    
    @staticmethod
    def init_api():
        
        ApiRest.logger.info('Initialazing API...')
        
        app = Flask(__name__)
        
        ns = Namespaces.create_namespaces()
        ApiWrapper.Api.add_namespace(ns, path='')
        
        blue_print = Blueprint('api', __name__, url_prefix="/api")
        ApiWrapper.Api.init_app(blue_print)
        app.register_error_handler(404, ApiRest.not_found_error_handler)
        
        app.register_blueprint(blue_print)
        
        return app
        

    @staticmethod
    def not_found_error_handler(error):
        path = request.path
        
        errorMessage = f'Path {path} not found in the server'
        message = f'{error.code} Bad Request.'
        logMessage = f'{message}. {errorMessage}'
        
        ApiRest.logger.error(f'{logMessage}')
        
        error.response = dict(
            status='KO',
            message=errorMessage
        )

        return error.response, error.code