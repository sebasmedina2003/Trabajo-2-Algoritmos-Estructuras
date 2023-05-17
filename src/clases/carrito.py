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
                Carrito.agregar_producto(carrito) # Agregar productos a la pila
            elif opcion == 2:
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
    
    def esta_vacia(self):
        return self.tope is None
    
    def agregar(self, valor):
        nodo_nuevo = Producto(valor) # Se añade un nodo con el valor del producto
        nodo_nuevo.siguiente = self.tope
        self.tope = nodo_nuevo
    
    def eliminar(self):
        if self.esta_vacia():
            return None
        else:
            valor_eliminado = self.tope.valor
            self.tope = self.tope.siguiente
            return valor_eliminado
        
    def ver_tope(self):
        if self.esta_vacia():
            return None
        else:
            return self.tope.valor
    
    def recorrer(self):
        if self.esta_vacia():
            print("La pila está vacía")
        else:
            self._recorrer_aux(self.tope)

    def _recorrer_aux(self, nodo):
        if nodo is not None:
            print(nodo.valor.nombre)
            self._recorrer_aux(nodo.siguiente)

""" Clase carrito """
class Carrito(Pila):
    def super__init__(self):
        self.pila = Pila

    def agregar_producto(self):
        #self.pila.agregar(producto)
        pass

    def eliminar_productos(self):
        if self.pila.esta_vacia:
            print("=> No hay productos en el carrito a eliminar...")
        else:
            # Recorrer la pila hasta encontrar el nodo que se desea eliminar
            print("=> Ingrese el indice del producto que desea eliminar de la pila...")
            pass

    def total(self):
        if self.pila.esta_vacia():
            print("=> No hay productos en el carrito a eliminar...")
        else:
            pass
            # Recorrer la pila calculando los precios de los productos agregados