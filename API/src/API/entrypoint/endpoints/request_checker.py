import re
from werkzeug.exceptions import BadRequest
from src.settings import OperationResult

class RequestChecker:
    """
    Class ussed to validate params from request if necessary
    """
        
    @staticmethod
    def check_dni(dni: str) -> None:
        DNI_REGEX = r'^\d{8}[A-HJ-NP-TV-Z]$'
        DNI_LETTERS = 'TRWAGMYFPDXBNJZSQVHLCKE'
        
        dni = dni.upper()
        
        if not re.match(DNI_REGEX, dni):
            raise BadRequest(description='DNI Incorrect', response=OperationResult.DNI_INCORRECT_RESULT['result'])
    
        digits = dni[:-1] 
        letter = dni[-1]
        letter_index = int(digits) % 23

        if letter != DNI_LETTERS[letter_index]:
            raise BadRequest(description='DNI Incorrect', response=OperationResult.DNI_INCORRECT_RESULT['result'])
        
    @staticmethod
    def check_email(email: str) -> None:
        
        EMAIL_REGEX = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        
        if not re.match(EMAIL_REGEX, email):
            raise BadRequest(description='Email Incorrect', response=OperationResult.EMAIL_INCORRECT_RESULT['result'])
        
        
    @staticmethod
    def check_simulation_params(tae: float, term: int):
        
        if tae <= 0 or term <= 0:
            raise BadRequest(description='Simulation Incorrect', response=OperationResult.TAE_TERM_INCORRECT_RESULT['result'])
        