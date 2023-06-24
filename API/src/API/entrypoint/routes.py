from flask_restx import Namespace
from src.API.entrypoint.endpoints.client_endpoints import ClientResource
from src.API.entrypoint.endpoints.simulation_endpoints import SimulationResource

class Namespaces:
    
    ns = Namespace('', description='Root Namespace')   
    
    @staticmethod
    def create_namespaces():
        
        name_spaces = Namespaces.ns
        name_spaces.add_resource(ClientResource, "/client")
        name_spaces.add_resource(SimulationResource, "/simulation")
        
        return name_spaces
    
