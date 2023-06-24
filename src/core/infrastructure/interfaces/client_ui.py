   
    
from abc import ABC,abstractmethod


class UIClient(ABC):
    
    @abstractmethod   
    def add_client(self, client: object) -> None:
        raise NotImplementedError
    
    @abstractmethod   
    def update_client(self, dni: str, params_to_update: dict) -> None:
        raise NotImplementedError
    
    @abstractmethod   
    def delete_client(self, client: object) -> bool:
        raise NotImplementedError
    
    @abstractmethod   
    def get_by_dni(self, dni: str) -> object:
        raise NotImplementedError
    
    @abstractmethod   
    def check_if_dni_exist(self, dni: str) -> bool:
        raise NotImplementedError