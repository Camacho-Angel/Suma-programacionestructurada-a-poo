import tkinter as tk
from tkinter import messagebox

class AreaApp:
    def __init__(self, ventanaprincipal):
        self.ventanaprincipal = ventanaprincipal
        self.ventanaprincipal.title("AREA TRIANGULO")

        
        self.labelH = tk.Label(ventanaprincipal, text="Dame la altura:")
        self.labelH.pack()
        self.entry1 = tk.Entry(ventanaprincipal)
        self.entry1.pack()

        self.labelB = tk.Label(ventanaprincipal, text="Dame la base:")
        self.labelB.pack()
        self.entry2 = tk.Entry(ventanaprincipal)
        self.entry2.pack()

        
        self.boton = tk.Button(ventanaprincipal, text="Calcular", command=self.calcular_suma)
        self.boton.pack()

        self.resultado_label = tk.Label(ventanaprincipal, text="Resultado:")
        self.resultado_label.pack()

    def calcular_suma(self):
        try:
            h = float(self.entry1.get())
            b = float(self.entry2.get())
            area = (h*b)/2
            self.resultado_label.config(text=f"Resultado: {area}")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa solo números enteros.")

ventanaprincipal = tk.Tk()
app = AreaApp(ventanaprincipal)
ventanaprincipal.mainloop()