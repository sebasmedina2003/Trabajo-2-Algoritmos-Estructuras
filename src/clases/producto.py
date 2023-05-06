from datetime import datetime


class Producto:
    def __init__(self, nombre: str, descripcion: str, precio: float, estatus: str, cantidad: int) -> None:
        """
        Constructor de la clase Producto, la fecha de creacion y actualizacion se toman automaticamente con el formato
        d/m/y
        """
        formato = "%d/%m/%y"
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.estatus = estatus
        self.cantidad = cantidad
        self.fechaCreacion = datetime.now().strftime(formato)
        self.fechaActualizacion = datetime.now().strftime(formato)

    def actualizarStock(self, cantVendida: int) -> (bool | None):
        if self.cantidad < cantVendida:
            return False

        self.cantidad -= cantVendida

        if self.cantidad == 0:
            self.estatus = "Acabado"
