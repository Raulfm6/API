
from sqlalchemy.orm import Session
from sqlite3 import IntegrityError
from src.core.infrastructure.interfaces.client_ui import UIClient
from src.core.domain.entities.client import Client
from src.core.infrastructure.database.sql_alchemy_controller import SqlAlchemyController


class ClienteRepository(UIClient, SqlAlchemyController):
    
    def __init__(self, session: Session) -> None:
        super().__init__(session)
    
    def add_client(self, client: Client) -> None:
        self.add(model=client)
        self.commit()

    def update_client(self, dni: str, params_to_update: dict) -> None:
        filter = [Client.dni == dni]
        self.update(model=Client, select_filter=filter, updates=params_to_update)
        self.commit()
        pass

    def delete_client(self, client: Client) -> bool:
        self.delete(model=client)
        self.commit()
        pass

    
    def check_if_dni_exist(self, dni: str) -> bool:
        filter = [Client.dni == dni]
        client = self.select_one(model=Client, select_filter=filter)
        return client is not None
        
    def get_by_dni(self, dni: str) -> Client:
        filter = [Client.dni == dni]
        client = self.select_one(model=Client, select_filter=filter)
        return client
