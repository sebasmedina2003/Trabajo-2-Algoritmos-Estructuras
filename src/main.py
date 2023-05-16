# Importar clases
from clases import agregar as agregar
import clases.controlador as controlador
from time import sleep

class Producto:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)
class ListaEnlazada:
    def __init__(self):
        self.first = None
        self.size = 0

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
        while current != None:
            if current.value["Status"] == "Activo" and current.value["Cantidad"] > 0:
                controlador.mostrarProductos(current.value)
            current = current.next

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

    def cargaDatos(self):
        lista = ListaEnlazada()
        archivo = open("src/archivos/datos.csv", "r")
        print("\n>>> Cargando datos de prueba...")
        for lineas in archivo:
            sleep(0.2)
            formato = {
                "Nombre": "",
                "Descripcion": "",
                "Precio": 0,
                "Status": "",
                "Cantidad": 0,
                "Opciones": "",
                "Fecha Creacion": "",
                "Fecha Modificacion": ""
            }
            aux = lineas.split(",")
            listaAux = aux[5].split("/")
            listaOpciones = listaAux[0]
            textoValores = listaAux[1]
            listaValores = textoValores.split("-")
            diccionario = {listaOpciones: listaValores}
            print("-> Agregando " + aux[0]+"...")
            formato["Nombre"] = aux[0]
            formato["Descripcion"] = aux[1]
            formato["Precio"] = float(aux[2])
            formato["Status"] = aux[3]
            formato["Cantidad"] = int(aux[4])
            formato["Opciones"] = diccionario
            formato["Fecha Creacion"] = aux[6]
            formato["Fecha Modificacion"] = aux[7].replace("\n", "")
            lista.Append(formato)
        print("\n+-----------------+ Datos almacenados exitosamente +-----------------+\n")
        return lista
class main:
    def __init__(self) -> None:
        self.Productos = ListaEnlazada()
        self.Productos = self.Productos.cargaDatos()
        print(self.Productos)
        self.menu()


    def menu(self):  # Metodo para capturar la opcion deseada
        while True:
            print("\n+----------+ Menu principal +----------+")
            print("| 1. Agregar productos                 |")
            print("| 2. Acceder a opciones de productos   |")
            print("| 3. Acceder al carrito de compra      |")
            print("| 4. Acceder al orden                  |")
            print("| 5. Acceder al controlador            |")
            print("| 6. Salir del programa                |")
            print("+--------------------------------------+")
            # Validacion de la captura de la opcion
            opcion = 9
            while opcion not in range(1, 7):
                try:
                    opcion = int(input(">>> Ingrese la opcion deseada: "))
                except:
                    print("-> Ingrese datos validos...")
            # Condicionales para filtrar las opciones
            if opcion == 1:
                print("-> Puede agregar productos al sistema...")

            elif opcion == 2:
                print("-> Puede ver las opciones de los productos del sistema...")

            elif opcion == 3:
                print("-> Ha ingresado al carrito de compra...")

            elif opcion == 4:
                print("-> Ha ingresado al orden de compra...")

            elif opcion == 5:
                print("-> Ha ingresado al controlador del sistema...")
                controlador.inicializar(self.Productos)
            else:
                print("-> Ha salido del programa...")
                break


if __name__ == "__main__":
    main()
