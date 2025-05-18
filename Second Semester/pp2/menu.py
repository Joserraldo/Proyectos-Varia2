from establecimiento import Establecimiento

def menu():
    accion = Establecimiento()
    
    while True:
        print("Titulo")
        print("opciones....")
        
        opcion = int(input("Selecciona una opción >>> "))
        if opcion == 1:
            pass #ingresar datos
            
        elif opcion == 2:
            pass 
                
        elif opcion == 3:
            pass
        
        elif opcion== 4:
            accion.x()

        elif opcion==5:
            accion.y()
            
        elif opcion == 6:
            #para salir
            print("Gracias por utilizar este software de ... \nPowered by: \nDonaciones nequi:")
            accion.z()
            break
        else:
            print("Opción no valida, Intenta nuevamente")
    
    