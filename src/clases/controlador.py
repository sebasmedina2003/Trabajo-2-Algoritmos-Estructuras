import clases.agregar as agregar
import time


def inicializar(lista):
    global MyList
    MyList = lista
    menu()


def menu() -> None:
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
            MyList.catalogo()
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
class ListaEnlazada(list):

    def __init__(self):
        self.first = None
        self.size = 0
        self.band = False
        
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
                if current.value[3] == "Activo" and current.value[4] > 0:
                    Stock2.Append(current.value)
                    Stock.Append(current.value)
                    self.band = True
                current = current.next
        mostrarProductos(Stock2)
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

    def Remove(self, value):
        if self.size == 0:
            return False
        else:
            Current = self.first
            try:
                while Current.next.value != value:
                    if Current.next == None:
                        return False
                    else:
                        Current = Current.next
                DeletedNode = Current.next
                Current.next = DeletedNode.next
            except AttributeError:
                return False
        self.size -= 1
        return DeletedNode
# class CarritoCompras:

#     def __init__(self):
#         self.first = None
#         self.size = 0
    
#     def Append(self, value):
#         MyNode = Producto(value)
#         if self.size == 0:
#             self.first = MyNode
#         else:
#             Current = self.first
#             while Current.next != None:
#                 Current = Current.next
#             Current.next = MyNode
#         self.size += 1
#         return MyNode

#     def Remove(self, value):
#         if self.size == 0:
#             return False
#         else:
#             Current = self.first
#             try:
#                 while Current.next.value != value:
#                     if Current.next == None:
#                         return False
#                     else:
#                         Current = Current.next
#                 DeletedNode = Current.next
#                 Current.next = DeletedNode.next
#             except AttributeError:
#                 return False
#         self.size -= 1
#         return DeletedNode

#     def añadir_carrito(self):
#         Actual = Carrito.first
#         while Actual != None:
#             Stock.Remove(Actual.value)
#             Actual = Actual.next
#         mostrarProductos(Stock)
#         opcion = -1
#         while opcion not in range(0, Stock.size): 
#             try:
#                 opcion = int(input(">>> Seleccione el producto que desea agregar al carrito: "))
#             except:
#                 print(">>> No se ha ingresado un numero, seleccione una opcion valida\n")
#         Current = Stock.first
#         i = 0
#         while Current != None:
#             if i == opcion:
#                 Carrito.Append(Current.value)
#                 return Carrito
#             i += 1
#             Current = Current.next

#     def comprar_carrito(self):
        
#         mostrarProductos(Carrito)
#         opcion = -1
#         while opcion not in range(0, self.size): 
#             try:
#                 opcion = int(input(">>> Seleccione el producto que desea comprar: "))
#             except:
#                 print(">>> No se ha ingresado un numero, seleccione una opcion valida\n")
#         Current = self.first
#         i = 0
#         while Current != None:
#             if i == opcion:
#                 Carrito.Remove(Current.value)
#                 return Carrito
#             i += 1
#             Current = Current.next
            
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
            time.sleep(0.5)
            print("| {:0} |{:<110}|".format(i, "Comprar Todo"))
        else:
            time.sleep(0.5)
            print("| {:0} |{:<21}|{:<23}|${:<7}|{:<20}|{:<12}|{:<21}|".format(i, Current.value[0], Current.value[1], Current.value[2], Current.value[3], Current.value[4], Current.value[5]))
        print("+" + "="*114 + "+")
        i+=1
        Current = Current.next
    print("\n")


Carrito = ListaEnlazada()
Stock2 = ListaEnlazada()
Stock = ListaEnlazada()
