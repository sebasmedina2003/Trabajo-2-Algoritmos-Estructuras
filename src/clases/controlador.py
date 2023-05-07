from datetime import datetime

def menu() -> None:
    while True: 
        print("\n+===========================================+\n" + "|" + "MENÚ".center(43," ") + "|\n" + "|===========================================|\n|                                           |\n| [1] Catálogo                              |\n| [2] Añadir al carrito                     |\n| [3] Comprar artíuclos                     |\n| [4] Ordenes de compra                     |\n| [5] Carrito de compra                     |\n| [6] Volver                                |\n|                                           |\n+===========================================+\n")
        opcion = 9
        while opcion not in range(1,7): 
            error = False
            try:
                opcion = int(input(">>> Seleccione la opción deseada: "))
                error = opcion not in range(1, 7)
                print(">>> Ha ingresado un numero fuera de rango\n" if error else "")
            except:
                error = True
                print(">>> No se ha ingresado un numero, seleccione una opcion valida\n")
            if not error:
                if opcion == 1:
                    print()
                elif opcion == 2:
                    print()
                elif opcion == 3:
                    print()
                elif opcion == 4:
                    print()
                elif opcion == 5:
                    print()
                elif opcion == 6:
                    break;
menu()



def catalogo():
    print()
catalogo()

def añadir_carrito():
    print()
añadir_carrito()

def comprar_carrito():
    print()
comprar_carrito()

def ordenes():
    print()
ordenes()

def carrito():
    print()
carrito()

def datos():
    print()
datos()