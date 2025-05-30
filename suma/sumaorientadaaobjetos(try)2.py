class Suma:
    def __init__(self):
        self.n1 = 0
        self.n2 = 0

    def pedir_datos(self):
        while True:
            try:
                self.n1 = int(input("Dame un número: "))
                break
            except ValueError:
                print("¡Error! Por favor, ingresa un número válido.")
        
        while True:
            try:
                self.n2 = int(input("Dame el segundo número: "))
                break
            except ValueError:
                print("¡Error! Por favor, ingresa un número válido.")

    def calcular_suma(self):
        return self.n1 + self.n2

    def mostrar_resultado(self):
        resultado = self.calcular_suma()
        print("El resultado es:", resultado)

operacion = Suma()
operacion.pedir_datos()
operacion.mostrar_resultado()
