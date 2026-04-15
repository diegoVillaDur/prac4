from typing import Tuple

from percepciones import Percepciones
from recomendacion import Recomendacion


class BaseConocimiento:

    @staticmethod
    def evaluar_habitos_estudio(
        percepciones: Percepciones,
    ) -> Tuple[str, Recomendacion]:
        """Evalúa hábitos de estudio"""
        horas = percepciones.horas_estudio
        apuntes = percepciones.calidad_apuntes

        # Bajo rendimiento
        if horas < 1 and apuntes == 0:
            return "habitos_estudio_malos", Recomendacion(
                percepcion="Hábitos de estudio",
                estado_detectado=f"Estudia menos de 1 hora ({horas:.1f}h) y no toma apuntes (calidad: {apuntes}/10)",
                interpretacion="Falta de práctica académica",
                accion="Crear horario diario de estudio e implementar herramientas que faciliten la toma de apuntes",
                nivel="bajo",
            )

        # Alto rendimiento
        elif horas >= 1.5 and horas <= 3 and apuntes >= 7:
            return "habitos_estudio_buenos", Recomendacion(
                percepcion="Hábitos de estudio",
                estado_detectado=f"Estudia más de 1 hora y media ({horas:.1f}h) y toma apuntes de buena calidad ({apuntes}/10)",
                interpretacion="Dedicación académica sobresaliente",
                accion="Mantener la rutina, pero recomendar no llegar a límites o fatiga extrema",
                nivel="alto",
            )

        # Medio rendimiento
        else:
            return "habitos_estudio_medios", Recomendacion(
                percepcion="Hábitos de estudio",
                estado_detectado=f"Estudia entre 1 y 1.5 horas ({horas:.1f}h) y toma apuntes de calidad media ({apuntes}/10)",
                interpretacion="Tiene práctica académica suficiente",
                accion="Buscar oportunidades de mejora para la rutina actual",
                nivel="medio",
            )

    @staticmethod
    def evaluar_gestion_tareas(percepciones: Percepciones) -> Tuple[str, Recomendacion]:
        """Evalúa gestión de tareas pendientes"""
        tareas = percepciones.tareas_atrasadas
        tiempo_org = percepciones.tiempo_organizacion

        # Bajo rendimiento
        if tareas > 3 and tiempo_org > 2:
            return "gestion_mala", Recomendacion(
                percepcion="Gestión de tareas pendientes",
                estado_detectado=f"Tiene más de 3 tareas atrasadas ({tareas}) y dedica más de 2 horas diarias a organizarse ({tiempo_org:.1f}h) sin resultados",
                interpretacion="Problemas de organización o sobrecarga",
                accion="Implementar un sistema de gestión de tiempo y priorización (ej. Matriz de Eisenhower)",
                nivel="bajo",
            )

        # Alto rendimiento
        elif tareas == 0 and tiempo_org < 1:
            return "gestion_alta", Recomendacion(
                percepcion="Gestión de tareas pendientes",
                estado_detectado=f"No tiene tareas atrasadas ({tareas}) y dedica menos de 1 hora diaria a organizarse ({tiempo_org:.1f}h)",
                interpretacion="Excelente gestión del tiempo y organización",
                accion="Mantener el sistema de organización actual",
                nivel="alto",
            )

        # Medio rendimiento
        else:
            return "gestion_media", Recomendacion(
                percepcion="Gestión de tareas pendientes",
                estado_detectado=f"Tiene entre 1 y 3 tareas atrasadas ({tareas}) y dedica entre 1 y 2 horas diarias a organizarse ({tiempo_org:.1f}h)",
                interpretacion="Organización aceptable, pero con margen de mejora",
                accion="Revisar y optimizar el método de priorización de tareas",
                nivel="medio",
            )

    @staticmethod
    def evaluar_actividad_fisica(
        percepciones: Percepciones,
    ) -> Tuple[str, Recomendacion]:
        """Evalúa nivel de actividad física"""
        actividad = percepciones.actividad_fisica_minutos
        sedentarismo = percepciones.horas_sedentarismo

        # Bajo rendimiento
        if actividad < 20 and sedentarismo > 8:
            return "actividad_fisica_mala", Recomendacion(
                percepcion="Nivel de actividad física",
                estado_detectado=f"Realiza menos de 20 minutos de actividad física diaria ({actividad:.0f} min) y permanece más de 8 horas sentado ({sedentarismo:.1f}h)",
                interpretacion="Estilo de vida sedentario con riesgos para la salud",
                accion="Iniciar con actividad física ligera (ej. caminatas de 30 minutos)",
                nivel="bajo",
            )

        # Alto rendimiento
        elif actividad > 60 and sedentarismo < 4:
            return "actividad_fisica_buena", Recomendacion(
                percepcion="Nivel de actividad física",
                estado_detectado=f"Realiza más de 1 hora de actividad física diaria ({actividad:.0f} min) y permanece menos de 4 horas sentado ({sedentarismo:.1f}h)",
                interpretacion="Estilo de vida activo y con buenas prácticas de salud",
                accion="Mantener la rutina, cuidar calentamiento y recuperación para evitar lesiones por sobreuso",
                nivel="alto",
            )

        # Medio rendimiento
        else:
            return "actividad_fisica_media", Recomendacion(
                percepcion="Nivel de actividad física",
                estado_detectado=f"Realiza entre 20 minutos y 1 hora de actividad física diaria ({actividad:.0f} min) y permanece entre 4 y 8 horas sentado ({sedentarismo:.1f}h)",
                interpretacion="Nivel de actividad física suficiente para la salud",
                accion="Intentar aumentar la duración de la actividad física",
                nivel="medio",
            )

    @staticmethod
    def evaluar_nivel_estres(percepciones: Percepciones) -> Tuple[str, Recomendacion]:
        """Evalúa nivel de estrés"""
        estres = percepciones.nivel_estres
        apoyo = percepciones.apoyo_emocional

        # Bajo rendimiento (alto estrés)
        if estres > 7 and apoyo <= 3:
            return "nivel_estres_malo", Recomendacion(
                percepcion="Nivel de estrés",
                estado_detectado=f"Nivel de estrés superior a 7 ({estres}/10) y cuenta con poco o ningún apoyo emocional ({apoyo}/10)",
                interpretacion="Estrés crónico o muy elevado que afecta el rendimiento",
                accion="Aplicar técnicas de relajación y buscar apoyo para gestionar la carga",
                nivel="bajo",
            )

        # Alto rendimiento (bajo estrés)
        elif estres < 3 and apoyo >= 7:
            return "nivel_estres_bueno", Recomendacion(
                percepcion="Nivel de estrés",
                estado_detectado=f"Nivel de estrés inferior a 3 ({estres}/10) y cuenta con alto apoyo emocional ({apoyo}/10)",
                interpretacion="Bajo nivel de ansiedad, buen manejo de la presión",
                accion="Continuar manteniendo un ambiente de estudio relajado",
                nivel="alto",
            )

        # Medio rendimiento
        else:
            return "nivel_estres_medio", Recomendacion(
                percepcion="Nivel de estrés",
                estado_detectado=f"Nivel de estrés entre 3 y 7 ({estres}/10) y cuenta con apoyo emocional moderado ({apoyo}/10)",
                interpretacion="Estrés manejable, pero requiere atención para evitar que aumente",
                accion="Integrar pausas activas y métodos de descompresión en la rutina diaria",
                nivel="medio",
            )

    @staticmethod
    def evaluar_habitos_sueno(percepciones: Percepciones) -> Tuple[str, Recomendacion]:
        """Evalúa hábitos de sueño"""
        cafeina = percepciones.tazas_cafeina
        pantalla = percepciones.minutos_pantalla_noche

        # Bajo rendimiento (usa OR)
        if cafeina > 4 or pantalla > 60:
            return "malos_habitos_de_sueno", Recomendacion(
                percepcion="Hábitos de sueño",
                estado_detectado=f"Consume más de 4 tazas de cafeína diarias ({cafeina:.1f}) o pasa más de 60 minutos frente a pantallas antes de dormir ({pantalla:.0f} min)",
                interpretacion="Falta crónica de descanso",
                accion="Establecer un horario regular de sueño y garantizar un mínimo de 7 horas",
                nivel="bajo",
            )

        # Alto rendimiento (usa AND)
        elif cafeina < 2 and pantalla == 0:
            return "buenos_habitos_de_sueno", Recomendacion(
                percepcion="Hábitos de sueño",
                estado_detectado=f"Consume menos de 2 tazas de cafeína diarias ({cafeina:.1f}) y no usa pantallas antes de dormir ({pantalla:.0f} min)",
                interpretacion="Nivel de sueño óptimo para la recuperación",
                accion="Mantener la rutina de sueño actual",
                nivel="alto",
            )

        # Medio rendimiento (usa OR)
        else:
            return "medios_habitos_de_sueno", Recomendacion(
                percepcion="Hábitos de sueño",
                estado_detectado=f"Consume entre 2 y 4 tazas de cafeína diarias ({cafeina:.1f}) o pasa entre 30 y 60 minutos frente a pantallas antes de dormir ({pantalla:.0f} min)",
                interpretacion="Descanso adecuado, pero puede ser insuficiente",
                accion="Priorizar la higiene del sueño para alcanzar las 7-8 horas",
                nivel="medio",
            )
