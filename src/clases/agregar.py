from datetime import time

def cargaDatos(lista: list[dict]) -> list[dict]:
    archivo = open("archivos/datos.csv", "r")
    print(">>> Cargando datos de prueba...")
    for lineas in archivo:
        time.sleep(0.5)
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
        print("-> Agregando " + aux[0]+"...")
        formato["Nombre"] = aux[0]
        formato["Descripcion"] = aux[1]
        formato["Precio"] = float(aux[2])
        formato["Status"] = aux[3]
        formato["Cantidad"] = int(aux[4])
        formato["Opciones"] = aux[5]
        formato["Fecha Creacion"] = aux[6]
        formato["Fecha Modificacion"] = aux[7].replace("\n", "")
        lista.append(formato)
    print("\n+-----------------+ Datos almacenados exitosamente +-----------------+\n")
    return lista
