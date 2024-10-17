import tkinter as tk
from tkinter import *
from math import factorial
from PIL import Image, ImageTk

class Container(tk.Frame):
    def __init__(self, padre, controlador):
        super().__init__(padre)
        self.controlador = controlador
        self.pack()
        self.place(x=0, y=0, width=800, height=400)
        
        self.canvas = tk.Canvas(self, width=800, height=400)
        self.canvas.pack(fill="both", expand=True)
        
        self.dibujar_degradado()
        
        self.widgets()

    def dibujar_degradado(self):
        for i in range(400):
            color = self.degradado_color(i, 400, "#7bcf7d", "#000000")
            self.canvas.create_line(0, i, 800, i, fill=color, width=2)

    def degradado_color(self, i, total, color1, color2):
        r1, g1, b1 = int(color1[1:3], 16), int(color1[3:5], 16), int(color1[5:7], 16)
        r2, g2, b2 = int(color2[1:3], 16), int(color2[3:5], 16), int(color2[5:7], 16)
        
        r = int(r1 + (r2 - r1) * i / total)
        g = int(g1 + (g2 - g1) * i / total)
        b = int(b1 + (b2 - b1) * i / total)
        
        return f"#{r:02x}{g:02x}{b:02x}"

    def show_frames(self, container):
        top_level = tk.Toplevel(self)
        frame = container(top_level)
        frame.config(bg="#7bcf7d")
        frame.pack(fill="both", expand=True)
        top_level.geometry("600x400+120+20")
        top_level.resizable(False, False)

        top_level.transient(self.master)
        top_level.grab_set()
        top_level.focus_set()
        top_level.lift()

    def permutaciones(self):
        self.show_frames(Permutaciones)

    def combinaciones(self):
        self.show_frames(Combinaciones)

    def widgets(self):
        frame1 = tk.Frame(self, bg="#7bcf7d")
        frame1.place(x=0, y=0, width=800, height=400)

        btn_permutaciones = Button(frame1, bg="#8de858", fg="black", font="sans 18 bold", text="Ir a Permutaciones", command=self.permutaciones)
        btn_permutaciones.place(x=500, y=30, width=240, height=60)

        btn_combinaciones = Button(frame1, bg="#d4f121", fg="black", font="sans 18 bold", text="Ir a Combinaciones", command=self.combinaciones)
        btn_combinaciones.place(x=500, y=130, width=240, height=60)

        self.logo_image = Image.open("imagenes/link.jpeg")
        self.logo_image = self.logo_image.resize((280,280))
        self.logo_image = ImageTk.PhotoImage(self.logo_image)
        self.logo_label = tk.Label(frame1, image=self.logo_image, bg="#7bcf7d")
        self.logo_label.place(x=100, y=30)

        copyright_label = tk.Label(frame1, text="© 2024 PaluZero Code. Todos los derechos reservados", font="sans 12 bold", bg="#7bcf7d", fg="white")
        copyright_label.place(x=180, y=350)

class Permutaciones(tk.Frame):
    def __init__(self, padre):
        super().__init__(padre)
        self.config(bg="#7bcf7d")
        self.pack(fill="both", expand=True)

        tk.Label(self, text="Cálculo de Permutaciones", font="Arial 18 bold", bg="#7bcf7d", fg="white").pack(pady=20)

        tk.Label(self, text="Número total de elementos (n):", font="Arial 12", bg="#7bcf7d", fg="white").pack(pady=5)
        self.entry_n = tk.Entry(self, font="Arial 12")
        self.entry_n.pack(pady=5)

        tk.Label(self, text="Número de elementos a seleccionar (r):", font="Arial 12", bg="#7bcf7d", fg="white").pack(pady=5)
        self.entry_r = tk.Entry(self, font="Arial 12")
        self.entry_r.pack(pady=5)

        tk.Label(self, text="¿Permitir repetición?", font="Arial 12", bg="#7bcf7d", fg="white").pack(pady=5)
        self.var_repeticion = tk.BooleanVar()
        tk.Checkbutton(self, text="Sí", variable=self.var_repeticion).pack(pady=5)

        tk.Button(self, text="Calcular Permutación", command=self.calcular_permutacion, font="Arial 12 bold", bg="#8de858").pack(pady=20)

        self.result_label = tk.Label(self, text="Resultado:", font="Arial 14 bold", bg="#7bcf7d", fg="white")
        self.result_label.pack(pady=10)

    def calcular_permutacion(self):
        try:
            n = int(self.entry_n.get())
            r = int(self.entry_r.get())

            if self.var_repeticion.get():
                resultado = n ** r  
            else:
                resultado = factorial(n) // factorial(n - r)  

            self.result_label.config(text=f"Resultado: {resultado}")
        except ValueError:
            self.result_label.config(text="Error: Ingrese números válidos.")

class Combinaciones(tk.Frame):
    def __init__(self, padre):
        super().__init__(padre)
        self.config(bg="#7bcf7d")
        self.pack(fill="both", expand=True)

        tk.Label(self, text="Cálculo de Combinaciones", font="Arial 18 bold", bg="#7bcf7d", fg="white").pack(pady=20)

        tk.Label(self, text="Número total de elementos (n):", font="Arial 12", bg="#7bcf7d", fg="white").pack(pady=5)
        self.entry_n = tk.Entry(self, font="Arial 12")
        self.entry_n.pack(pady=5)

        tk.Label(self, text="Número de elementos a seleccionar (r):", font="Arial 12", bg="#7bcf7d", fg="white").pack(pady=5)
        self.entry_r = tk.Entry(self, font="Arial 12")
        self.entry_r.pack(pady=5)

        tk.Label(self, text="¿Permitir repetición?", font="Arial 12", bg="#7bcf7d", fg="white").pack(pady=5)
        self.var_repeticion = tk.BooleanVar()
        tk.Checkbutton(self, text="Sí", variable=self.var_repeticion).pack(pady=5)

        tk.Button(self, text="Calcular Combinación", command=self.calcular_combinacion, font="Arial 12 bold", bg="#d4f121").pack(pady=20)

        self.result_label = tk.Label(self, text="Resultado:", font="Arial 14 bold", bg="#7bcf7d", fg="white")
        self.result_label.pack(pady=10)

    def calcular_combinacion(self):
        try:
            n = int(self.entry_n.get())
            r = int(self.entry_r.get())

            if self.var_repeticion.get():
                resultado = factorial(n + r - 1) // (factorial(r) * factorial(n - 1))  
            else:
                resultado = factorial(n) // (factorial(r) * factorial(n - r))  

            self.result_label.config(text=f"Resultado: {resultado}")
        except ValueError:
            self.result_label.config(text="Error: Ingrese números válidos.")

def mostrar_menu():
    ventana_menu = tk.Tk()
    ventana_menu.title("Menú Principal")

    container = Container(ventana_menu, None)
    container.pack(fill="both", expand=True)

    ventana_menu.geometry("800x400+120+20")
    ventana_menu.resizable(False, False)
    ventana_menu.mainloop()

mostrar_menu()





