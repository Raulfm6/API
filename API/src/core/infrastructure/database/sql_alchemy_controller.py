from typing import List
from sqlalchemy.orm import Session
from src.core.infrastructure.interfaces.sql_alchemy_ui import UISqlAlchemy

class SqlAlchemyController(UISqlAlchemy):
    
    def __init__(self, session: Session):
        self.session = session

    def add(self, model: object) -> None:
        self.session.add(model)
        
    def select_one(self, model: object, select_filter: List[str]) -> object:
        result = self.session.query(model).filter(*select_filter).first()
        return result

    def select_all(self, model: object) -> None:
        result = self.session.query(model).all()
        return result

    def update(self, model: object, select_filter: list, updates: dict) -> None:
        self.session.query(model).filter(*select_filter).update(updates)

    def commit(self) -> None:
        self.session.commit()

    def delete(self, model: object) -> None:
        self.session.delete(model)
    