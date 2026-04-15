from typing import Dict

from nivel_rendimiento import NivelRendimiento


class MotorInferencia:

    @staticmethod
    def determinar_rendimiento(hechos: Dict[str, str]) -> NivelRendimiento:

        # Extraer hechos
        habitos = hechos.get("habitos_estudio", "")
        gestion = hechos.get("gestion_tareas", "")
        actividad = hechos.get("actividad_fisica", "")
        estres = hechos.get("nivel_estres", "")

        # Evaluar Rendimiento ALTO
        rendimiento_alto = (
            (habitos == "habitos_estudio_buenos" and gestion == "gestion_alta")
            or (
                habitos == "habitos_estudio_buenos"
                and gestion == "gestion_media"
                and (
                    actividad == "actividad_fisica_buena"
                    or estres == "nivel_estres_bueno"
                )
            )
            or (
                habitos == "habitos_estudio_medios"
                and gestion == "gestion_alta"
                and estres == "nivel_estres_bueno"
            )
        )

        # Evaluar Rendimiento BAJO
        rendimiento_bajo = (
            (habitos == "habitos_estudio_malos")
            or (habitos == "habitos_estudio_medios" and gestion == "gestion_mala")
            or (
                habitos == "habitos_estudio_buenos"
                and gestion == "gestion_mala"
                and estres == "nivel_estres_malo"
            )
        )

        # Determinar rendimiento
        if rendimiento_alto:
            return NivelRendimiento.ALTO
        elif rendimiento_bajo:
            return NivelRendimiento.BAJO
        else:
            return NivelRendimiento.MEDIO
