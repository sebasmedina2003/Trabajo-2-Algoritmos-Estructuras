""" Orden de compra """

def menu_ordenCompra(productos):
        while True: 
            print("\n+----- ORDEN DE COMPRA -----+")
            print("| 1. Generar orden de compra  |")
            print("| 2. Salir                    |")
            print("+-----------------------------+")
            opcion = 0
            while opcion not in range(1, 3):
                try:
                    opcion = int(input(">>> Ingrese la opcion deseada: "))
                except:
                    print("-> Ingrese datos validos...")
            # Condicional opcion elegida
            if opcion == 1:
                pass
            else:
                break

class Orden: 
    def __init__(self, productos):
        self.cola = Cola
        self.productos = productos

    def generar_factura(self):
        print()

""" Producto -> Nodos"""
class Producto:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

""" Lista enlazada -> Colas """
class Cola:
    def __init__(self):
        self.frente = None
        self.fin = None

    def esta_vacia(self):
        return self.frente is None

    def agregar(self, valor):
        nodo_nuevo = Producto(valor) # Se añade un nodo con el valor del producto
        if self.esta_vacia():
            self.frente = nodo_nuevo
        else:
            self.fin.siguiente = nodo_nuevo
        self.fin = nodo_nuevo

    def eliminar(self):
        if self.esta_vacia():
            return None
        else:
            valor_eliminado = self.frente.valor
            self.frente = self.frente.siguiente
            if self.frente is None:
                self.fin = None
            return valor_eliminado
    
    def ver_frente(self):
        if self.esta_vacia():
            return None
        else:
            return self.frente.valor
    
    def recorrer(self):
        if self.esta_vacia():
            print("La cola está vacía")
        else:
            self._recorrer_aux(self.frente)
    
    def _recorrer_aux(self, nodo):
        if nodo is not None:
            print(nodo.valor.nombre)
            self._recorrer_aux(nodo.siguiente)