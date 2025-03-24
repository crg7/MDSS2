import uuid

class ProductoFinal:
    def __init__(self, tipo, cantidad, unidad, metodo_extraccion=None):
        self.codigo_seguimiento = str(uuid.uuid4().int)[:20]
        self.tipo = tipo
        self.cantidad = cantidad
        self.unidad = unidad
        self.metodo_extraccion = metodo_extraccion
        self.calidad = None
        self.almacenamiento = {"galpon": None, "sala": None}

    def asignar_almacenamiento(self, galpon, sala):
        self.almacenamiento["galpon"] = galpon
        self.almacenamiento["sala"] = sala
