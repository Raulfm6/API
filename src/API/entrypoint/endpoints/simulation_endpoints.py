from flask_restx import Resource
from flask import request
from src.API.models.api_models import ApiWrapper
from src.logger import Logger
from src.settings import SqlAlchemyConfig
from src.core.infrastructure.database.client_repository import ClienteRepository
from src.core.infrastructure.database.simulation_repository import SimulationRepository
from src.API.entrypoint.endpoints.request_checker import RequestChecker
from src.core.domain.entities.simulation import Simulation

class SimulationResource(Resource, RequestChecker):
    
    def __init__(self, api=None, *args, **kwargs) -> None:
        self.logger = Logger()
        self.session = SqlAlchemyConfig.getPersistenceSessionContext()
        super().__init__(api, *args, **kwargs)
        
    @ApiWrapper.Api.expect(ApiWrapper.SimulationModel, validate=True)   
    @ApiWrapper.Api.doc('Allow to make a mortgage simulation') 
    def post(self):
        
        body = request.get_json()
        dni = body.get('dni').upper()
        self.check_dni(dni=dni)
        
        client = ClienteRepository(session=self.session).get_by_dni(dni=dni)
        if not client:
            return dict(status=404, result="There isn´t a client for this DNI"), 404
        
        tae = body.get('tae')
        term = body.get('term')
        
        self.check_simulation_params(tae=tae, term=term)
        
        quota, return_import = self.__calculate_quota_and_return_import(tae=tae, term=term, capital=client.capital)
        
        simulation = Simulation(dni=dni, quota=quota, return_import=return_import)
        simulation_repository = SimulationRepository(session=self.session)
        simulation_exist = simulation_repository.check_if_simulation_exist(dni=dni)
        
        if simulation_exist:
            simulation_repository.update_simulation(dni=dni, params_to_update=dict(quota=quota, return_import=return_import))
        else:
            simulation_repository.add_simulation(simulation=simulation)
            
        return dict(success=200, result=f"Quota: {quota}, Importe Total: {return_import}"),200
    
    
    @staticmethod
    def __calculate_quota_and_return_import(tae, term, capital):
        NUMBER_OF_MONTHS = 12
        PERCENTAGE = 100
        
        type_of_monthly_interes = (tae / PERCENTAGE / NUMBER_OF_MONTHS)
        number_of_payments = (term * NUMBER_OF_MONTHS)
        
        divisor = pow((type_of_monthly_interes - (1 + type_of_monthly_interes)), -number_of_payments)
        
        quota = capital * type_of_monthly_interes / divisor
        return_import = quota * number_of_payments
        
        return quota, return_import