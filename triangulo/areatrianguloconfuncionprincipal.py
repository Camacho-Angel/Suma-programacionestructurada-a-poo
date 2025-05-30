class AREA:
    def __init__(self):
        self.h = 0
        self.b = 0

    def pedir_datos(self):
        self.h = float(input("Dame la altura: "))
        self.b = int(input("Dame la base: "))

    def calcular_area(self):
        return (self.h * self.b)/2

    def mostrar_resultado(self):
        resultado = self.calcular_area()
        print("El area es:", resultado)
def principal():
    operacion = AREA()
    operacion.pedir_datos()
    operacion.mostrar_resultado()

principal()    
