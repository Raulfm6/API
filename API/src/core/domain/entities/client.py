from dataclasses import dataclass, field


def to_upper(value: str) -> str:
    return value.upper()

@dataclass
class Client:
    name: str
    email: str
    capital: float
    dni: str = field(default_factory=to_upper)
    id: int = None
    
    def __str__(self) -> str:
        return f"Cliente con id {self.id}, dni {self.dni}, email {self.email} y capital {self.capital}"
