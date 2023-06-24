from sqlalchemy import Column, MetaData, Table, ForeignKey
from sqlalchemy.types import INTEGER, VARCHAR, TEXT, FLOAT
from sqlalchemy.orm import registry

from src.core.domain.entities.simulation import Simulation
from src.core.domain.entities.client import Client

metadata = MetaData()
mapper_registry = registry()

client_schema = Table(
    'clients',
    metadata,
    Column('id', INTEGER, primary_key=True),
    Column('name', TEXT, nullable=False),
    Column('dni', VARCHAR(9), nullable=False, unique=True),
    Column('email', TEXT, nullable=False),
    Column('capital', FLOAT, nullable=False),
)

simulation_schema = Table(
    'simulation',
    metadata,
    Column('id', INTEGER, primary_key=True),
    Column('dni', VARCHAR(9), ForeignKey('clients.dni')),
    Column('quota', FLOAT, nullable=False),
    Column('return_import', FLOAT, nullable=False),
)


def start_mappers(engine: any) -> None:
    metadata.create_all(engine)
    mapper_registry.map_imperatively(Client, client_schema)
    mapper_registry.map_imperatively(Simulation, simulation_schema)
    