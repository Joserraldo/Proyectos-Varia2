from optica import Optica

def menu():
    accion = Optica()
    
    while True:
        print("=-="*20)
        print("=-="*5,"[👁  Optica Universo Visual 👁 ]","=-="*4)
        print("=-="*20)
        print()
        print("=-="*8,"☰  MENU ☰","=-="*8)
        print("1. Ingresar usuario\n2. Mostrar datos ingresados\n3. Buscar usuario\n4. exportar/agregar/importar bases de datos \n5. Comprar productos\n6. Salir")

        print("=-="*20)
        
        opcion = int(input("Selecciona una opción para continuar >>> "))
        try:
            if opcion == 1:
                sub_opcion= int(input("¿Que desea añadir? \n1. Agregar cliente\n2. Agregar optometra\n3. Agregar producto"
                                    "\nSelecciona una opción para continuar >>> "))
                if sub_opcion == 1:
                    nombre = input("Digite el nombre del cliente >>> ")
                    cedula = int(input(f"Digite el numero de documento del cliente {nombre} >>> "))
                    fecha_nac= input(f"Digite la fecha de nacimiento de {nombre} >>> ")
                    contacto = int(input(f"Digite el numero telefonico de {nombre} >>> "))
                    resultados_d= float(input(f"digite el resultado de la prueba de distancia del ojo derecho de {nombre} >>> 20/"))
                    resultados_i= float(input(f"digite el resultado de la prueba de distancia del ojo izquierdo de {nombre} >>> 20/"))
                    accion.agregar_cliente(nombre,cedula,fecha_nac,contacto,resultados_d,resultados_i)
                    input("da enter para continuar...")

                elif sub_opcion ==2:
                    nombre = input("Digite el nombre del optometra >>> ")
                    cedula = int(input(f"Digite el numero de documento del optometra {nombre} >>> "))
                    fecha_nac= input(f"Digite la fecha de nacimiento de {nombre} >>> ")
                    contacto = int(input(f"Digite el numero telefonico de {nombre} >>> "))
                    horas_sem = int(input(f"Digite el numero de horas semanales que trabaja {nombre} >>> "))
                    experiencia = int(input(f"Digite los años de experiencia que tiene {nombre} >>> "))
                    accion.agregar_optometra(nombre,cedula,fecha_nac,contacto,horas_sem,experiencia)
                    input("da enter para continuar...")

                elif sub_opcion==3:
                    nombre = input("Digite el nombre del producto >>> ")
                    id= int(input("Digite el id del producto >>> "))
                    precio = int(input(f"Digite el precio del producto {nombre} >>> "))
                    stock = int(input(f"Digite el stock del producto >>> "))
                    if stock <=0:
                        stock = 0
                    accion.agregar_producto(nombre,id, precio, stock)
                    input("da enter para continuar...")
                else: 
                    input("Opción no valida, Presiona enter para intentar nuevamente...")

            #ingresar datos
            elif opcion == 2:
                sub_opcion= int(input("¿Que desea ver? \n1. Clientes\n2. Optometras\n3. Productos"
                                    "\nSelecciona una opción para continuar >>> "))
                if sub_opcion == 1:
                    accion.ver_cliente(accion.cliente)
                    input("da enter para continuar...")
                elif sub_opcion == 2:
                    accion.ver_optometra(accion.optometra)
                    input("da enter para continuar...")
                elif  sub_opcion == 3:
                    accion.ver_producto(accion.producto)
                    input("da enter para continuar...")
                else:
                    input("Opción no valida, Presiona enter para intentar nuevamente...")

            elif opcion == 3:
                id = int(input("Digite el numero de documento del usuario o producto >>> "))
                encontrado = accion.buscar(id)
                if encontrado :
                    try:
                        accion.ver_cliente(encontrado)
                    except AttributeError:
                        try:
                            accion.ver_optometra(encontrado)
                        except AttributeError:
                            try:
                                accion.ver_producto(encontrado)
                            except AttributeError:
                                print("Error atributo desconocido")
                    input("da enter para continuar...")
                else:
                    print("No hay ningun usuario o  producto con ese id")

                    
            elif opcion == 4:
                sub_opcion= int(input("1. Crear una nueva base de datos\n2. Añadir a una base de datos ya existente"
                                    "\n3. leer una base de datos\nselecciona una opcion para continuar >>> "))
                if sub_opcion == 1:
                    sub_opcion_2=int(input("¿Para quien crear la base de datos?\n1. Clientes\n2. Optometras"
                                    "\n3. Productos\nSelecciona una opción para continuar >>> "))
                    if sub_opcion_2 == 1:
                        accion.guardar("clientes.json")
                        input("da enter para continuar...")
                    elif sub_opcion_2 == 2:
                        accion.guardar("optometras.json")
                        input("da enter para continuar...")
                    elif sub_opcion_2==3:
                        accion.guardar("productos.json")
                        input("da enter para continuar...")
                    else:
                        input("Opción no valida, Presiona enter para intentar nuevamente...")

                if  sub_opcion == 2:
                    sub_opcion_2=int(input("Seleccione la base de datos en la que va a añadir algo nuevo"
                                        "\n1. Clientes\n2. Optometras\n3. Productos\nSelecciona una opción para continuar >>> "))
                    if sub_opcion_2 == 1:
                        accion.anadir("clientes.json")
                        input("da enter para continuar...")
                    elif sub_opcion_2 ==2:
                        accion.anadir("optometras.json")
                        input("da enter para continuar...")
                    elif sub_opcion_2 ==3:
                        accion.anadir("productos.json")
                        input("da enter para continuar...")
                    else:
                        input("Opción no valida, Presiona enter para intentar nuevamente...")   
                    
                if  sub_opcion == 3:
                    sub_opcion_2=int(input("Seleccione la base de datos desea visualizar en la terminal"
                                        "\n1. Clientes\n2. Optometras\n3. Productos\nSelecciona una opción para continuar >>> "))
                    if sub_opcion_2 == 1:
                        print(accion.importar("clientes.json"))
                        input("da enter para continuar...")
                    if sub_opcion_2 == 2:
                        print(accion.importar("optometras.json"))
                        input("da enter para continuar...")
                    if sub_opcion_2 == 3:
                        print(accion.importar("productos.json"))
                        input("da enter para continuar...")
                    else:
                        input("Opción no valida, Presiona enter para intentar nuevamente...")   

            elif opcion == 5:
                accion.importar("productos.json")
                accion.compra()
            elif opcion ==6: 
                #para salir
                print("Gracias por utilizar este software de Optometria\n Powered by: José Téllez. \nDonaciones nequi: 3115349124")
                break
            else:
                print("Opción no valida, Intenta nuevamente")

        except Exception as e:
                print("Error encontrado: ", e)
        
        '''def importar(self, ruta):
    with open(ruta, "r") as archivo:
        productos_dic = json.load(archivo)
        for producto_dic in productos_dic:
            producto = Producto(
                producto_dic["nombre"],
                producto_dic["id"],
                producto_dic["precio"],
                producto_dic["descripcion"],
                producto_dic["tipo"],
                producto_dic["stock"]
            )
            self.productos.append(producto)'''