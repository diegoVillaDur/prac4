from dataclasses import dataclass


@dataclass
class Recomendacion:
    percepcion: str
    estado_detectado: str
    interpretacion: str
    accion: str
    nivel: str  # bajo, medio, alto
