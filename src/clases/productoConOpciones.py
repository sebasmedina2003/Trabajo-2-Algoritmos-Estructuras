from producto import Producto


class ProductoConOpciones(Producto):
    def __init__(self,
                 nombre: str,
                 descripcion: str,
                 precio: float,
                 estatus: str,
                 cantidad: int,
                 opciones: dict
                 ) -> None:
        super().__init__(nombre, descripcion, precio, estatus, cantidad)

        self.opciones = opciones
    
    def mostrarOpciones(self) -> None:
        for keys in self.opciones:
            if type(self.opciones.get(keys)) in [str,int,float] :
                print("Para la clave {llave} tenemos {valor}".format(llave=keys, valor=self.opciones.get(keys)))
            else:
                text = ""
                for valores in self.opciones.get(keys):
                    text += valores + ", "
                text = text[:len(text)-2]
                print("Para la clave {llave} tenemos {valores}".format(llave = keys, valores = text))