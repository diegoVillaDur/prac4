from dataclasses import dataclass


@dataclass
class Percepciones:
    # Hábitos de estudio
    horas_estudio: float  # horas diarias
    calidad_apuntes: int  # escala 0-10

    # Gestión de tareas
    tareas_atrasadas: int
    tiempo_organizacion: float  # horas diarias

    # Actividad física
    actividad_fisica_minutos: float  # minutos diarios
    horas_sedentarismo: float  # horas sentado

    # Nivel de estrés
    nivel_estres: int  # escala 0-10
    apoyo_emocional: int  # escala 0-10

    # Hábitos de sueño
    tazas_cafeina: float  # tazas diarias
    minutos_pantalla_noche: float  # minutos antes de dormir
