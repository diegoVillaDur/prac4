from typing import Dict, List

from nivel_rendimiento import NivelRendimiento
from percepciones import Percepciones
from recomendacion import Recomendacion
from base_conocimiento import BaseConocimiento
from motor_inferencia import MotorInferencia


class AgenteAcademico:

    def __init__(self):
        self.base_conocimiento = BaseConocimiento()
        self.motor_inferencia = MotorInferencia()

    def evaluar_estudiante(self, percepciones: Percepciones) -> Dict:

        # FASE 1: Percepción → Base de Conocimiento
        hechos = {}
        recomendaciones = []

        # Evaluar cada percepción
        hecho, rec = self.base_conocimiento.evaluar_habitos_estudio(percepciones)
        hechos["habitos_estudio"] = hecho
        recomendaciones.append(rec)

        hecho, rec = self.base_conocimiento.evaluar_gestion_tareas(percepciones)
        hechos["gestion_tareas"] = hecho
        recomendaciones.append(rec)

        hecho, rec = self.base_conocimiento.evaluar_actividad_fisica(percepciones)
        hechos["actividad_fisica"] = hecho
        recomendaciones.append(rec)

        hecho, rec = self.base_conocimiento.evaluar_nivel_estres(percepciones)
        hechos["nivel_estres"] = hecho
        recomendaciones.append(rec)

        hecho, rec = self.base_conocimiento.evaluar_habitos_sueno(percepciones)
        hechos["habitos_sueno"] = hecho
        recomendaciones.append(rec)

        # FASE 2: Motor de Inferencia
        rendimiento = self.motor_inferencia.determinar_rendimiento(hechos)

        # FASE 3: Acción - Generar recomendación final
        recomendacion_final = self._generar_recomendacion_final(
            rendimiento, recomendaciones
        )

        return {
            "hechos": hechos,
            "recomendaciones_por_percepcion": recomendaciones,
            "clasificacion_rendimiento": rendimiento.value,
            "recomendacion_final": recomendacion_final,
        }

    def _generar_recomendacion_final(
        self, rendimiento: NivelRendimiento, recomendaciones: List[Recomendacion]
    ) -> str:

        if rendimiento == NivelRendimiento.ALTO:
            return (
                "¡Excelente trabajo! Tu rendimiento académico es ALTO. "
                "Mantén tus buenos hábitos de estudio y gestión del tiempo. "
                "Continúa cuidando tu salud física y mental para sostener este nivel de desempeño."
            )
        elif rendimiento == NivelRendimiento.BAJO:
            areas_criticas = [
                r.percepcion for r in recomendaciones if r.nivel == "bajo"
            ]
            return (
                f"Tu rendimiento académico es BAJO. Se detectaron áreas críticas en: {', '.join(areas_criticas)}. "
                "Es fundamental implementar las recomendaciones específicas para cada área. "
                "Prioriza mejorar tus hábitos de estudio y gestión del tiempo como primer paso."
            )
        else:  # MEDIO
            return (
                "Tu rendimiento académico es MEDIO. Tienes una base sólida pero hay oportunidades de mejora. "
                "Revisa las recomendaciones específicas para optimizar tus hábitos. "
                "Pequeños ajustes en tu rutina pueden llevarte al siguiente nivel."
            )
