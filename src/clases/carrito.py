from clases.controlador import mostrarProductos
""" Carrito de compra """
def menu_carrito(productos):
        carrito = Carrito
        while True:
            print("\n+--------- CARRITO DE COMPRA ----------+")
            print("| 1. Agregar productos                  |")
            print("| 2. Eliminar productos                 |")
            print("| 3. Total de compra                    |")
            print("| 4. Salir                              |")
            print("+---------------------------------------+")
            opcion = 0
            while opcion not in range(1, 5):
                try:
                    opcion = int(input(">>> Ingrese la opcion deseada: "))
                except:
                    print("-> Ingrese datos validos...")
            # Condicional opcion elegida
            if opcion == 1:
                mostrarProductos(productos)
                while True:
                    try:
                        opcion = input("=> Ingrese el indice del producto que desea agregar: ")
                    except:
                        print("=> Ingrese un indice valido...")
                    # Recorrer la lista enlazada en busca del producto
                    contador = 0
                    
                Carrito.agregar_producto(carrito, opcion) # Agregar productos a la pila
            elif opcion == 2:
                mostrarProductos(Pila)
                Carrito.eliminar_productos(carrito) # Eliminar productos de la pila
            elif opcion == 3:
                Carrito.total(carrito) # Calcular el total de los productos almacenados en la pila
            else:
                break


""" Producto -> Nodos"""
class Producto:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


""" Lista enlazada -> Pilas """
class Pila:
    def __init__(self):
        self.tope = None
    
    def vacia(self):
        return self.tope is None
    
    def agregar(self, valor):
        new = Producto(valor) # Se añade un nodo con el valor del producto
        new.siguiente = self.tope
        self.tope = new
    
    def eliminar(self):
        if self.esta_vacia():
            return None
        else:
            valor_eliminado = self.tope.valor
            self.tope = self.tope.siguiente
            return valor_eliminado
    
    def recorrerPila(self):
        if self.esta_vacia():
            print("La pila está vacía")
        else:
            self.aux(self.tope)

    def aux(self, nodo):
        if nodo is not None:
            print()
            self.aux(nodo.siguiente)

""" Clase carrito """
class Carrito(Pila):
    def __init__(self):
        super.__init__()

    def agregar_producto(self, producto):
        Pila.agregar(producto)
        pass

    def eliminar_productos(self):
        if Pila.vacia():
            print("=> No hay productos en el carrito a eliminar...")
        else:
            # Recorrer la pila hasta encontrar el nodo que se desea eliminar
            print("=> Ingrese el indice del producto que desea eliminar de la pila...")
            pass

    def total(self):
        if Pila.vacia():
            print("=> No hay productos en el carrito a eliminar...")
        else:
            pass
            # Recorrer la pila calculando los precios de los productos agregados