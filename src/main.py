# Importar clases
import clases.controlador as controlador
import clases.carrito as carrito
import clases.orden as orden
from time import sleep

""" Producto -> Nodos"""
class Producto:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)
    
""" Lista enlazada """
class ListaEnlazada:
    def __init__(self):
        self.first = None
        self.size = 0
        self.band = False

    def __len__(self):
        return self._size

    def Append(self, value):
        nodo = Producto(value)
        if self.size == 0:
            self.first = nodo
        else:
            current = self.first
            while current.next != None:
                current = current.next
            current.next = nodo
        self.size += 1

    def catalogo(self):
        current = self.first
        if self.band == False:
            while current != None:
                if current.value["Status"] == "activo" and current.value["Cantidad"] > 0:
                    controlador.Stock.Append(current.value)
                    self.band = True    
                current = current.next
        controlador.mostrarProductos(controlador.Stock)

      

    def __str__(self):
        string = "["
        Current = self.first
        while Current != None:
            string += str(Current)
            # Este simple condicional para arreglar el tema de la coma
            if Current.next != None:
                string += str(", ")
            Current = Current.next
        string += "]"
        return string

    # Cargar datos del CSV
    def cargaDatos(self):
        archivo = open(file = "src/archivos/datos.csv", mode = "r", encoding="UTF-8")
        print("\n>>> Cargando productos al sistema...")
        for lineas in archivo:
            sleep(0.2)
            self.formato = {
                "Nombre": "",
                "Descripcion": "",
                "Precio": 0,
                "Status": "",
                "Cantidad": 0,
                "Opciones": {
                    "Tamaños":[],
                    "Colores":[]
                },
                "Fecha Creacion": "",
                "Fecha Modificacion": ""
            }
            aux = lineas.split(",")
            opciones = aux[5].split("/")
            longitudes = opciones[0].split("-")
            colores = opciones[1].split("-")
            print("-> Agregando " + aux[0]+"...")
            self.formato["Nombre"] = aux[0]
            self.formato["Descripcion"] = aux[1]
            self.formato["Precio"] = float(aux[2])
            self.formato["Status"] = aux[3]
            self.formato["Cantidad"] = int(aux[4])
            self.formato["Opciones"]["Tamaños"] = longitudes
            self.formato["Opciones"]["Colores"] = colores
            self.formato["Fecha Creacion"] = aux[6]
            self.formato["Fecha Modificacion"] = aux[7].replace("\n", "")
            self.Append(self.formato)
        print("\n+-----------------+ Datos almacenados exitosamente +-----------------+\n")





""" Clase del menu principal """
class main:
    def __init__(self) -> None:
        # Cargar datos del CSV de manera automatica
        self.producto = ListaEnlazada()
        self.producto.cargaDatos()
        self.carrito = carrito.Carrito()
        self.orden = orden.Orden()
        self.menu()

    def menu(self):  # Metodo para capturar la opcion deseada
        while True:
            print("\n+----------+ MENU PRINCIPAL +----------+")
            print("| 1. Carrito de compra                 |")
            print("| 2. Orden de compra                   |")
            print("| 3. Controlador del sistema           |")
            print("| 4. Salir                             |")
            print("+--------------------------------------+")
            # Validacion de la captura de la opcion
            opcion = 0
            while opcion not in range(1, 5):
                try:
                    opcion = int(input(">>> Ingrese la opcion deseada: "))
                except:
                    print("-> Ingrese datos validos...")
            # Condicionales para filtrar las opciones
            if opcion == 1:
                print("\n=> Carrito de compra...")
                carrito.menu_carrito(self.producto, self.carrito) # Menu del carrito de compra

            elif opcion == 2:
                if not self.carrito.vacia():
                    print("\n =>Generar orden de compra...")

                    if not orden.menu_ordenCompra(controlador.Stock, self.orden): # Menu de la orden de compra
                        print("=> No ha generado la orden de compra")
                    else:
                        self.carrito = carrito.Carrito()
                else:
                    print("\n =>La lista de productos está vacía...\n")
            elif opcion == 3:
                print("\n=> Controlador del sistema...")
                controlador.menu(self.producto) # Menu del controlador
            else:
                print("\n=> Fin del programa...")
                break


if __name__ == "__main__":
    main()
    
