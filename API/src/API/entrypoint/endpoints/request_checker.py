import re
from werkzeug.exceptions import BadRequest

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
            raise BadRequest(description='DNI Incorrect', response='The DNI sended is incorrect')
    
        digits = dni[:-1] 
        letter = dni[-1]
        letter_index = int(digits) % 23

        if letter != DNI_LETTERS[letter_index]:
            raise BadRequest(description='DNI Incorrect', response='The DNI sended is incorrect')
        
    @staticmethod
    def check_email(email: str) -> None:
        
        EMAIL_REGEX = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        
        if not re.match(EMAIL_REGEX, email):
            raise BadRequest(description='Email Incorrect', response='The email sended is incorrect')
        
        
    @staticmethod
    def check_simulation_params(tae: float, term: int):
        
        if tae <= 0 or term <= 0:
            raise BadRequest(description='Simulation Incorrect', response='The TAE and term values cannot be negative nor zero')
        