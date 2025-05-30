class Area:
    def __init__(self):
        self.h = 0
        self.b = 0

    def pedir_datos(self):
        while True:
            try:
                self.h = float(input("Dame la altura: "))
                break
            except ValueError:
                print("¡Error! Por favor, ingresa un número.")
        
        while True:
            try:
                self.b = float(input("Dame la base: "))
                break
            except ValueError:
                print("¡Error! Por favor, ingresa un número.")

    def calcular_area(self):
        return (self.b + self.h)/2

    def mostrar_resultado(self):
        resultado = self.calcular_area()
        print("El area es:", resultado)

operacion = Area()
operacion.pedir_datos()
operacion.mostrar_resultado()