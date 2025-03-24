import uuid
import datetime
from state import Ingresado

class LoteMateriaPrima:
    def __init__(self, productor, fecha_cosecha, producto, peso_bruto, peso_tara):
        self.productor = productor
        self.fecha_cosecha = fecha_cosecha
        self.fecha_arribo = datetime.datetime.now()
        self.codigo = str(uuid.uuid4().int)[:24]
        self.peso_bruto = peso_bruto
        self.peso_tara = peso_tara
        self.producto = producto
        self.imagenes = []
        self.resultados = []
        self.estado = Ingresado()

    @property
    def peso_neto(self):
        return self.peso_bruto - self.peso_tara

    def ingresar_imagen(self, imagen):
        self.estado.ingresar_imagen(self, imagen)

    def agregar_resultado(self, resultado):
        self.estado.agregar_resultado(self, resultado)

    def pasar_a_analisis(self):
        self.estado.pasar_a_analisis(self)

    def revertir_estado(self):
        self.estado.revertir(self)

    def accept(self, visitante):
        resultado = visitante.visit(self)
        self.resultados.append(resultado)
