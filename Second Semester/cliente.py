from persona import Persona

class Cliente(Persona):
    def __init__(self,nombre,cedula,fecha_nac,contacto,resultado_d,resultado_i):
        super().__init__(nombre,cedula,fecha_nac,contacto)
        self.resultado_d = resultado_d
        self.resultado_i = resultado_i
        self.diagnostico = self.diagnosticar()

    def diagnosticar(self):
            #diagnostico ojo derecho
            if self.resultado_d == 20:
                x = "Vision Normal"
            elif 20 < self.resultado_d <= 40:
                x = "Miopia leve"
            elif 40 < self.resultado_d <= 60:
                x = "Miopia moderada"
            elif 60 < self.resultado_d <= 80:
                x = "Miopia severa"
            else:
                x = "¡valor fuera de rango, visite a un especialista!"
            #diagnostico ojo izquierdo
            if  self.resultado_i == 20:
                 y = "Vision Normal"
            elif 20 < self.resultado_i <= 40:
                y = "Miopia leve"
            elif 40 < self.resultado_i <= 60:
                y = "Miopia moderada"
            elif 60 < self.resultado_i <= 80:
                y = "Miopia severa"
            else:
                y = "¡valor fuera de rango, visite a un especialista!"

            return f"los resultados del analisis para el ojo derecho son: [{x}] \ny para el ojo izquierdo: [{y}]"
    
    def diccionario(self):
        return {
            'nombre':self.nombre,
            'cedula':self.cedula,
            'fecha_nac':self.fecha_nac,
            'contacto':self.contacto,
            'resultado_d':self.resultado_d,
            'resultado_i':self.resultado_i,
            'diagnostico':self.diagnostico
            }




'''accion=Cliente
print(accion.diagnosticar(Cliente("jose",1212,"13/10/2006",121,30,50)))'''   


        

