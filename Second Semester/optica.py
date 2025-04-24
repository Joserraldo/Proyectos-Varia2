from cliente import Cliente
from optometra import Optometra
from producto import Producto

import datetime as dt
import json 

class Optica:
    def __init__(self):
        self.clientes= []
        self.optometras=[]
        self.productos=[]
        self.cliente= None
        self.optometra= None
        self.producto=None
     
    def agregar_cliente(self,nombre,cedula,fecha_nac,contacto,resultados_d,resultados_i) :
        cliente = Cliente(nombre,cedula,fecha_nac,contacto,resultados_d,resultados_i)
        self.clientes.append(cliente)
        self.cliente = cliente   

    def agregar_optometra(self,nombre,cedula,fecha_nac,contacto,horas_sem,experiencia):
        optometra = Optometra(nombre,cedula,fecha_nac,contacto,horas_sem,experiencia)
        self.optometras.append(optometra)
        self.optometra = optometra
    
    def agregar_producto(self,nombre,id,precio,stock):
        producto = Producto(nombre,id,precio,stock)
        self.productos.append(producto)
        self.producto = producto
    
    def ver_cliente(self,cliente):
        titulo="=-="*5+"Información Cliente"+"=-="*5
        print(f"{titulo}\nNombre: {cliente.nombre}\nCedula: {cliente.cedula}\n"
            f"Edad: {cliente.edad} años\nContacto: +57 {cliente.contacto} \n"
            f"Diagnostico: {cliente.diagnostico}")
    
    def ver_optometra(self,optometra):
        titulo="=-="*5+"Información Optometra"+"=-="*5
        print(f"{titulo}\nNombre: {optometra.nombre}\nCedula: {optometra.cedula}\n"
            f"Edad: {optometra.edad} años\nContacto: +57 {optometra.contacto} \n"
            f"Salario: $ {optometra.salario} COP")
    
    def ver_producto(self,producto):
        titulo="=-="*5+"Información Producto"+"=-="*5
        print(f"{titulo}\nNombre: {producto.nombre}\nid: {producto.id}\n"
            f"Precio: ${producto.precio} COP\nTipo: {producto.tipo}")
        if producto.hay_stock ==True:
            print(f"Stock: {producto.stock} unidades")
        else:
            print("No hay stock disponible")

    def buscar(self,buscar_id):
        for cliente in self.clientes:
            if buscar_id == cliente.cedula:
                return cliente
            
        for optometra in self.optometras:
            if buscar_id == optometra.cedula:
                return optometra
            
        for producto in self.productos:
            if buscar_id == producto.id:
                return producto 
        return None

    def guardar(self, ruta):
        data = []
        if ruta == "clientes.json":
            data = [cliente.diccionario() for cliente in self.clientes]
        elif ruta == "optometras.json":
            data = [optometra.diccionario() for optometra in self.optometras]
        elif ruta == "productos.json":
            data = [producto.diccionario() for producto in self.productos]

        if data:
            with open(ruta, "w") as archivo:
                json.dump(data, archivo, indent=4)
                 

    def anadir(self,ruta):
                if ruta == "clientes.json":
                    clientes_dic = [cliente.diccionario() for cliente in self.clientes]
                    with open(ruta, "a") as archivo:
                        for  cliente in clientes_dic:
                            json.dump(cliente, archivo, indent=4)

                elif ruta == "optometras.json":
                    optometras_dic = [optometra.diccionario() for optometra in self.optometras]
                    with open(ruta, "a") as archivo:
                        for optometra in  optometras_dic:
                            json.dump(optometra, archivo, indent=4)

                elif ruta == "productos.json":
                    productos_dic = [producto.diccionario() for producto in self.productos]
                    with open(ruta, "a") as archivo:
                        for producto in  productos_dic:
                            json.dump(producto, archivo, indent=4)   
                print(f"Los datos han sido añadidos en la BD {ruta} exitosamente")
                
    def importar(self, ruta):
        with open(ruta,"r")as archivo:
            if ruta == "clientes.json":
                    cliente = json.load(archivo)
                    self.clientes.append(cliente)
                    return cliente
            elif ruta == "optometras.json":
                    optometra = json.load(archivo)
                    self.optometras.append(optometra) 
                    return optometra       
            elif ruta == "productos.json":
                    producto = json.load(archivo)
                    self.productos.append(producto)
                    return  producto

  
    
    def compra(self):
        print("Productos disponibles:")
        for i, producto in enumerate(self.productos):
            print(f"{i+1}. {producto['nombre']} - ${producto['precio']} COP - Stock: {producto['stock']}")

        while True:
            try:
                opcion = int(input("Seleccione un producto para comprar >>> "))
                if 1 <= opcion <= len(self.productos):
                    producto_seleccionado = self.productos[opcion - 1]
                    break
                else:
                    print("Opción no válida. Por favor, intenta nuevamente.")
            except ValueError:
                print("Entrada inválida. Por favor, ingresa un número.")

        while True:
            try:
                cantidad = int(input("Ingrese la cantidad que desea comprar >>> "))
                if cantidad <= 0:
                    print("La cantidad debe ser un número entero positivo.")
                elif cantidad > producto_seleccionado['stock']:
                    print("No hay suficiente stock para esta cantidad")
                else:
                    producto_seleccionado['stock'] -= cantidad
                    self.agregar_producto(producto_seleccionado['nombre'],producto_seleccionado['id'],producto_seleccionado['precio'],producto_seleccionado['stock'])
                    with open("productos.json", "w") as archivo:
                            json.dump(producto_seleccionado, archivo, indent=4)


                    print("-----------[ 👁 Factura de compra Optica Universo Visual 👁 ]-----------")
                    print(f"Has comprado {cantidad} unidades de {producto_seleccionado['nombre']} por un precio de {producto_seleccionado['precio']} COP")
                    print(f"El total es: ${producto_seleccionado['precio'] * cantidad} COP")
                    print(f"Con IVA (19%): ${(producto_seleccionado['precio'] * cantidad * 1.19)} COP")
                    input("Presiona enter para confirmar la compra ...")
                    break
            except ValueError:
                print("Entrada inválida. Por favor, ingresa un número.")
        
                        



            
        
        
        
    
