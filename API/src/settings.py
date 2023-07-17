import os
from sqlalchemy import create_engine
from sqlalchemy.orm import Session,sessionmaker

from src.core.infrastructure.database.schemas import start_mappers

class FlaskConfig:
    
    FLASK_HOST = "0.0.0.0"
    FLASK_PORT = 8080
    
class OperationResult:
    SUCCESS_CODE = 200
    ERROR_CODE = 400
    NOT_FOUND_CODE = 404
    DATABASE_ERROR_CODE = 500
    SUCCESS_RESULT = dict(
        status='OK', 
        result='Operation Succeded'
    )
    CLIENT_NOT_EXIST_RESULT = dict(
        status='KO', 
        result='There isn´t a client for this DNI'
    )
    DNI_INCORRECT_RESULT = dict(
            status='KO', 
            result='The DNI sended is incorrect'
    )
    EMAIL_INCORRECT_RESULT = dict(
            status='KO', 
            result='The email sended is incorrect'
    )
    TAE_TERM_INCORRECT_RESULT = dict(
            status='KO', 
            result='The TAE and term values cannot be negative nor zero'
    )
    DNI_ALREADY_IN_DATABASE_RESULT = dict(
            status='KO', 
            result='The DNI sended is already in database'
    )
    
class SqlAlchemyConfig:
    __engine = None
    DATA_BASE_FOLDER_NAME = 'DB'
    DATA_BASE_URI = f'sqlite:///{DATA_BASE_FOLDER_NAME}/database.db'
    SQL_ALCHEMY_POOL_RECYCLE = 280
    SQL_ALCHEMY_POOL_SIZE = 1
    SQL_ALCHEMY_MAX_OVERFLOW = -1
    
    @classmethod
    def getPersistenceSessionContext(cls) -> Session:
        if not os.path.exists(cls.DATA_BASE_FOLDER_NAME):
            os.makedirs(cls.DATA_BASE_FOLDER_NAME)
                     
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