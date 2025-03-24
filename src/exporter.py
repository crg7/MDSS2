from abc import ABC, abstractmethod
import json

class ExportStrategy(ABC):
    @abstractmethod
    def export(self, reporte: dict, archivo: str):
        pass

class ExportJSONStrategy(ExportStrategy):
    def export(self, reporte: dict, archivo: str):
        with open(archivo, "w", encoding="utf-8") as f:
            json.dump(reporte, f, indent=4, ensure_ascii=False)
        print(f"Reporte exportado a {archivo}")
