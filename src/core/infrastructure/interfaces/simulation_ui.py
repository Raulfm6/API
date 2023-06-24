    
from abc import ABC,abstractmethod


class UISimulation(ABC):
    
    @abstractmethod   
    def add_simulation(self, simulation: object) -> None:
        raise NotImplementedError