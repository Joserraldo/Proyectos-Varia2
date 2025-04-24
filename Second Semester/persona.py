import datetime as dt

class Persona:
    def __init__(self,nombre,cedula,fecha_nac,contacto):
        self.nombre = nombre
        self.cedula = cedula
        self.fecha_nac = fecha_nac
        self.contacto = contacto
        self.edad = self.calcular_edad()
        
        
    def calcular_edad(self):
        hoy = dt.date.today()
        fecha_nac = dt.datetime.strptime(self.fecha_nac,'%d/%m/%Y').date()
        edad = hoy.year - fecha_nac.year - ((hoy.month,hoy.day)<(fecha_nac.month,fecha_nac.day))
        return edad