class Casas:
    def __init__(self, numero, propietario, pisos,multas):
        self.numero = numero
        self.propietario = propietario
        self.pisos = pisos
        self.multas = multas
        self.pago_multas =self.calcular_pago_multas()
        self.admon = self.calcular_admon()
        
    def calcular_pago_multas(self):
        if self.multas<=3:
            return self.multas*30000
        elif self.multas<=6:
            return self.multas*40000
        elif self.multas<=9:
            return self.multas*50000
        else:
            return self.multas*60000
        
    def calcular_admon(self):
        # Aquí se calcularía el costo de la administración según la cantidad de pisos
        admon_base = 300000
        incremento_piso = 50000
        return self.calcular_pago_multas()+admon_base + ((self.pisos-1) * incremento_piso)
    
    def presentar(self):
        return {
                    "Número de Casa": self.numero,
                    "Propietario": self.propietario,
                    "Número de Pisos": self.pisos,
                    "Número de Multas": self.multas,
                    "Pago de Multas": self.calcular_pago_multas(),
                    "Pago de Administración": self.calcular_admon()
                }
    