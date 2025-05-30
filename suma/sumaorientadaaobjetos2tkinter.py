import tkinter as tk
from tkinter import messagebox

class SumaApp:
    def __init__(self, ventanaprincipal):
        self.ventanaprincipal = ventanaprincipal
        self.ventanaprincipal.title("Suma de dos números")

        
        self.label1 = tk.Label(ventanaprincipal, text="Dame un número:")
        self.label1.pack()
        self.entry1 = tk.Entry(ventanaprincipal)
        self.entry1.pack()

        self.label2 = tk.Label(ventanaprincipal, text="Dame el segundo número:")
        self.label2.pack()
        self.entry2 = tk.Entry(ventanaprincipal)
        self.entry2.pack()

        
        self.boton = tk.Button(ventanaprincipal, text="Calcular", command=self.calcular_suma)
        self.boton.pack()

        self.resultado_label = tk.Label(ventanaprincipal, text="Resultado:")
        self.resultado_label.pack()

    def calcular_suma(self):
        try:
            n1 = int(self.entry1.get())
            n2 = int(self.entry2.get())
            suma = n1 + n2
            self.resultado_label.config(text=f"Resultado: {suma}")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa solo números enteros.")

ventanaprincipal = tk.Tk()
app = SumaApp(ventanaprincipal)
ventanaprincipal.mainloop()
