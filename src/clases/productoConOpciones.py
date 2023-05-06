from producto import Producto


class ProductoConOpcinoes(Producto):
    def __init__(self,
                 nombre: str,
                 descripcion: str,
                 precio: float,
                 estatus: str,
                 cantidad: int,
                 opciones: list[dict]
                 ) -> None:
        super().__init__(nombre, descripcion, precio, estatus, cantidad)

        self.opciones = opciones
    
    def mostrarOpciones(self) -> None:
        for keys in self.opciones:
            print(f"Para la clave {} tenemos {}".format(keys, self.opciones[keys]))
