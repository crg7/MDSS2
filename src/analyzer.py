from abc import ABC, abstractmethod
import random

class AnalizadorVisitor(ABC):
    @abstractmethod
    def visit(self, lote):
        pass

class AnalizadorMadurezVisitor(AnalizadorVisitor):
    def visit(self, lote):
        if lote.producto.lower() == "aceite":
            return {
                "tipo_analisis": "madurez",
                "nivel_madurez": random.randint(0, 100),
                "acido_oleico": round(random.uniform(0.0, 100.0), 2),
                "indice_grasa": round(random.uniform(0.0, 100.0), 2)
            }
        else:
            return {
                "tipo_analisis": "madurez",
                "estado_madurez": random.choice(["verde", "envero", "negro"]),
                "firmeza_piel": round(random.uniform(0.0, 10.0), 2)
            }

class AnalizadorDefectosVisitor(AnalizadorVisitor):
    def visit(self, lote):
        if lote.producto.lower() == "aceite":
            return {
                "tipo_analisis": "defectos",
                "hongos_detectados": random.choice([True, False]),
                "fermentacion_anomala": random.choice([True, False]),
                "danos_fisicos": random.choice(["leve", "moderado", "severo"])
            }
        else:
            return {
                "tipo_analisis": "defectos",
                "golpes": random.randint(0, 10),
                "arrugas": random.randint(0, 10),
                "presencia_insectos": random.choice([True, False]),
                "pudricion": random.choice(["nulo", "leve", "moderado", "severo"])
            }
