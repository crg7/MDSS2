from abc import ABC, abstractmethod

class CalidadStrategy(ABC):
    @abstractmethod
    def evaluate(self, atributos: dict) -> str:
        pass

class CalidadAceiteVirgenExtra(CalidadStrategy):
    def evaluate(self, atributos: dict) -> str:
        puntaje = 0
        puntaje += 2 if atributos.get("acidez", 0) < 0.5 else 1 if atributos.get("acidez", 0) < 1 else 0
        puntaje += 2 if atributos.get("metodo", "") == "PRENSADO_EN_FRIO" else 0
        puntaje += 2 if atributos.get("polifenoles", 0) > 300 else 1 if atributos.get("polifenoles", 0) > 150 else 0
        puntaje += 2 if atributos.get("defectos", 0) == 0 else 1 if atributos.get("defectos", 0) <= 2 else 0
        puntaje += 2
        if puntaje > 8:
            return "ALTA"
        elif puntaje >= 5:
            return "MEDIA"
        else:
            return "BAJA"

class CalidadAceiteVirgen(CalidadStrategy):
    def evaluate(self, atributos: dict) -> str:
        puntaje = 0
        puntaje += 2 if atributos.get("acidez", 0) < 1 else 1 if atributos.get("acidez", 0) < 1.5 else 0
        puntaje += 2 if atributos.get("metodo", "") in ["PRENSADO_EN_FRIO", "CENTRIFUGADO"] else 0
        puntaje += 2 if atributos.get("polifenoles", 0) > 250 else 1 if atributos.get("polifenoles", 0) > 100 else 0
        puntaje += 2 if atributos.get("defectos", 0) == 0 else 1 if atributos.get("defectos", 0) <= 3 else 0
        puntaje += 1
        if puntaje > 8:
            return "ALTA"
        elif puntaje >= 5:
            return "MEDIA"
        else:
            return "BAJA"

class CalidadAceiteDeOrujo(CalidadStrategy):
    def evaluate(self, atributos: dict) -> str:
        puntaje = 0
        puntaje += 2 if atributos.get("acidez", 0) < 2 else 1 if atributos.get("acidez", 0) < 3 else 0
        puntaje += 2 if atributos.get("metodo", "") == "CON_DISOLVENTES" else 0
        puntaje += 2 if atributos.get("polifenoles", 0) > 200 else 1 if atributos.get("polifenoles", 0) > 100 else 0
        puntaje += 2 if atributos.get("defectos", 0) == 0 else 1 if atributos.get("defectos", 0) <= 2 else 0
        puntaje += 2
        if puntaje > 8:
            return "ALTA"
        elif puntaje >= 5:
            return "MEDIA"
        else:
            return "BAJA"

class CalidadOlivaMesa(CalidadStrategy):
    def evaluate(self, atributos: dict) -> str:
        puntaje = 0
        puntaje += 2 if atributos.get("uniformidad_color", 0) > 80 else 1 if atributos.get("uniformidad_color", 0) > 50 else 0
        puntaje += 2 if atributos.get("tamano_promedio", 0) > 50 else 1 if atributos.get("tamano_promedio", 0) > 30 else 0
        puntaje += 2 if atributos.get("desviacion", 0) < 5 else 1 if atributos.get("desviacion", 0) < 10 else 0
        puntaje += 2 if atributos.get("perfil_sabor", "") in ["suave", "equilibrado"] else 0
        puntaje += 1 if atributos.get("proceso_curado", "") in ["natural", "salmuerado"] else 0
        puntaje += 2 if atributos.get("contenido_sal", 0) < 5 else 0
        puntaje += 2 if atributos.get("defectos", 0) == 0 else 1 if atributos.get("defectos", 0) <= 2 else 0
        puntaje += 1 if atributos.get("ph", 7) >= 7 else 0
        if puntaje > 8:
            return "ALTA"
        elif puntaje >= 5:
            return "MEDIA"
        else:
            return "BAJA"
