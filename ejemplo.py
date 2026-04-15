from typing import Dict

from percepciones import Percepciones
from agente_academico import AgenteAcademico


def imprimir_resultados(resultados: Dict):
    print("\n" + "=" * 80)
    print("EVALUACIÓN DE RENDIMIENTO ACADÉMICO - AGENTE BASADO EN CONOCIMIENTO")
    print("=" * 80 + "\n")

    # Hechos detectados
    print("HECHOS DETECTADOS:")
    print("-" * 80)
    for percepcion, hecho in resultados["hechos"].items():
        print(f"  • {percepcion}: {hecho}")

    # Recomendaciones por percepción
    print("\n\nRECOMENDACIONES POR PERCEPCIÓN:")
    print("-" * 80)
    for i, rec in enumerate(resultados["recomendaciones_por_percepcion"], 1):
        print(f"\n{i}. {rec.percepcion} (Nivel: {rec.nivel.upper()})")
        print(f"   Estado detectado: {rec.estado_detectado}")
        print(f"   Interpretación: {rec.interpretacion}")
        print(f"   Acción recomendada: {rec.accion}")

    # Clasificación final
    print("\n\n" + "=" * 80)
    print(
        f"CLASIFICACIÓN DE RENDIMIENTO: {resultados['clasificacion_rendimiento'].upper()}"
    )
    print("=" * 80)

    # Recomendación final
    print(f"\n{resultados['recomendacion_final']}")
    print("\n" + "=" * 80 + "\n")


agente = AgenteAcademico()

# Ejemplo 1: Estudiante con bajo rendimiento
print("\n### EJEMPLO 1: ESTUDIANTE CON BAJO RENDIMIENTO ###")
estudiante_bajo = Percepciones(
    horas_estudio=0.5,
    calidad_apuntes=0,
    tareas_atrasadas=5,
    tiempo_organizacion=2.5,
    actividad_fisica_minutos=10,
    horas_sedentarismo=9,
    nivel_estres=8,
    apoyo_emocional=2,
    tazas_cafeina=5,
    minutos_pantalla_noche=90,
)
resultados = agente.evaluar_estudiante(estudiante_bajo)
imprimir_resultados(resultados)

# Ejemplo 2: Estudiante con alto rendimiento
print("\n\n### EJEMPLO 2: ESTUDIANTE CON ALTO RENDIMIENTO ###")
estudiante_alto = Percepciones(
    horas_estudio=2.5,
    calidad_apuntes=9,
    tareas_atrasadas=0,
    tiempo_organizacion=0.5,
    actividad_fisica_minutos=75,
    horas_sedentarismo=3,
    nivel_estres=2,
    apoyo_emocional=8,
    tazas_cafeina=1,
    minutos_pantalla_noche=0,
)
resultados = agente.evaluar_estudiante(estudiante_alto)
imprimir_resultados(resultados)

# Ejemplo 3: Estudiante con rendimiento medio
print("\n\n### EJEMPLO 3: ESTUDIANTE CON RENDIMIENTO MEDIO ###")
estudiante_medio = Percepciones(
    horas_estudio=1.2,
    calidad_apuntes=5,
    tareas_atrasadas=2,
    tiempo_organizacion=1.5,
    actividad_fisica_minutos=40,
    horas_sedentarismo=6,
    nivel_estres=5,
    apoyo_emocional=5,
    tazas_cafeina=3,
    minutos_pantalla_noche=45,
)
resultados = agente.evaluar_estudiante(estudiante_medio)
imprimir_resultados(resultados)
