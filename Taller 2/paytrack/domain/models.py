from dataclasses import dataclass
from datetime import datetime

@dataclass
class Payment:
    id: int
    nombre_cliente: str
    monto: float
    fecha: datetime
    estado: str = "COMPLETADO"