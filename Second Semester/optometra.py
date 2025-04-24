from persona import Persona

class Optometra(Persona):
    def __init__(self,nombre,cedula,fecha_nac,contacto,horas_sem,experiencia):
        super().__init__(nombre,cedula,fecha_nac,contacto)
        self.horas_sem = horas_sem
        self.experiencia = experiencia
        self.salario=self.calcular_salario()

    def calcular_salario(self):
            salario_base = 20000
            aumento= (1+(0.2*self.experiencia))
            #salario base por hora que trabaje
            salario = 4* (salario_base*self.horas_sem*aumento)
            return salario
    def diccionario(self):
        return {
            'nombre':self.nombre,
            'cedula':self.cedula,
            'fecha_nac':self.fecha_nac,
            'contacto':self.contacto,
            'horas_sem':self.horas_sem,
            'experiencia':self.experiencia,
            'salario':self.salario
            }

'''dan=Optometra
print(dan.calcular_salario(dan("dan",123,"13/10/2006",311,40,5)))'''
            

                
        


        

