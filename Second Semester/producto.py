class Producto:
    def  __init__(self, nombre,id, precio, stock):
        self.nombre = nombre
        self.id=id
        self.precio = precio
        self.stock = stock
        self.tipo=self.hallar_tipo()
        self.hay_stock=self.si_hay_stock()

    def hallar_tipo(self):
        if self.nombre.startswith("gafas de vista"):
            return "Gafas formuladas"
        elif self.nombre.startswith("gafas de sol"):
            return "Gafas de sol"
        elif self.nombre.startswith("lentes"):
            return "Lentes de contacto"
        elif self.nombre.startswith("limpiador" or "solucion"):
            return "Soluciones"
        elif self.nombre.startswith("paño" or "cadena"):
            return "Accesorios"
        
    def  si_hay_stock(self):
        if self.stock:
            return True
        else:
            return False
        
    def diccionario(self):
        return {
            'nombre':self.nombre,
            'id':self.id,
            'precio':self.precio,
            'stock':self.stock,
            'tipo':self.tipo,
            'hay_stock':self.hay_stock
            }
