from time import sleep


def menu(lista) -> None:
    while True: 
        print("\n+===========================================+\n" + "|" + "MENÚ".center(43," ") + "|\n" + "|===========================================|\n|                                           |\n| [1] Catálogo                              |\n| [2] Añadir al carrito                     |\n| [3] Comprar artíuclos                     |\n| [4] Ordenes de compra                     |\n| [5] Carrito de compra                     |\n| [6] Volver                                |\n|                                           |\n+===========================================+\n")
        while True:
            try:
                opcion = int(input(">>> Seleccione la opción deseada: "))
                if opcion not in range(1, 7):
                    print(">>> Ha ingresado un numero fuera de rango\n")
                else:
                    break
            except ValueError:
                print(">>> No se ha ingresado un numero, seleccione una opcion valida\n")
        if opcion == 1:
            lista.catalogo()
        elif opcion == 2:
            Carrito.añadir_carrito()
        elif opcion == 3:
            Carrito.comprar_carrito()
        elif opcion == 4:
            print()
        elif opcion == 5:
            mostrarProductos(Carrito)
        elif opcion == 6:
            break;

class Producto:
    def __init__(self, value):
        self.value = value
        self.next = None

class Disponible:
    def __init__(self):
        self.first = None
        self.size = 0

    def Append(self, value):
        Nodo = Producto(value)
        if self.size == 0:
            self.first = Nodo
        else:
            Current = self.first
            while Current.next != None:
                Current = Current.next
            Current.next = Nodo
        self.size += 1

    def encontrar_nodo(self, i):
        current_node = self.first
        for k in range(i):
            current_node = current_node.next
        return current_node

    def Remove(self, i = None):
        if i == 0:
            value = self.first.value
            self.first = self.first.next
        else:
            node_before = self.encontrar_nodo(i-1)
            node_to_remove = node_before.next
            value = node_to_remove.value
            node_before.next = node_to_remove.next
            self.size = self.size - 1
        return value

class CarritoCompras:

    def __init__(self):
        self.first = None
        self.size = 0
    
    def Append(self, value):
        MyNode = Producto(value)
        if self.size == 0:
            self.first = MyNode
        else:
            Current = self.first
            while Current.next != None:
                Current = Current.next
            Current.next = MyNode
        self.size += 1
        return MyNode

    def encontrar_nodo(self, i):
        current_node = self.first
        for k in range(i):
            current_node = current_node.next
        return current_node

    def Remove(self, i = None):
        if i == 0:
            value = Carrito.first.value
            Carrito.first = Carrito.first.next
        else:
            node_before = self.encontrar_nodo(i-1)
            node_to_remove = node_before.next
            value = node_to_remove.value
            node_before.next = node_to_remove.next
            self.size = self.size - 1
        return value

    def añadir_carrito(self):
        mostrarProductos(Stock)
        opcion = -1
        while opcion not in range(0, Stock.size): 
            try:
                opcion = int(input(">>> Seleccione el producto que desea agregar al carrito: "))
            except:
                print(">>> No se ha ingresado un numero, seleccione una opcion valida\n")
        Current = Stock.first
        i = 0
        while Current != None:
            if i == opcion:
                Carrito.Append(Current.value)
                Stock.Remove(i)
                return Carrito
            i += 1
            Current = Current.next

    def comprar_carrito(self):
        mostrarProductos(Carrito)
        opcion = -1
        while opcion not in range(0, Carrito.size): 
            try:
                opcion = int(input(">>> Seleccione el producto que desea comprar: "))
            except:
                print(">>> No se ha ingresado un numero, seleccione una opcion valida\n")
        Current = self.first
        i = 0
        while Current != None:
            if i == opcion:
                Carrito.Remove(i)
                return Carrito
            i += 1
            Current = Current.next
            
# class Ordenes:

#     def __init__(self):
#         self.first = None
#         self.size = 0

#     def ordenes(self):
#         Current = self.first
#         i = 0
#         while Current != None:
#             print(str(i) + " " + str(Current) + "\n")
#             i += 1
#             Current = Current.next

def mostrarProductos(self):
    print("+" + "="*114 + "+")
    print("| I |       Nombre        |      Descripcion      | Precio |       Status       |  Cantidad  |       Opciones      |")
    print("+" + "="*114 + "+")
    Current = self.first
    i = 0
    while Current != None:
        if Current.value == "Comprar Todo":
            sleep(0.5)
            print("| {:0} |{:<110}|".format(i, "Comprar Todo"))
        else:
            sleep(0.5)
            print("| {:0} |{:<18}|{:<25}|${:5}|{:<9}|{:<5}|{:25}|{:<10}|{:<10}|".format(i, str(Current.value["Nombre"]), str(Current.value["Descripcion"]), float(Current.value["Precio"]), str(Current.value["Status"]), str (Current.value["Cantidad"]), str(Current.value["Opciones"]), str(Current.value["Fecha Creacion"]), str(Current.value["Fecha Modificacion"])))
        print("+" + "="*114 + "+")
        i+=1
        Current = Current.next
    print("\n")

Stock = Disponible()
Carrito = CarritoCompras()

