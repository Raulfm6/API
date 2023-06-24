from sqlalchemy import create_engine
from sqlalchemy.orm import Session,sessionmaker

from src.core.infrastructure.database.schemas import start_mappers

class FlaskConfig:
    
    FLASK_HOST = "0.0.0.0"
    FLASK_PORT = 8080
    
    
class SqlAlchemyConfig:
    __engine = None
    DATA_BASE_URI = 'sqlite:///DB/database.db'
    SQL_ALCHEMY_POOL_RECYCLE = 280
    SQL_ALCHEMY_POOL_SIZE = 1
    SQL_ALCHEMY_MAX_OVERFLOW = -1
    
    @classmethod
    def getPersistenceSessionContext(cls) -> Session:
                     
        if cls.__engine is None:
            cls.__engine = create_engine(
                cls.DATA_BASE_URI,
                pool_recycle=cls.SQL_ALCHEMY_POOL_RECYCLE,
                pool_size=cls.SQL_ALCHEMY_POOL_SIZE,
                max_overflow=cls.SQL_ALCHEMY_MAX_OVERFLOW
            )
            start_mappers(cls.__engine)    

        session = sessionmaker(bind=cls.__engine, future=True)()
        return session