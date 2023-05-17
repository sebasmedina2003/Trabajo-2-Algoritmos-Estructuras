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
                if current.value["Status"] == "Activo" and current.value["Cantidad"] > 0:
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
        lista = ListaEnlazada()
        archivo = open("src/archivos/datos.csv", "r")
        print("\n>>> Cargando productos al sistema...")
        for lineas in archivo:
            sleep(0.2)
            formato = {
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
            formato["Nombre"] = aux[0]
            formato["Descripcion"] = aux[1]
            formato["Precio"] = float(aux[2])
            formato["Status"] = aux[3]
            formato["Cantidad"] = int(aux[4])
            formato["Opciones"]["Tamaños"] = longitudes
            formato["Opciones"]["Colores"] = colores
            formato["Fecha Creacion"] = aux[6]
            formato["Fecha Modificacion"] = aux[7].replace("\n", "")
            lista.Append(formato)
        print("\n+-----------------+ Datos almacenados exitosamente +-----------------+\n")
        return lista





""" Clase del menu principal """
class main:
    def __init__(self) -> None:
        # Cargar datos del CSV de manera automatica
        self.Productos = ListaEnlazada().cargaDatos()
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
                carrito.menu_carrito(self.Productos) # Menu del carrito de compra

            elif opcion == 2:
                print("\n=>Generar orden de compra...")
                orden.menu_ordenCompra(self.Productos) # Menu de la orden de compra

            elif opcion == 3:
                print("\n=> Controlador del sistema...")
                controlador.menu(self.Productos) # Menu del controlador
            else:
                print("\n=> Fin del programa...")
                break


if __name__ == "__main__":
    main()
    