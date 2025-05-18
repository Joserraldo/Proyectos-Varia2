from persona import Persona

class Producto(Persona):
    def __init__(self,nombre,cedula,fecha_nac,peso,talla):
        super().__init__(nombre,cedula,fecha_nac)
        self.peso = peso
        self.talla = talla
        self.imc = self.calcular_imc()
        self.diagnostico = self.diagnosticar()
    
    def calcular_imc(self):
        imc = round(self.peso/self.talla**2,2)
        return imc
    
    def diagnosticar(self):
        if self.imc < 18.5:
            return "Bajo peso"
        elif self.imc >= 18.5 and self.imc < 25:
            return "Peso Normal"
        elif self.imc >= 25 and self.imc < 30:
            return "Sobrepeso"
        elif self.imc >= 30 and self.imc < 35:
            return "Obesidad Grado I"
        elif self.imc >= 35 and self.imc < 40:
            return "Obesidad Grado II"
        else:
            return "Obesidad Grado III"