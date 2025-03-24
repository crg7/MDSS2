from abc import ABC, abstractmethod
import datetime

class EstadoLote(ABC):
    def __init__(self):
        self.timestamp = datetime.datetime.now()

    def registrar_transicion(self, accion):
        print(f"{accion} a las {self.timestamp.isoformat()}")

    @abstractmethod
    def ingresar_imagen(self, lote, imagen):
        pass

    @abstractmethod
    def agregar_resultado(self, lote, resultado):
        pass

    @abstractmethod
    def pasar_a_analisis(self, lote):
        pass

    @abstractmethod
    def revertir(self, lote):
        pass

class Ingresado(EstadoLote):
    def ingresar_imagen(self, lote, imagen):
        self.registrar_transicion("Registrando imagen")
        lote.imagenes.append(imagen)

    def agregar_resultado(self, lote, resultado):
        print("No se permiten resultados en estado Ingresado.")

    def pasar_a_analisis(self, lote):
        self.registrar_transicion("Cambiando a EnAnálisis")
        lote.estado = EnAnalisis()

    def revertir(self, lote):
        print("El lote ya se encuentra en estado Ingresado.")

class EnAnalisis(EstadoLote):
    def ingresar_imagen(self, lote, imagen):
        print("No se permiten imágenes en estado EnAnálisis.")

    def agregar_resultado(self, lote, resultado):
        self.registrar_transicion("Agregando resultado")
        lote.resultados.append(resultado)

    def pasar_a_analisis(self, lote):
        self.registrar_transicion("Cambiando a Analizado")
        lote.estado = Analizado()

    def revertir(self, lote):
        self.registrar_transicion("Revirtiendo a Ingresado")
        lote.resultados.clear()
        lote.estado = Ingresado()

class Analizado(EstadoLote):
    def ingresar_imagen(self, lote, imagen):
        print("No se permiten imágenes en estado Analizado.")

    def agregar_resultado(self, lote, resultado):
        print("No se permiten resultados en estado Analizado.")

    def pasar_a_analisis(self, lote):
        print("El lote ya está Analizado.")

    def revertir(self, lote):
        print("No se puede revertir desde Analizado.")

class EnProduccion(EstadoLote):
    def ingresar_imagen(self, lote, imagen):
        print("No se permiten imágenes en estado EnProducción.")

    def agregar_resultado(self, lote, resultado):
        print("No se permiten resultados en estado EnProducción.")

    def pasar_a_analisis(self, lote):
        print("El lote ya está en Producción.")

    def revertir(self, lote):
        self.registrar_transicion("Revirtiendo a Analizado")
        lote.estado = Analizado()
