from dataclasses import dataclass, field

def to_upper(value: str) -> str:
    return value.upper()

@dataclass
class Simulation:
    return_import: float
    quota: float
    dni: str = field(default_factory=to_upper)
    id: int = None