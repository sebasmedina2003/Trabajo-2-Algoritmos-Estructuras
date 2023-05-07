# Importar clases


class main:
    
    def menu(self): # Metodo para capturar la opcion deseada
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
          while opcion not in range(1,7):
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

          else:
             print("-> Ha salido del programa...")
             break
          

if __name__ == "__main__":
   principal = main()
   principal.menu()