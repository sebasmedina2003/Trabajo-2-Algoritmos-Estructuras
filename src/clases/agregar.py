import clases.controlador as controlador
from time import sleep

def cargaDatos(lista: list[dict]) -> list[dict]:
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
