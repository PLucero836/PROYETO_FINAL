from tkinter import *
import tkinter as tk
from ventas import Ventas
from inventario import Inventario
from clientes import ControlClientes
from PIL import Image, ImageTk

class Container(tk.Frame):
    def __init__(self, padre, controlador):
        super().__init__(padre)
        self.controlador = controlador
        self.pack()
        self.place(x=0, y=0, width=800, height=400)
        self.config(bg="#66cc66")  
        self.widgets()

    def show_frames(self, container):
        top_level = tk.Toplevel(self)
        frame = container(top_level)
        frame.config(bg="#66cc66")  
        frame.pack(fill="both", expand=True)
        top_level.geometry("1100x650+120+20")
        top_level.resizable(False, False)

        top_level.transient(self.master)
        top_level.grab_set()
        top_level.focus_set()
        top_level.lift()

    def ventas(self):
        self.show_frames(Ventas)

    def inventario(self):
        self.show_frames(Inventario)

    def clientes(self):
        self.show_frames(ControlClientes)

    def widgets(self):

        frame1 = tk.Frame(self, bg="#66cc66")  
        frame1.pack()
        frame1.place(x=0, y=0, width=800, height=400)

        btnventas = Button(frame1, bg="#7ed9ff", fg="black", font="sans 18 bold", text="Ir a ventas", command=self.ventas)
        btnventas.place(x=500, y=30, width=240, height=60)

        btninventario = Button(frame1, bg="#f1d121", fg="black", font="sans 18 bold", text="Ir a inventario", command=self.inventario)
        btninventario.place(x=500, y=130, width=240, height=60)

        btnclientes = Button(frame1, bg="#4ad2ff", fg="black", font="sans 18 bold", text="Ir a clientes", command=self.clientes)
        btnclientes.place(x=500, y=230, width=240, height=60)

        self.logo_image = Image.open("imagenes/link.jpeg")
        self.logo_image = self.logo_image.resize((280, 280))
        self.logo_image = ImageTk.PhotoImage(self.logo_image)
        self.logo_label = tk.Label(frame1, image=self.logo_image, bg="#66cc66")  
        self.logo_label.place(x=100, y=30)

        copyright_label = tk.Label(frame1, text="© 2024 PaluZero Code. Todos los derechos reservados", font="sans 12 bold", bg="#66cc66", fg="white")
        copyright_label.place(x=180, y=350)