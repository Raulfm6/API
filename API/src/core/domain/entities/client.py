from dataclasses import dataclass, field, asdict


def to_upper(value: str) -> str:
    return value.upper()

@dataclass
class Client:
    name: str
    email: str
    capital: float
    dni: str = field(default_factory=to_upper)
    id: int = None
    
    def toJson(self):
        return asdict(self)
