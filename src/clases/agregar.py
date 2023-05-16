import clases.controlador as controlador
from time import sleep

class Producto:
    def __init__(self, value):
        self.value = value
        self.next = None


class ListaEnlazada():
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

    def cargaDatos() -> list[dict]:
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
            longitud = listaAux[0]
            color = listaAux[1]
            diccionario = {"Longitud": longitud.split("-"), "Color":color.split("-")}
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
    
    def getFirst(self):
        return self.first
