class Productor:
    def __init__(self, nombre, apellidos, nif, direccion, telefono, correo):
        self.nombre = nombre
        self.apellidos = apellidos
        self.nif = nif
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"
