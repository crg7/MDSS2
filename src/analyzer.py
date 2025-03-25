from abc import ABC, abstractmethod
import random

class AnalizadorVisitor(ABC):
    @abstractmethod
    def visit(self, lote):
        pass

class AnalizadorMadurezVisitor(AnalizadorVisitor):
    def visit(self, lote):
        funciones = {
            "aceite": self.analyze_aceite,
            "oliva de mesa": self.analyze_oliva
        }
        return funciones.get(lote.producto.lower(), self.analyze_default)(lote)
    
    def analyze_aceite(self, lote):
        return {
            "tipo_analisis": "madurez",
            "nivel_madurez": random.randint(0, 100),
            "acido_oleico": round(random.uniform(0.0, 100.0), 2),
            "indice_grasa": round(random.uniform(0.0, 100.0), 2)
        }
    
    def analyze_oliva(self, lote):
        return {
            "tipo_analisis": "madurez",
            "estado_madurez": random.choice(["verde", "envero", "negro"]),
            "firmeza_piel": round(random.uniform(0.0, 10.0), 2)
        }
    
    def analyze_default(self, lote):
        return {"tipo_analisis": "madurez", "resultado": "No definido"}

class AnalizadorDefectosVisitor(AnalizadorVisitor):
    def visit(self, lote):
        funciones = {
            "aceite": self.analyze_aceite,
            "oliva de mesa": self.analyze_oliva
        }
        return funciones.get(lote.producto.lower(), self.analyze_default)(lote)
    
    def analyze_aceite(self, lote):
        return {
            "tipo_analisis": "defectos",
            "hongos_detectados": random.choice([True, False]),
            "fermentacion_anomala": random.choice([True, False]),
            "danos_fisicos": random.choice(["leve", "moderado", "severo"])
        }
    
    def analyze_oliva(self, lote):
        return {
            "tipo_analisis": "defectos",
            "golpes": random.randint(0, 10),
            "arrugas": random.randint(0, 10),
            "presencia_insectos": random.choice([True, False]),
            "pudricion": random.choice(["nulo", "leve", "moderado", "severo"])
        }
    
    def analyze_default(self, lote):
        return {"tipo_analisis": "defectos", "resultado": "No definido"}

class AnalizadorHumedadVisitor(AnalizadorVisitor):
    def visit(self, lote):
        funciones = {
            "aceite": self.analyze_aceite,
            "oliva de mesa": self.analyze_oliva
        }
        return funciones.get(lote.producto.lower(), self.analyze_default)(lote)
    
    def analyze_aceite(self, lote):
        return {
            "tipo_analisis": "humedad",
            "porcentaje_humedad": round(random.uniform(0.0, 100.0), 2)
        }
    
    def analyze_oliva(self, lote):
        return {
            "tipo_analisis": "humedad",
            "porcentaje_humedad": round(random.uniform(0.0, 100.0), 2),
            "riesgo_moho": random.choice(["bajo", "medio", "alto"]),
            "idoneidad_conservacion": random.choice(["mala", "regular", "buena", "excelente"])
        }
    
    def analyze_default(self, lote):
        return {"tipo_analisis": "humedad", "resultado": "No definido"}

class AnalizadorColorVisitor(AnalizadorVisitor):
    def visit(self, lote):
        funciones = {
            "aceite": self.analyze_aceite,
            "oliva de mesa": self.analyze_oliva
        }
        return funciones.get(lote.producto.lower(), self.analyze_default)(lote)
    
    def analyze_aceite(self, lote):
        return {
            "tipo_analisis": "color",
            "color_preponderante": random.choice(["verde claro", "verde oscuro", "negro"]),
            "indice_color_esperado": random.choice(["verde-amarillo", "amarillo-dorado", "ambar"]),
            "transparencia": random.choice(["baja", "media", "alta"])
        }
    
    def analyze_oliva(self, lote):
        return {
            "tipo_analisis": "color",
            "clasificacion_color": {
                "verde claro": round(random.uniform(0.0, 100.0), 2),
                "verde oscuro": round(random.uniform(0.0, 100.0), 2),
                "negro": round(random.uniform(0.0, 100.0), 2)
            },
            "uniformidad_color": round(random.uniform(0.0, 100.0), 2)
        }
    
    def analyze_default(self, lote):
        return {"tipo_analisis": "color", "resultado": "No definido"}

class AnalizadorTamanoVisitor(AnalizadorVisitor):
    def visit(self, lote):
        funciones = {
            "aceite": self.analyze_aceite,
            "oliva de mesa": self.analyze_oliva
        }
        return funciones.get(lote.producto.lower(), self.analyze_default)(lote)
    
    def analyze_aceite(self, lote):
        return {
            "tipo_analisis": "tamano",
            "tamano_promedio": round(random.uniform(0.0, 20.0), 2),
            "frutos_fuera_estandar": round(random.uniform(0.0, 100.0), 2)
        }
    
    def analyze_oliva(self, lote):
        return {
            "tipo_analisis": "tamano",
            "clasificacion_calibre": random.choice(["chico", "mediano", "grande"]),
            "frutos_fuera_estandar": round(random.uniform(0.0, 100.0), 2)
        }
    
    def analyze_default(self, lote):
        return {"tipo_analisis": "tamano", "resultado": "No definido"}

class AnalizadorVariedadVisitor(AnalizadorVisitor):
    def visit(self, lote):
        return {
            "tipo_analisis": "variedades",
            "distribucion_variedades": [
                {"variedad": "variedad1", "porcentaje": round(random.uniform(0.0, 100.0), 2)},
                {"variedad": "variedad2", "porcentaje": round(random.uniform(0.0, 100.0), 2)}
            ]
        }
