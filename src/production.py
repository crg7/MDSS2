import uuid
import datetime

class LoteProduccion:
    def __init__(self):
        self.numero_lote = str(uuid.uuid4().int)[:24]
        self.lotes_materia = []
        self.productos_finales = []
        self.transiciones = []
        self.estado = "En armado"

    def agregar_lote(self, lote):
        self.lotes_materia.append(lote)
        self.transiciones.append({"accion": "lote agregado", "timestamp": datetime.datetime.now().isoformat()})

    def asignar_producto(self, producto):
        self.productos_finales.append(producto)
        self.transiciones.append({"accion": "producto asignado", "timestamp": datetime.datetime.now().isoformat()})

    def exportar_reporte(self, estrategia_export, archivo: str):
        reporte = {
            "numero_lote": self.numero_lote,
            "estado": self.estado,
            "transiciones": self.transiciones,
            "lotes_materia": [
                {
                    "codigo": lm.codigo,
                    "productor": str(lm.productor),
                    "fecha_cosecha": lm.fecha_cosecha,
                    "fecha_arribo": lm.fecha_arribo.isoformat(),
                    "peso_neto": lm.peso_neto
                } for lm in self.lotes_materia
            ],
            "productos_finales": [
                {
                    "codigo_seguimiento": pf.codigo_seguimiento,
                    "tipo": pf.tipo,
                    "cantidad": pf.cantidad,
                    "unidad": pf.unidad,
                    "almacenamiento": pf.almacenamiento,
                    "calidad": pf.calidad
                } for pf in self.productos_finales
            ]
        }
        estrategia_export.export(reporte, archivo)
