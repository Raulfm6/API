
from sqlalchemy.orm import Session
from src.core.infrastructure.interfaces.simulation_ui import UISimulation
from src.core.domain.entities.simulation import Simulation
from src.core.infrastructure.database.sql_alchemy_controller import SqlAlchemyController


class SimulationRepository(UISimulation, SqlAlchemyController):
    
    def __init__(self, session: Session) -> None:
        super().__init__(session)
    
    def add_simulation(self, simulation: Simulation) -> None:
        self.add(model=simulation)
        self.commit()
        
    def update_simulation(self, dni:str, params_to_update: dict) -> None:
        filter = [Simulation.dni == dni]
        self.update(model=Simulation, select_filter=filter, updates=params_to_update)
        self.commit()
        
    def check_if_simulation_exist(self, dni: str) -> bool:
        filter = [Simulation.dni == dni]
        exist = self.select_one(model=Simulation, select_filter=filter)
        return exist is not None
    