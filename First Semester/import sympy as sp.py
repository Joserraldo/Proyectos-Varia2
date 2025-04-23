from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, StringVar, W, N , E ,S, ttk, simpledialog, messagebox
from tkinter.ttk import *
from decimal import Decimal 
from fractions import Fraction
import numpy as np
from random import randint
import sympy as sp
import tkinter as tk
from numpy import matrix
import math
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib import style
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from math import *
from numpy import *
import warnings
import customtkinter
from sympy import symbols, integrate,simplify,pretty, Eq, solve
from tkinter.messagebox import askyesno
from sympy.parsing.sympy_parser import parse_expr

root = tk.Tk()
root.geometry('500x500')
root.title("prueba")
def resolver_x():
         
    resultado=None

ventana1 = tk.Toplevel()
ventana1.title("Resolver x")
ventana1.config(bg="#FFFFFF")
ventana1.geometry("500x500")



frame=customtkinter.CTkFrame(master=ventana1,fg_color="#f0f0f0")
frame.pack(pady=20, padx= 20, fill= "both", expand= True) 
x = symbols('x')

entrada_ecuacion=customtkinter.CTkEntry(master=frame,width=200,height=30,border_color="#f0f0f0",fg_color="#ffffff",text_color="#000000")
entrada_ecuacion.place(x=140,y=130)

titulo1=customtkinter.CTkLabel(master=frame,text="Escriba la ecuación hallar para x",font=("Arial",28),text_color="#000000")
titulo1.pack()

def calculado():    
    expresion_str = entrada_ecuacion.get()
    try:
        # Definir la variable
        x = symbols('x')

        # Parsear la expresión ingresada por el usuario
        ecuacion = Eq(parse_expr(expresion_str), 0)

        # Resolver la ecuación
        soluciones = solve(ecuacion, x)

        # Mostrar las soluciones en la etiqueta

        rta = solve(ecuacion, x)
        rta_x = pretty(rta)

        resultado=customtkinter.CTkLabel(frame,text=f"El valor de x para su ecuación es: \n {rta_x}",text_color="#000000",font=("Arial",25))
        resultado.place(x=60,y=260)
    except Exception as e:
        resultado=customtkinter.CTkLabel(frame,text=f'Error: {str(e)}',text_color="#000000",font=("Arial",25))
        resultado.place(x=60,y=260)

        rta_x = solve(ecuacion, x)
         



respuesta_x=customtkinter.CTkButton(frame,text="Hallar x",command=calculado,fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
respuesta_x.place(x=160,y=200)
        

def confirmar():
    ans = askyesno(title="Salir", message= '¿Deseas salir?')
    if ans:
        root.destroy()

root.protocol('WM_DELETE_WINDOW', confirmar)
root.mainloop()



