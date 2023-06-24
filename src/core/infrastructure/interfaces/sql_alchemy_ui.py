from abc import ABC, abstractmethod
from typing import List


class UISqlAlchemy(ABC):
    
    @abstractmethod
    def add(self, model: dict) -> None:
        raise NotImplementedError
    
    @abstractmethod
    def select_one(self, model: object, select_filter: List[str]) -> object:
        raise NotImplementedError
    
    @abstractmethod
    def select_all(self, model: object) -> List[object]:
        raise NotImplementedError
    
    @abstractmethod
    def update(self, model: object, select_filter: list, updates: object) -> None:
        raise NotImplementedError
    
    @abstractmethod
    def commit(self) -> None:
        raise NotImplementedError
    
    @abstractmethod
    def delete(self, model: object) -> None:
        raise NotImplementedError
