from producer import Productor
from rawbatch import LoteMateriaPrima
from analyzer import AnalizadorMadurezVisitor, AnalizadorDefectosVisitor
from production import LoteProduccion
from product import ProductoFinal
from exporter import ExportJSONStrategy
from quality import CalidadAceiteVirgenExtra

def main():
    productor = Productor("Carlos", "Rangel", "12345678A", "Calle Falsa 123", "600123456", "carlos@mail.com")
    lote = LoteMateriaPrima(productor, "2025-03-01", "Aceite", 1000, 50)
    lote.ingresar_imagen("imagen1.jpg")
    lote.ingresar_imagen("imagen2.jpg")
    lote.pasar_a_analisis()
    analizador_madurez = AnalizadorMadurezVisitor()
    analizador_defectos = AnalizadorDefectosVisitor()
    lote.accept(analizador_madurez)
    lote.accept(analizador_defectos)
    lote.pasar_a_analisis()
    lote_prod = LoteProduccion()
    lote_prod.agregar_lote(lote)
    producto = ProductoFinal("Aceite", 500, "LITROS", metodo_extraccion="PRENSADO_EN_FRIO")
    estrategia_calidad = CalidadAceiteVirgenExtra()
    atributos = {
        "acidez": 0.4,
        "metodo": "PRENSADO_EN_FRIO",
        "polifenoles": 320,
        "defectos": 0
    }
    producto.calidad = estrategia_calidad.evaluate(atributos)
    producto.asignar_almacenamiento("G1", "S1")
    lote_prod.asignar_producto(producto)
    estrategia_export = ExportJSONStrategy()
    lote_prod.exportar_reporte(estrategia_export, "lote_produccion.json")

if __name__ == "__main__":
    main()
