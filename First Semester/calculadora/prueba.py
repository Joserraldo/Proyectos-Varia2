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
from sympy import symbols, integrate,simplify,pretty
from tkinter.messagebox import askyesno

potencia = {
    '^': '**'
    
}
def calculadora():
    def ingresarValores(tecla):
        if tecla >= '0' and tecla <= '9' or tecla == '(' or tecla == ')' or tecla == '.' or tecla == '**':
            entrada2.set(entrada2.get() + tecla)
            
        if tecla == '*' or tecla == '/' or tecla == '+' or tecla == '-' or tecla == 'Mod' or tecla == 'Div':
            if tecla == '*':
                entrada1.set(entrada2.get() + '*')
            elif tecla == '/':
                entrada1.set(entrada2.get() + '/')
            elif tecla == '+':
                entrada1.set(entrada2.get() + '+')
            elif tecla == '-':
                entrada1.set(entrada2.get() + '-')
            elif tecla == '**':
                entrada1.set(entrada2.get() + '**' ) 
            elif tecla == 'Mod':
                entrada1.set(entrada2.get() + '%')
            elif tecla == 'Div':
                entrada1.set(entrada2.get() + '//')
            entrada2.set('')
        if tecla == "=":
            entrada1.set(entrada1.get() + entrada2.get())
            resultado = eval(entrada1.get())
            entrada2.set(resultado)


    def euler():
        entrada1.set('')
        resultado = math.e
        entrada2.set(resultado)
    def redon():
        entrada1.set('')
        resultado = round(float(entrada2.get()))
        entrada2.set(resultado)
    def raiz_cuadrada():
        entrada1.set('')
        resultado = math.sqrt(float(entrada2.get()))
        entrada2.set(resultado)    
    def pi():

        entrada1.set('')
        resultado = math.pi
        entrada2.set(resultado)
    def log10n():
        entrada1.set('')
        resultado = log10(float(entrada2.get()))
        entrada2.set(resultado)

    def numero_aureo():
        entrada1.set('')
        resultado  = (1 + math.sqrt(5)) / 2
        entrada2.set(resultado)
    def sen():
        entrada1.set('')
        resultado = sin(((float(entrada2.get())) * math.pi)/180)
        if resultado < 1e-15 and resultado > 0 or resultado < 0 and resultado > -1e-10:
            resultado = 0.0

        entrada2.set(resultado)
    def coss():
        entrada1.set('')
        resultado = cos((((float(entrada2.get())) * math.pi)/180))
        if abs(resultado) < 1e-15:
            resultado = 0.0
        entrada2.set(resultado)
    def tann():
        entrada1.set('')
        resultado = tan(((float(entrada2.get())) * math.pi)/180)
        if abs(resultado) > 1e15:
            resultado = 'Indefinido'
        elif resultado < 1e-15 and resultado > 0 or resultado < 0 and resultado > -1e-10:
            resultado = 0.0

        entrada2.set(resultado)
    def cotan():
        entrada1.set('')
        
        resultado = 1/(tan(((float(entrada2.get())) * math.pi)/180))

        if abs(resultado) < 1e-15:
            resultado = 0.0
        elif abs(resultado) >= 2*math.pi:
            resultado = 'Indefinido'
        entrada2.set(resultado)
    def sec():
        
        entrada1.set('')
        resultado = 1/(cos(((float(entrada2.get())) * math.pi)/180))
        if abs(resultado) < 1e-15:
            resultado = 0.0
        elif abs(resultado) > 1e15:
            resultado = 'Indefinido'
        entrada2.set(resultado)
    def csc():
        
        entrada1.set('')
        resultado = 1/(sin(((float(entrada2.get())) * math.pi)/180))
        if abs(resultado) < 1e-15:
            resultado = 0.0
        elif abs(resultado) > 1e15:
            resultado = 'Indefinido'
        entrada2.set(resultado)
        
    def asen():
        entrada1.set('') 
        valor_ingresado = float(entrada2.get())  
        resultado = degrees(arcsin(valor_ingresado)) 
        if valor_ingresado >= -1 and valor_ingresado <= 1: 
            if abs(resultado) < 1e-15:
                resultado = 0.0
        elif abs(resultado) > 1e15:
            resultado = 'Indefinido'
        else:
            resultado = 'Fuera de rango' 

        entrada2.set(resultado) 
    
    def acos():


        valor_ingresado = float(entrada2.get())

    
        if valor_ingresado >= -1 and valor_ingresado <= 1:
            resultado_radianes = arccos(valor_ingresado)
            resultado_grados = degrees(resultado_radianes)
        else:
            resultado_grados = 'Fuera de rango'

        entrada2.set(resultado_grados) 

    def absoluto():
        entrada1.set('')
        resultado = abs(float(entrada2.get()))
        entrada2.set(resultado)
    def borrar():
        inicio = 0
        final = len(entrada2.get())

        entrada2.set(entrada2.get()[inicio:final - 1])
    def borrartodo():
        entrada1.set('')
        entrada2.set('')
    def aleatorio():
        numero1 = simpledialog.askinteger("Número 1", "Ingrese el primer número:")
        numero2 = simpledialog.askinteger("Número 2", "Ingrese el segundo número:")
        
    
        if numero1 is not None and numero2 is not None:
            
            numero_aleatorio = randint(numero1, numero2)
            
            
            ventana_resultado = tk.Toplevel(root)
            ventana_resultado.geometry('+100+200')
            ventana_resultado.minsize(width=300 ,height= 100)
            ventana_resultado.maxsize(width=300 ,height= 100)
            etiqueta_resultado = tk.Label(ventana_resultado, text=f"Número aleatorio entre {numero1} y {numero2}: {numero_aleatorio}")
            etiqueta_resultado.grid(row=2)
            etiqueta_resultado.pack()
            
    

    root1 = tk.Toplevel()

    root1.title("Calculadora")
    root1.geometry("500x500")
    root1.columnconfigure(0, weight=1)
    root1.rowconfigure(0, weight=1)

   

    root = ttk.Frame(root1, style="mainframe.TFrame")
    root.grid(column=0, row=0, sticky=(W, N, E ,S))
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)
    root.columnconfigure(2, weight=1)
    root.columnconfigure(3, weight=1)
    root.columnconfigure(4, weight=1)
    root.columnconfigure(5, weight=1)
    root.columnconfigure(6, weight=1)



    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)
    root.rowconfigure(2, weight=1)
    root.rowconfigure(3, weight=1)
    root.rowconfigure(4, weight=1)
    root.rowconfigure(5, weight=1)
    root.rowconfigure(6, weight=1)
    root.rowconfigure(7, weight=1)
    root.rowconfigure(8, weight=1)

   


    entrada1 = StringVar()
    label_entrada1 = ttk.Label(root, textvariable=entrada1, anchor= "e", font="80",foreground="#000000")
    label_entrada1.grid(row=0, column=0, columnspan=8, sticky=(W,N,E,S))

    entrada2 = StringVar()
    label_entrada2 = ttk.Label(root, textvariable=entrada2, anchor= "e", font="100",foreground="#000000")
    label_entrada2.grid(row=1, column=0, columnspan=8, sticky=(W,N,E,S))

    

    button0 = customtkinter.CTkButton(root, text="0", command=lambda: ingresarValores('0'),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    button1 = customtkinter.CTkButton(root, text="1", command=lambda: ingresarValores('1'),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    button2 = customtkinter.CTkButton(root, text="2", command=lambda: ingresarValores('2'),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    button3 = customtkinter.CTkButton(root, text="3", command=lambda: ingresarValores('3'),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    button4 = customtkinter.CTkButton(root, text="4", command=lambda: ingresarValores('4'),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    button5 = customtkinter.CTkButton(root, text="5", command=lambda: ingresarValores('5'),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    button6 = customtkinter.CTkButton(root, text="6", command=lambda: ingresarValores('6'),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    button7 = customtkinter.CTkButton(root, text="7", command=lambda: ingresarValores('7'),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    button8 = customtkinter.CTkButton(root, text="8", command=lambda: ingresarValores('8'),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    button9 = customtkinter.CTkButton(root, text="9", command=lambda: ingresarValores('9'),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    button_aleatorio = customtkinter.CTkButton(root, text='Al',command=lambda: aleatorio(),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    button_borrar = customtkinter.CTkButton(root, text=chr(9003), command=lambda: borrar(),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    button_borrar_todo = customtkinter.CTkButton(root, text="C", command=lambda:borrartodo(),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    button_parentesis1 = customtkinter.CTkButton(root, text="(", command=lambda: ingresarValores('('),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    button_parentesis2 = customtkinter.CTkButton(root, text=")", command=lambda: ingresarValores(')'),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    button_punto = customtkinter.CTkButton(root, text=".", command=lambda: ingresarValores('.'),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    button_pi = customtkinter.CTkButton(root, text='π', command=lambda: pi(),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    button_aureo = customtkinter.CTkButton(root, text= 'φ', command=lambda: numero_aureo(),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    button_division = customtkinter.CTkButton(root, text=chr(247), command=lambda: ingresarValores('/'),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    button_multiplicacion = customtkinter.CTkButton(root, text="x", command=lambda: ingresarValores('*'),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    button_resta = customtkinter.CTkButton(root, text="-", command=lambda: ingresarValores('-'),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    button_suma = customtkinter.CTkButton(root, text="+", command=lambda: ingresarValores('+'),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    button_sen = customtkinter.CTkButton(root, text= 'sen(θ)', command=lambda: sen(),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    button_igual = customtkinter.CTkButton(root, text="=", command=lambda: ingresarValores("="),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    button_raiz_cuadrada = customtkinter.CTkButton(root, text="√", command=lambda:raiz_cuadrada(),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    button_cos = customtkinter.CTkButton(root, text= 'cos(θ)', command=lambda: coss(),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    button_tan = customtkinter.CTkButton(root, text= 'tan(θ)', command=lambda: tann(),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    button_cot = customtkinter.CTkButton(root, text= 'ctan(θ)',command=lambda: cotan(),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    button_sec = customtkinter.CTkButton(root, text= 'sec(θ)', command=lambda: sec(),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    button_csc = customtkinter.CTkButton(root, text= 'csc(θ)', command=lambda: csc(),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    button_arcsen = customtkinter.CTkButton(root, text= 'arsen(θ)', command=lambda: asen(),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    button_arccos = customtkinter.CTkButton(root, text= 'arccos(θ)', command=lambda: acos(),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    button_abs = customtkinter.CTkButton(root, text= '|x|', command=lambda: absoluto(),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    button_potencia = customtkinter.CTkButton(root, text= '^' , command=lambda:ingresarValores('**'),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    button_logaritmo10 = customtkinter.CTkButton(root, text= 'Log10', command=lambda:log10n(),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    button_redon = customtkinter.CTkButton(root, text='Redon', command=lambda:redon(),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    button_mod = customtkinter.CTkButton(root, text='Mod', command=lambda: ingresarValores('Mod',fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF"),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    button_div = customtkinter.CTkButton(root, text='Div', command=lambda:ingresarValores('Div'),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    button_euler = customtkinter.CTkButton(root, text="e", command=lambda: euler(),fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")

    button_potencia.grid(column=4, row = 3, sticky=(W,N,E,S))
    button_parentesis1.grid(column=0, row=2,sticky=(W,N,E,S))
    button_parentesis2.grid(column=1, row=2,sticky=(W,N,E,S))
    button_borrar_todo.grid(column=2, row=2,sticky=(W,N,E,S))
    button_borrar.grid(column=3, row=2,sticky=(W,N,E,S))
    button_pi.grid(column=3 ,  row=7, sticky=(W,N,E,S) )
    button_aureo.grid(column=4, row= 7, sticky=(W,N,E,S))
    button7.grid(column=0, row=3,sticky=(W,N,E,S))
    button8.grid(column=1, row=3,sticky=(W,N,E,S))
    button9.grid(column=2, row=3,sticky=(W,N,E,S))
    button_division.grid(column=3, row=3,sticky=(W,N,E,S))
    button_cos.grid (column= 6, row= 2, sticky=(W,N,E,S))
    button_tan.grid  (column= 6, row= 5, sticky=(W,N,E,S))
    button_cot.grid  (column=5 , row= 3, sticky=(W,N,E,S))
    button_sec.grid (column= 6, row= 3, sticky=(W,N,E,S))
    button_csc.grid (column= 6 , row= 6, sticky=(W,N,E,S))
    button_arcsen.grid  (column= 5, row= 4, sticky=(W,N,E,S))
    button_arccos.grid  (column=6 , row= 4, sticky=(W,N,E,S))
    button_sen.grid(column=5, row=2, sticky=(W,N,E,S))
    button4.grid(column=0, row=4,sticky=(W,N,E,S))
    button5.grid(column=1, row=4,sticky=(W,N,E,S))
    button6.grid(column=2, row=4,sticky=(W,N,E,S))
    button_multiplicacion.grid(column=3, row=4,sticky=(W,N,E,S))
    button_abs.grid(column= 4, row= 4 , sticky=(W,N,E,S))
    button1.grid(column=0, row=5,sticky=(W,N,E,S))
    button1.grid(column=0, row=5,sticky=(W,N,E,S))
    button2.grid(column=1, row=5,sticky=(W,N,E,S))
    button3.grid(column=2, row=5,sticky=(W,N,E,S))
    button_suma.grid(column=3, row=5,sticky=(W,N,E,S))
    button_aleatorio.grid(column=4, row = 5, sticky=(W,N,E,S))
    button0.grid(column=0, row=6, columnspan=2,sticky=(W,N,E,S))
    button_punto.grid(column=2, row=6,sticky=(W,N,E,S))
    button_resta.grid(column=3, row=6,sticky=(W,N,E,S))
    button_logaritmo10.grid(column=4, row=6, sticky=(W,N,E,S))
    button_igual.grid(column=0, row=7, columnspan=2, sticky=(W,N,E,S))
    button_raiz_cuadrada.grid(column=4, row=2,sticky=(W,N,E,S))
    button_redon.grid(column= 5, row=5, sticky=(W,N,E,S))
    button_mod.grid(column=5, row=6, sticky=(W,N,E,S))
    button_div.grid(column=5, row=7, sticky=(W,N,E,S))
    button_euler.grid(column=2, row=7, sticky=(W,N,E,S))
    for child in root.winfo_children():
        child.grid_configure(ipady=10, padx=1, pady=1)
    
    root1.resizable(0,0)

def inte_indefinidas():
    ventana1 = tk.Toplevel()
    ventana1.title("Integrales Definidas")
    ventana1.config(bg="#FFFFFF")
    ventana1.geometry("500x500")
    frame=customtkinter.CTkFrame(master=ventana1,fg_color="#f0f0f0")
    frame.pack(pady=20, padx= 20, fill= "both", expand= True) 

    x = symbols('x')
    funcion=customtkinter.CTkEntry(frame,border_color="#f0f0f0",fg_color="#ffffff",text_color="#000000")
    funcion.pack()
    funcion.place(x=150,y=139)

    dx_c=customtkinter.CTkLabel(frame,text=f"dx ",font=("Arial",30),text_color="#000000")
    dx_c.pack()
    dx_c.place(x=300,y=139)
    
    titulo=customtkinter.CTkLabel(master=frame,text="∫", font=("Arial",60),text_color="#000000")
    titulo.pack()
    titulo.place(x=125,y=120)

    titulo1=customtkinter.CTkLabel(master=frame,text="Calcule su Integral Definida",font=("Arial",28),text_color="#000000")
    titulo1.pack()

    resultado=None

    def calcular():

        nonlocal resultado  
        if resultado:
                resultado.destroy()

        funcion1=funcion.get()

         
        try:
            integral_indefinida1 = integrate(funcion1, x)
            integral_indefinida_simplificada = simplify(integral_indefinida1)
            resultado_texto = pretty(integral_indefinida_simplificada, use_unicode=True)
            cons=customtkinter.CTkLabel(frame,text=f" + C ",text_color="#000000")
            cons.pack()
            cons.place(x=180,y=260)
            resultado = customtkinter.CTkLabel(frame, text=f"El resultado de su integral es:\n {resultado_texto}", text_color="#000000", font=("Arial", 25))
            resultado.pack()
            resultado.place(x=60, y=260)
        except Exception as e:
            resultado = customtkinter.CTkLabel(frame, text=f"Error: {str(e)}", text_color="#FF0000", font=("Arial", 25))
            resultado.pack()
            resultado.place(x=60, y=260)

    integrar = customtkinter.CTkButton(frame, text="Integrar la Funcion", command=calcular, fg_color="#a3d9f3", text_color="black", hover_color="#FFFFFF")
    integrar.pack()
    integrar.place(x=160, y=200)
    

def integrales_definidas():
    ventana1 = tk.Toplevel()
    ventana1.title("Integrales Definidas")
    ventana1.config(bg="#FFFFFF")
    ventana1.geometry("500x400")
    frame=customtkinter.CTkFrame(master=ventana1,fg_color="#f0f0f0")
    frame.pack(pady=20, padx= 20, fill= "both", expand= True)  

    lim_supe=customtkinter.CTkEntry(master=frame,width=30,height=20,border_color="#f0f0f0",fg_color="#ffffff",text_color="#000000")
    lim_supe.pack()
    lim_supe.place(x=110,y=120)

    lim_inf=customtkinter.CTkEntry(master=frame,width=30,height=20,border_color="#f0f0f0",fg_color="#ffffff",text_color="#000000")
    lim_inf.pack()
    lim_inf.place(x=110,y=170)
    
    funcion=customtkinter.CTkEntry(frame,border_color="#f0f0f0",fg_color="#ffffff",text_color="#000000")
    funcion.pack()
    funcion.place(x=140,y=139)

    dx_c=customtkinter.CTkLabel(frame,text=f"dx ",font=("Arial",30),text_color="#000000")
    dx_c.pack()
    dx_c.place(x=290,y=139)


    titulo=customtkinter.CTkLabel(master=frame,text="∫", font=("Arial",60),text_color="#000000")
    titulo.pack()
    titulo.place(x=90,y=130)

    titulo1=customtkinter.CTkLabel(master=frame,text="Calcule su Integral Definida",font=("Arial",28),text_color="#000000")
    titulo1.pack()

    x = symbols('x')

    resultado=None

    def calculado():

        nonlocal resultado  
        if resultado:
                resultado.destroy() 

        funcion1=funcion.get()
        lim_inf1=lim_inf.get()
        lim_supe1=lim_supe.get()

        lim_inf2=int(lim_inf1)
        lim_supe2=int(lim_supe1)
        
        integral_definida1 = integrate(funcion1, (x, lim_inf2, lim_supe2))

        resultado=customtkinter.CTkLabel(frame,text=f"El resultado de su integral es:\n {integral_definida1}",text_color="#000000",font=("Arial",25))
        resultado.pack()
        resultado.place(x=60,y=260)

    integrar=customtkinter.CTkButton(frame,text="Integrar la Funcion",command=calculado,fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    integrar.pack()
    integrar.place(x=160,y=200)

    

    
def integrales():
    ventana1 = tk.Toplevel()
    ventana1.title("Escoja su tipo de integral")
    ventana1.config(bg="#FFFFFF")
    ventana1.geometry("350x250")
    frame=customtkinter.CTkFrame(master=ventana1,fg_color="#f0f0f0")
    frame.pack(pady=20, padx= 20, fill= "both", expand= True)        
    etiqueta2 = tk.Label(frame, text = "Escoja su tipo de integral")
    etiqueta2.pack(padx=10, pady=5)
    boton1 = customtkinter.CTkButton(frame, text="INTEGRAL INDEFINIDA", command=inte_indefinidas,fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    boton1.pack(padx=10, pady=10)
    boton2 = customtkinter.CTkButton(frame, text="INTEGRAL DEFINIDA", command=integrales_definidas,fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    boton2.pack(padx=10, pady=10)
def derivar():
        ventana1 = tk.Tk()
        ventana1.title("Escoja su tipo de derivada")
        ventana1.config(bg="#FFFFFF")
        ventana1.geometry("350x250")
        frame=customtkinter.CTkFrame(master=ventana1,fg_color="#f0f0f0")
        frame.pack(pady=20, padx= 20, fill= "both", expand= True)        
        etiqueta2 = tk.Label(frame, text = "Escoja su tipo de integral")
        etiqueta2.pack(padx=10, pady=5)
        
        
        def deri_implicita():
            ventana_resultado = tk.Toplevel()
            ventana_resultado.title("Resultado")
            ventana_resultado.configure(bg="#FFFFFF")
            ventana_resultado.geometry("600x440")
            frame1 = customtkinter.CTkFrame(master=ventana_resultado, fg_color="#f0f0f0")
            frame1.pack(pady=20, padx=20, fill="both", expand=True)

            x, y = sp.symbols('x y')
            eqn_original = customtkinter.CTkEntry(master=frame1, bg_color="#FFFFFF")
            eqn_original.pack()
            eqn_original.place(x=80, y=80)

            eqn_label = customtkinter.CTkLabel(frame1, text="<- Ingrese la ecuación implícita", text_color="black", font=("Arial", 20))
            eqn_label.pack()
            eqn_label.place(x=275, y=80)

            titulo = customtkinter.CTkLabel(master=frame1, text="Calcula la Derivada Implícita", text_color="black", font=("Doble struck", 28))
            titulo.pack()
            titulo.place(x=105, y=10)

            etiqueta_resultado = None

            def calcular():
                nonlocal etiqueta_resultado  
                if etiqueta_resultado:
                    etiqueta_resultado.destroy()  

                eqn = eqn_original.get()

                if eqn:
                    try:
                        eq = sp.sympify(eqn)
                        derivada_implicita = sp.diff(eq, x) / sp.diff(eq, y)
                        derivada_implicita = -derivada_implicita  # Ajuste para la forma típica de dy/dx
                        etiqueta_resultado = tk.Label(ventana_resultado, text=f"La derivada implícita de la ecuación {eqn} es: \n{derivada_implicita}", fg="black", font=("Doble struck", 15))
                        etiqueta_resultado.pack(padx=20, pady=20)
                        etiqueta_resultado.place(x=20, y=200)
                    except (sp.SympifyError, ValueError) as e:
                        etiqueta_resultado = customtkinter.CTkLabel(frame1, text=f"Error: {e}", text_color="black")
                        etiqueta_resultado.pack(padx=20, pady=20)
                        etiqueta_resultado.place(x=20, y=200)
                else:
                    etiqueta_resultado = customtkinter.CTkLabel(frame1, text="Por favor, ingrese una ecuación válida.", text_color="black")
                    etiqueta_resultado.pack(padx=20, pady=20)
                    etiqueta_resultado.place(x=20, y=200)

            boton_calcular = customtkinter.CTkButton(master=frame1, text="Calcular Derivada Implícita", command=calcular, fg_color="#a3d9f3", text_color="black", hover_color="#FFFFFF")
            boton_calcular.pack(pady=10)
            boton_calcular.place(y=180, x=200)
        def deri_ordensupe():
            ventana_resultado = tk.Toplevel()
            ventana_resultado.title("Resultado")
            ventana_resultado.configure(bg="#FFFFFF")
            ventana_resultado.geometry("670x440")
            frame1 = customtkinter.CTkFrame(master=ventana_resultado, fg_color="#f0f0f0")
            frame1.pack(pady=20, padx=20, fill="both", expand=True)

            x = sp.Symbol('x')

            funcion_original = customtkinter.CTkEntry(master=frame1, bg_color="#FFFFFF")
            funcion_original.pack()
            funcion_original.place(x=80, y=80)

            numero_deri = customtkinter.CTkEntry(master=frame1, bg_color="#ffffff")
            numero_deri.pack()
            numero_deri.place(x=80, y=130)

            orden_supe = customtkinter.CTkLabel(frame1, text="<-Ingrese el orden", text_color="black", font=("Arial", 20))
            orden_supe.pack()
            orden_supe.place(x=300, y=130)

            funcion_deri = customtkinter.CTkLabel(frame1, text="<-Ingrese la funcion a derivar", text_color="black", font=("Arial", 20))
            funcion_deri.pack()
            funcion_deri.place(x=300, y=80)

            titulo = customtkinter.CTkLabel(master=frame1, text="Calcula la Derivada de Orden Superior", text_color="black", font=("Doble struck", 28))
            titulo.pack()
            titulo.place(x=55, y=10)

            etiqueta_resultado = None

            def calcular_derivada():
                nonlocal etiqueta_resultado  
                if etiqueta_resultado:
                    etiqueta_resultado.destroy()  

                funcion = funcion_original.get()
                orden_str = numero_deri.get()

                if funcion and orden_str:
                    try:
                        orden = int(orden_str)
                        derivada = sp.diff(sp.sympify(funcion), x, orden)
                        etiqueta_resultado = tk.Label(ventana_resultado, text=f"La derivada de orden {orden} de la función {funcion} es: \n{derivada}", fg="black", font=("Doble struck", 15))
                        etiqueta_resultado.pack(padx=20, pady=20)
                        etiqueta_resultado.place(x=70, y=280)
                    except (sp.SympifyError, ValueError) as e:
                        etiqueta_resultado = customtkinter.CTkLabel(frame1, text=f"Verifique la manera en la que escribio la funcion", text_color="black")
                        etiqueta_resultado.pack(padx=20, pady=20)
                        etiqueta_resultado.place(x=70, y=280)
                else:
                    etiqueta_resultado = customtkinter.CTkLabel(frame1, text="Por favor, ingresa una función y un orden válido.", text_color="black")
                    etiqueta_resultado.pack(padx=20, pady=20)
                    etiqueta_resultado.place(x=70, y=280)

            boton_calcular = customtkinter.CTkButton(master=frame1, text="Calcular Derivada", command=calcular_derivada, fg_color="#a3d9f3", text_color="black", hover_color="#FFFFFF")
            boton_calcular.pack(pady=10)
            boton_calcular.place(y=180, x=200)

        boton1 = customtkinter.CTkButton(frame, text="Derivada Implicita", command=deri_implicita,fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
        boton1.pack(padx=10, pady=10)
        boton2 = customtkinter.CTkButton(frame, text="Derivada de Orden Superior", command=deri_ordensupe,fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
        boton2.pack(padx=10, pady=10)
def sistemas_de_ecuaciones():
    
    ventana2 = tk.Toplevel()
    ventana2.title("Sistemas de ecuaciones lineales")
    ventana2.config(bg="#ffffff")
    frame=customtkinter.CTkFrame(master=ventana2,fg_color="#f0f0f0")
    frame.pack(pady=20, padx= 20, fill= "both", expand= True)
    
    ventana2.minsize(width=300, height=260)
    ventana2.maxsize(width=300, height=350)
    
    etiqueta2 = customtkinter.CTkLabel(frame, text = "𝙴𝚂𝙲𝙾𝙹𝙰 𝙻𝙰 𝙾𝙿𝙴𝚁𝙰𝙲𝙸𝙾𝙽 𝙰 𝚁𝙴𝙰𝙻𝙸𝚉𝙰𝚁", font=("Doble struck",17),text_color="black" )
    etiqueta2.pack(padx=10, pady=5)
    

    
        

    def matriz():   
    
        root = Tk()
        root.withdraw()

    
        warnings.filterwarnings("ignorar-----", message=".")

        r = int(simpledialog.askstring("Ingresar números", "Ingresar la cantidad de variables: "))
        c = int(simpledialog.askstring("Ingresar números", "Ingresar la cantidad de ecuaciones: "))

        m = []
        for i in range(c):
            l = []
            for j in range(r):
                v = float(simpledialog.askstring("Ingresar números", "Ingresar los números de la matriz: "))
                l.append(v)
            m.append(l)

        vector = []
        for i in range(c):
            v = float(simpledialog.askstring("Ingresar números", "Ingresar los resultados: "))
            vector.append(v)

        A = np.array(m)
        b = np.array(vector)
        

        try:
            x = np.linalg.solve(A, b)

          
            x_fracciones = [f"{Fraction(num).limit_denominator()}" for num in x]
            x_resultado = " ".join(x_fracciones)

        
            ventana_resultado = Tk()
            ventana_resultado.title("Resultado")
            
            etiqueta_resultado = Label(ventana_resultado, text=f"La solución del sistema de ecuaciones es:\n{x_resultado}")
            etiqueta_resultado.pack(padx=20, pady=20)
            ventana_resultado.mainloop()

        except np.linalg.LinAlgError as e:
            ventana_error = Tk()
            ventana_error.title("Error")
            
            etiqueta_error = Label(ventana_error, text="Su ecuacion no tiene solucion o tiene infinitas soluciones")
            etiqueta_error.pack(padx=20, pady=20)
            ventana_error.mainloop()
                
    def matriz_inversa():
          
       
        n = int(simpledialog.askstring("Ingresar números", "Ingrese el tamaño de la matriz (nxn): "))
        
        m = []

        for i in range(n):
            l = []
            for j in range(n):
                v = Fraction(simpledialog.askstring("Ingresar números", "Ingrese los números de la matriz (como fracción): "))
                l.append(v)
            m.append(l)

        A = np.array(m, dtype=np.float64) 

        
        if A.shape[0] != A.shape[1]:
            ventana_error = tk.Toplevel()
            ventana_error.title("Error")
           
            etiqueta_error = tk.Label(ventana_error, text="La matriz no es cuadrada, por lo que no tiene inversa.")
            etiqueta_error.pack(padx=20, pady=20)
            return

        if np.linalg.det(A) == 0:
            ventana_error = tk.Toplevel()
            ventana_error.title("Error")
            
            etiqueta_error = tk.Label(ventana_error, text="La matriz es singular y no tiene inversa.")
            etiqueta_error.pack(padx=20, pady=20)
            return

    
        matriz_inversa = np.linalg.inv(A)
        
        matriz_inversa_fraction = np.vectorize(Fraction)(matriz_inversa)

        ventana_resultado = tk.Toplevel()
        ventana_resultado.title("Resultado")
        
        etiqueta_resultado = tk.Label(ventana_resultado, text="La inversa de la matriz ingresada es:")
        etiqueta_resultado.pack(padx=20, pady=10)

        frame = tk.Frame(ventana_resultado)
        frame.pack(padx=20, pady=10)
        for i in range(n):
            for j in range(n):
                etiqueta = tk.Label(frame, text=str(matriz_inversa_fraction[i, j]))
                etiqueta.grid(row=i, column=j, padx=5, pady=5)
            
    
        
    def matriz_transpuesta():
        ventana2.destroy() 
        r = int(simpledialog.askstring("Ingresar números", "Ingresar la cantidad de variables: "))
        c = int(simpledialog.askstring("Ingresar números", "Ingresar la cantidad de ecuaciones: "))
            
        m = []
            
        for i in range(c):
            l = []
            for j in range(r):
                valor_str = simpledialog.askstring("Ingresar números", "Ingresar los números de la matriz: ")
                l.append(valor_str)
            m.append(l)
            
        A = np.array(m, dtype=object)

    
        for i in range(A.shape[0]):
            for j in range(A.shape[1]):
                A[i, j] = Fraction(A[i, j])

        
        matriz_transpuesta = np.transpose(A)

       
        matriz_transpuesta_cadenas = [[str(cell) for cell in row] for row in matriz_transpuesta]

       
        cadena_matriz_transpuesta = "\n".join([" ".join(fila) for fila in matriz_transpuesta_cadenas])

       
        matriz_cadenas = [[str(cell) for cell in row] for row in A]
        cadena_matriz = "\n".join([" ".join(fila) for fila in matriz_cadenas])

    
        ventana_resultado = tk.Toplevel()
        ventana_resultado.title("Resultado")
        
        etiqueta_resultado = tk.Label(ventana_resultado, text=f"Su matriz de tamaño {c}x{r} original es:{('\n')} {cadena_matriz} {('\n')} y su transpuesta de {r}x{c} es:{('\n')} {cadena_matriz_transpuesta}")
        etiqueta_resultado.pack(padx=20, pady=20)

    def determinante():
        r = int(simpledialog.askstring("ingresar numeros","ingresar la dimension de su matriz: "))
       
        
        
        l = []
        m = []
        
        for i in range(r):
            l = []
            for j in range(r):
                v = float(simpledialog.askstring("ingresar numeros"," ingresar los numeros de la matriz: "))
                l.append(v)
            m.append(l)
        A = np.array(m)

        matriz = np.array(A)
      
        determinante = np.linalg.det(matriz)

        ventana_resultado = tk.Toplevel()
       
        ventana_resultado.title("Resultado")
        etiqueta_resultado = tk.Label(ventana_resultado, text=f"la matriz ingresada es{"\n"} {matriz} {"\n"} y su determinante es  :{("\n")} {determinante:.2f}")
        etiqueta_resultado.pack(padx=20, pady=20)
       

        
    def operaciones_matrices():
        ventana2 = tk.Toplevel()
        ventana2.title("Sistemas de ecuaciones lineales")
        ventana2.config(bg="#ffffff")
        frame=customtkinter.CTkFrame(master=ventana2,fg_color="#f0f0f0")
        frame.pack(pady=20, padx= 20, fill= "both", expand= True)
        
        ventana2.minsize(width=300, height=260)
        ventana2.maxsize(width=300, height=350)
        
        etiqueta2 = customtkinter.CTkLabel(frame, text = "𝙴𝚂𝙲𝙾𝙹𝙰 𝙻𝙰 𝙾𝙿𝙴𝚁𝙰𝙲𝙸𝙾𝙽 𝙰 𝚁𝙴𝙰𝙻𝙸𝚉𝙰𝚁", font=("Doble struck",17),text_color="black" )
        etiqueta2.pack(padx=10, pady=5)

        def suma_matrices():
            r = int(simpledialog.askstring("Ingresar números", "Ingresar la cantidad de variables de la primera matriz: "))
            c = int(simpledialog.askstring("Ingresar números", "Ingresar la cantidad de ecuaciones de la primera matriz: "))

            m = []
            for i in range(c):
                l = []
                for j in range(r):
                    v = Fraction(simpledialog.askstring("Ingresar números", "Ingresar los números de la matriz: "))
                    l.append(v)
                m.append(l)
        
            a = int(simpledialog.askstring("Ingresar números", "Ingresar la cantidad de variables de la segunda matriz: "))
            b = int(simpledialog.askstring("Ingresar números", "Ingresar la cantidad de ecuaciones de la segunda matriz: "))

            q = []
            for i in range(b):
                s = []
                for j in range(a):
                    k = Fraction(simpledialog.askstring("Ingresar números", "Ingresar los números de la matriz: "))
                    s.append(k)
                q.append(s)

             
            suma = []
            for i in range(len(m)):
                fila_suma = []
                for j in range(len(m[0])):
                    fila_suma.append(m[i][j] + q[i][j])
                suma.append(fila_suma)
                
                texto = ""
                for fila in suma:
                    fila_texto = "   ".join(map(lambda x: str(Fraction(x).limit_denominator()), fila)) 
                    texto += f"{fila_texto}\n" 

            ventana_resultado = tk.Tk()
            ventana_resultado.title("Resultado")
            ventana_resultado.config(bg="#ffffff")
            frame=customtkinter.CTkFrame(ventana_resultado,fg_color="#f0f0f0")
            frame.pack(pady=20, padx= 20, fill= "both", expand= True)
            etiqueta_resultado = tk.Label(frame, text=f"El resultado entre su operacion entre matrices es:\n {(texto)}")
            etiqueta_resultado.pack(padx=20, pady=20)


        def resta_marices():
            r = int(simpledialog.askstring("Ingresar números", "Ingresar la cantidad de variables de la primera matriz: "))
            c = int(simpledialog.askstring("Ingresar números", "Ingresar la cantidad de ecuaciones de la primera matriz: "))

            m = []
            for i in range(c):
                l = []
                for j in range(r):
                    v = float(simpledialog.askstring("Ingresar números", "Ingresar los números de la matriz: "))
                    l.append(v)
                m.append(l)
        
            a = int(simpledialog.askstring("Ingresar números", "Ingresar la cantidad de variables de la segunda matriz: "))
            b = int(simpledialog.askstring("Ingresar números", "Ingresar la cantidad de ecuaciones de la segunda matriz: "))

            q = []
            for i in range(b):
                s = []
                for j in range(a):
                    k = Fraction(simpledialog.askstring("Ingresar números", "Ingresar los números de la matriz: "))
                    s.append(k)
                q.append(s)

             
            suma = []
            for i in range(len(m)):
                fila_suma = []
                for j in range(len(m[0])):
                    fila_suma.append(m[i][j] - q[i][j])
                suma.append(fila_suma)
                
                texto = ""
                for fila in suma:
                    fila_texto = "   ".join(map(lambda x: str(Fraction(x).limit_denominator()), fila)) 
                    texto += f"{fila_texto}\n" 

            ventana_resultado = tk.Toplevel()
            ventana_resultado.title("Resultado")
            ventana_resultado.config(bg="#ffffff")
            frame=customtkinter.CTkFrame(master=ventana_resultado,fg_color="#f0f0f0")
            frame.pack(pady=20, padx= 20, fill= "both", expand= True)
            etiqueta_resultado = tk.Label(frame, text=f"El resultado de su operacion entre matrices es:\n {(texto)}")
            etiqueta_resultado.pack(padx=20, pady=20)

        def multi_matrices():
            r = int(simpledialog.askstring("Ingresar números", "Ingresar la cantidad de variables de la primera matriz: "))
            c = int(simpledialog.askstring("Ingresar números", "Ingresar la cantidad de ecuaciones de la primera matriz: "))

            m = []
            for i in range(c):
                l = []
                for j in range(r):
                    v = Fraction(simpledialog.askstring("Ingresar números", "Ingresar los números de la matriz: "))
                    l.append(v)
                m.append(l)
        
            a = int(simpledialog.askstring("Ingresar números", "Ingresar la cantidad de variables de la segunda matriz: "))
            b = int(simpledialog.askstring("Ingresar números", "Ingresar la cantidad de ecuaciones de la segunda matriz: "))

            q = []
            for i in range(b):
                s = []
                for j in range(a):
                    k = Fraction(simpledialog.askstring("Ingresar números", "Ingresar los números de la matriz: "))
                    s.append(k)
                q.append(s)

             
            multiplicacion = []
            for i in range(len(m)):
                fila_multiplicacion = []
                for j in range(len(q[0])):
                    suma = 0
                    for k in range(len(q)):
                        suma += m[i][k] * q[k][j]
                    fila_multiplicacion.append(suma)
                multiplicacion.append(fila_multiplicacion)
            
            texto = ""
            for fila in multiplicacion:
                fila_texto = "   ".join(map(lambda x: str(Fraction(x).limit_denominator()), fila))  
                texto += f"{fila_texto}\n" 

            ventana_resultado = tk.Toplevel()
            ventana_resultado.title("Resultado")
            ventana_resultado.config(bg="#ffffff")
            frame=customtkinter.CTkFrame(master=ventana_resultado,fg_color="#f0f0f0")
            frame.pack(pady=20, padx= 20, fill= "both", expand= True)
            etiqueta_resultado = tk.Label(frame, text=f"El resultado de la operacion de la matrices es:\n {(texto)}")
            etiqueta_resultado.pack(padx=20, pady=20)

        
        def escalar_matriz():
            a = Fraction(simpledialog.askstring("Ingrese numero", "Ingrese el escalar"))
            r = int(simpledialog.askstring("Ingresar números", "Ingresar la cantidad de variables de la matriz: "))
            c = int(simpledialog.askstring("Ingresar números", "Ingresar la cantidad de ecuaciones de la matriz: "))

            q = []
            for i in range(c):
                s = []
                for j in range(r):
                    k = Fraction(simpledialog.askstring("Ingresar números", "Ingresar los números de la matriz: "))
                    s.append(k)
                q.append(s)

            resultado = []
            for fila in q:
                fila_resultado = [elemento * a for elemento in fila]
                resultado.append(fila_resultado)


                texto = ""
                for fila in resultado:
                    fila_texto = "   ".join(map(lambda x: str(Fraction(x).limit_denominator()), fila))  
                    texto += f"{fila_texto}\n"   

            ventana_resultado = tk.Toplevel()
            ventana_resultado.title("Resultado")
            ventana_resultado.config(bg="#ffffff")
            frame1=customtkinter.CTkFrame(master=ventana_resultado,fg_color="#f0f0f0")
            frame1.pack(pady=20, padx= 20, fill= "both", expand= True)
            etiqueta_resultado = tk.Label(frame1, text=f"El resultado de la operacion con matices es:\n {"\n"}{(texto)}")
            etiqueta_resultado.pack(padx=20, pady=20)

    
        boton0=customtkinter.CTkButton(master=frame,text="Suma",command=suma_matrices,fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
        boton0.pack(padx=20, pady=10)
        boton20=customtkinter.CTkButton(master=frame, text="Resta",command=resta_marices,fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
        boton20.pack(padx=20, pady=10)
        boton10=customtkinter.CTkButton(master=frame, text="Multiplicacion",command=multi_matrices,fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
        boton10.pack(padx=20, pady=10)
        boton30=customtkinter.CTkButton(master= frame, text="Por escalar",command=escalar_matriz,fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
        boton30.pack(padx=20, pady=10)
    

    
    boton1 =customtkinter.CTkButton(frame, text="sistemas de ecuaciones", command= matriz,fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    boton1.pack(padx=10, pady=10)

    boton2 =customtkinter.CTkButton(frame, text="Matriz transpuesta", command= matriz_transpuesta,fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    boton2.pack(padx=10, pady=5)
        
    boton3 =customtkinter.CTkButton(frame, text="Matriz inversa", command = matriz_inversa,fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    boton3.pack(padx=10, pady=5)

    boton3 =customtkinter.CTkButton(frame, text="determinante", command = determinante,fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    boton3.pack(padx=10, pady=5)

    boton=customtkinter.CTkButton(frame,text="Operaciones entre matrices",command=operaciones_matrices,fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    boton.pack(padx=10, pady=10)


def grafica():
    ventana1=tk.Tk()
    ventana1.title("Graficador de funciones")
    ventana1.config(bg="#ffffff")
    ventana1.geometry("500x200")
    frame=customtkinter.CTkFrame(master=ventana1,fg_color="#f0f0f0")
    frame.pack(pady=20, padx= 20, fill= "both", expand= True)
    
    def grafica3d():
        
        def plot_function_3d():
            
            function_text = function_entry.get()

           
            ax.clear()
            
        
            x_min = float(x_min_entry.get())
            x_max = float(x_max_entry.get())
            y_min = float(y_min_entry.get())
            y_max = float(y_max_entry.get())

            x = np.linspace(x_min, x_max, 1000)
            y = np.linspace(y_min, y_max, 1000)
            x, y = np.meshgrid(x, y)
            
            try:
                z = eval(function_text)
                
                ax.plot_surface(x, y, z, cmap='viridis')
                ax.set_xlabel('x')
                ax.set_ylabel('y')
                ax.set_zlabel('z')
                ax.set_title('Gráfico 3D de la función: ' + function_text)
                ax.grid(True)
                
                canvas.draw()
                
            except Exception as e:
     
                error_label.config(text="Error: " + str(e))

        def clear_plot():
         
            ax.clear()
      
            canvas.draw()

      
        root = tk.Tk()
        root.title("Graficador de funciones 3D")
        root.geometry("800x600")

        root = tk.Tk()
        root.geometry('500x500')
        root.title("prueba")


        
        function_label = customtkinter.CTkLabel(root, text="Ingrese la función:", text_color="black", font=("Arial", 16))
        function_label.pack()
        function_entry = tk.Entry(root, width=50)
        function_entry.pack()

        
        domain_frame = tk.Frame(root)
        domain_frame.pack()
        x_min_label = tk.Label(domain_frame, text="x mínimo:")
        x_min_label.grid(row=0, column=0)
        x_min_entry = tk.Entry(domain_frame)
        x_min_entry.grid(row=0, column=1)
        x_max_label = tk.Label(domain_frame, text="x máximo:")
        x_max_label.grid(row=0, column=2)
        x_max_entry = tk.Entry(domain_frame)
        x_max_entry.grid(row=0, column=3)
        
        y_min_label = tk.Label(domain_frame, text="y mínimo:")
        y_min_label.grid(row=1, column=0)
        y_min_entry = tk.Entry(domain_frame)
        y_min_entry.grid(row=1, column=1)
        y_max_label = tk.Label(domain_frame, text="y máximo:")
        y_max_label.grid(row=1, column=2)
        y_max_entry = tk.Entry(domain_frame)
        y_max_entry.grid(row=1, column=3)

        
        plot_button = customtkinter.CTkButton(root, text="Graficar", command=plot_function_3d, fg_color="#a3d9f3", text_color="black", hover_color="#FFFFFF")
        plot_button.pack(pady=5)
        clear_button = customtkinter.CTkButton(root, text="Borrar", command=clear_plot, fg_color="#a3d9f3", text_color="black", hover_color="#FFFFFF")
        clear_button.pack(pady=5)

        
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

      
        toolbar = NavigationToolbar2Tk(canvas, root)
        toolbar.update()
        canvas.get_tk_widget().pack()

        error_label = tk.Label(root, fg="red")
        error_label.pack()

        
    def graficadefuncion():
        
        def plot_function():
            
            function_text = function_entry.get()

            x_min = float(x_min_entry.get())
            x_max = float(x_max_entry.get())
            x = np.linspace(x_min, x_max, 4000000)
            try:
                y = eval(function_text)
               
                plt.plot(x, y)
                plt.xlabel('x')
                plt.ylabel('f(x)')
                plt.title('Gráfico de la función: ' + function_text)
                plt.grid(True)
                plt.axhline(0, color='black', linewidth=0.5)
                plt.axvline(0, color='black', linewidth=0.5)
                plt.xlim(x_min, x_max)
                plt.tight_layout()
             
                
                canvas.draw()
                
            except Exception as e:
               
                error_label.config(text="Error: " + str(e))

        def clear_plot():
           
            ax.clear()
            
            canvas.draw()

    
     
        root = tk.Tk()
    
        root.title("Graficador de funciones")
        
        
        
        function_label = customtkinter.CTkLabel(root, text="Ingrese la función:",text_color="black",font=("Arial",16))
        function_label.pack()
        function_entry = tk.Entry(root, width=50)
        function_entry.pack()

        
        domain_frame = tk.Frame(root)           
        domain_frame.pack()
        x_min_label = tk.Label(domain_frame, text="x mínimo:")
        x_min_label.grid(row=0, column=0)
        x_min_entry = tk.Entry(domain_frame,textvariable="1")
        x_min_entry.grid(row=0, column=1)
        x_max_label = tk.Label(domain_frame, text="x máximo:")
        x_max_label.grid(row=0, column=2) 
        x_max_entry = tk.Entry(domain_frame)
        x_max_entry.grid(row=0, column=3)

      
        plot_button = customtkinter.CTkButton(root, text="Graficar", command=plot_function,fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
        plot_button.pack(pady=5)
        clear_button = customtkinter.CTkButton(root, text="Borrar", command=clear_plot,fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
        clear_button.pack(pady=5)


       
        fig, ax = plt.subplots()
        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.draw()
        canvas.get_tk_widget().pack()


        toolbar = NavigationToolbar2Tk(canvas, root)
        toolbar.update()
        canvas.get_tk_widget().pack()

        error_label = tk.Label(root, fg="red")
        error_label.pack()
    

    label=customtkinter.CTkLabel(frame,text="Elige tu forma de grafica",text_color="black",font=("Arial",25))
    label.pack()
    boton0=customtkinter.CTkButton(frame,command=grafica3d,text="Grafica 3D",fg_color="#a3d9f3", text_color="black", hover_color="#FFFFFF")
    boton0.pack(padx=20,pady=20)
    boton10=customtkinter.CTkButton(frame,command=graficadefuncion,text="Grafica 2D",fg_color="#a3d9f3", text_color="black", hover_color="#FFFFFF")
    boton10.pack(padx=20,pady=20)
    
    
def operacion_con_complejos():
    
    ventana2 = tk.Toplevel()
    ventana2.title("Operacion con complejos")
    ventana2.minsize(width=300, height=350)
    ventana2.maxsize(width=300, height=400)
    ventana2.configure(bg= "#FFFFFF")
    frame=customtkinter.CTkFrame(master=ventana2,fg_color="#f0f0f0")
    frame.pack(pady=20, padx= 20, fill= "both", expand= True)
    etiqueta2 = customtkinter.CTkLabel(frame, text = "𝙴𝚂𝙲𝙾𝙹𝙰 𝙻𝙰 𝙾𝙿𝙴𝚁𝙰𝙲𝙸𝙾𝙽 𝙰 𝚁𝙴𝙰𝙻𝙸𝚉𝙰𝚁", font=("Doble struck",18),text_color="black")
    etiqueta2.pack(padx=10, pady=5)

    def exponencial_polar():
        r = Fraction(simpledialog.askstring("Ingresar numeros","re^(jθ)" "\n" "Ingrese r:"))  
        theta = Fraction(simpledialog.askstring("Ingresar numeros","re^(jθ)" "\n" "Ingrese θ:"))

        resultado = str(r) + "( cos" + str(theta) + " + " + "jsen" + str(theta) + ")"
        ventana_resultado = tk.Toplevel()
        ventana_resultado.title("Resultado")
        frame=customtkinter.CTkFrame(master=ventana_resultado,fg_color="#f0f0f0")
        frame.pack(pady=20, padx= 20, fill= "both", expand= True)
        etiqueta_resultado = tk.Label(frame, text=f"El resultado es: {resultado}")
        etiqueta_resultado.pack(padx=20, pady=20)
    def binomica_polar():
        a = Fraction(simpledialog.askstring("Ingresar numeros","a + bj" "\n" "Ingrese a:"))  
        b = Fraction(simpledialog.askstring("Ingresar numeros","a + bj" "\n" "Ingrese b:"))

        r = Fraction("{:.2f}".format(math.sqrt((a**2)+(b**2))))
        theta = Fraction("{:.2f}".format(math.degrees(math.atan(b/a))))

        resultado = str(r) + "( cos" + str(theta) + " + " + "jsen" + str(theta) + ")"
        ventana_resultado = tk.Toplevel()
        ventana_resultado.title("Resultado")
        frame=customtkinter.CTkFrame(master=ventana_resultado,fg_color="#f0f0f0")
        frame.pack(pady=20, padx= 20, fill= "both", expand= True)
        etiqueta_resultado = tk.Label(frame, text=f"El resultado es: {resultado}")
        etiqueta_resultado.pack(padx=20, pady=20)

    def cartesiana_polar():
        a = Fraction(simpledialog.askstring("Ingresar numeros","(a , b)" "\n" "Ingrese a:"))   
        b = Fraction(simpledialog.askstring("Ingresar numeros","(a , b)" "\n" "Ingrese b:"))
            
        r = Fraction("{:.2f}".format(math.sqrt((a**2)+(b**2))))
        theta = Fraction("{:.2f}".format(math.degrees(math.atan(b/a))))

        resultado = str(r) + "( cos" + str(theta) + " + " +"jsen" + str(theta) + ")"
        ventana_resultado = tk.Toplevel()
        ventana_resultado.title("Resultado")
        frame=customtkinter.CTkFrame(master=ventana_resultado,fg_color="#f0f0f0")
        frame.pack(pady=20, padx= 20, fill= "both", expand= True)

        etiqueta_resultado = tk.Label(frame, text=f"El resultado es: {resultado}")
        etiqueta_resultado.pack(padx=20, pady=20)
    
    def polar_exponencial():
        r = Fraction(simpledialog.askstring("Ingresar numeros","r ( cosθ + jsenθ )" "\n" "Ingrese r:"))
        theta = Fraction(simpledialog.askstring("Ingresar numeros","r ( cosθ + jsenθ )" "\n" "Ingrese θ:"))

        resultado = str(r) + "e^j" + str(theta)
        ventana_resultado = tk.Toplevel()
        ventana_resultado.title("Resultado")
        frame=customtkinter.CTkFrame(master=ventana_resultado,fg_color="#f0f0f0")
        frame.pack(pady=20, padx= 20, fill= "both", expand= True)
        
        etiqueta_resultado = tk.Label(frame, text=f"El resultado es: {resultado}")
        etiqueta_resultado.pack(padx=20, pady=20)

    def binomica_exponencial():
        a = Fraction(simpledialog.askstring("Ingresar numeros","a + bj" "\n" "Ingrese a:"))  
        b = Fraction(simpledialog.askstring("Ingresar numeros","a + bj" "\n" "Ingrese b:"))
            
        r = Fraction("{:.2f}".format(math.sqrt((a**2)+(b**2))))
        theta = Fraction("{:.2f}".format(math.degrees(math.atan(b/a))))

        resultado = str(r) + "e^j" + str(theta)
        ventana_resultado = tk.Toplevel()
        ventana_resultado.title("Resultado")
        frame=customtkinter.CTkFrame(master=ventana_resultado,fg_color="#f0f0f0")
        frame.pack(pady=20, padx= 20, fill= "both", expand= True)
       
        etiqueta_resultado = tk.Label(frame, text=f"El resultado es: {resultado}")
        etiqueta_resultado.pack(padx=20, pady=20)

    def cartesiana_exponencial():
        a = Fraction(simpledialog.askstring("Ingresar numeros","(a , b)" "\n" "Ingrese a:"))
        b = Fraction(simpledialog.askstring("Ingresar numeros","(a , b)" "\n" "Ingrese b:"))
            
        r = math.sqrt((a**2)+(b**2))
        theta = Fraction("{:.2f}".format(math.degrees(math.atan(b/a))))

        resultado = str(r) + "e^j" + str(theta)
        ventana_resultado = tk.Toplevel()
        ventana_resultado.title("Resultado")
        frame=customtkinter.CTkFrame(master=ventana_resultado,fg_color="#f0f0f0")
        frame.pack(pady=20, padx= 20, fill= "both", expand= True)
        
        etiqueta_resultado = tk.Label(frame, text=f"El resultado es: {resultado}")
        etiqueta_resultado.pack(padx=20, pady=20)

    def polar_binomica():
        r = Fraction(simpledialog.askstring("Ingresar numeros","r ( cosθ + jsenθ )" "\n" "Ingrese r:"))
        theta = Fraction(simpledialog.askstring("Ingresar numeros","r ( cosθ + jsenθ )" "\n" "Ingrese θ:"))

        a= Fraction("{:.2f}".format(r*cos(theta)))
        b= Fraction("{:.2f}".format(r*sin(theta)))

        resultado = f"{a},{b}j"
        ventana_resultado = tk.Toplevel()
        ventana_resultado.title("Resultado")
        frame=customtkinter.CTkFrame(master=ventana_resultado,fg_color="#f0f0f0")
        frame.pack(pady=20, padx= 20, fill= "both", expand= True)
        etiqueta_resultado = tk.Label(frame, text=f"El resultado es: {resultado}")
        etiqueta_resultado.pack(padx=20, pady=20)

    def exponcial_binomica():
        r = Fraction(simpledialog.askstring("Ingresar numeros","re^(jθ)" "\n" "Ingrese r:"))    
        theta = Fraction(simpledialog.askstring("Ingresar numeros","re^(jθ)" "\n" "Ingrese θ:"))

        a= Fraction("{:.2f}".format(r*cos(theta)))
        b= Fraction("{:.2f}".format(r*sin(theta)))
        
        resultado = f"{a},{b}j"
        ventana_resultado = tk.Toplevel()
        ventana_resultado.title("Resultado")
        frame=customtkinter.CTkFrame(master=ventana_resultado,fg_color="#f0f0f0")
        frame.pack(pady=20, padx= 20, fill= "both", expand= True)
        etiqueta_resultado = tk.Label(frame, text=f"El resultado es: {resultado}")
        etiqueta_resultado.pack(padx=20, pady=20)

    def cartesiana_binomica():
        a = Fraction(simpledialog.askstring("Ingresar numeros","(a , b)" "\n" "Ingrese a:"))
        b = Fraction(simpledialog.askstring("Ingresar numeros","(a , b)" "\n" "Ingrese b:"))

        resultado = f"{a},{b}j"
        ventana_resultado = tk.Toplevel()
        ventana_resultado.title("Resultado")
        frame=customtkinter.CTkFrame(master=ventana_resultado,fg_color="#f0f0f0")
        frame.pack(pady=20, padx= 20, fill= "both", expand= True)
        etiqueta_resultado = tk.Label(frame, text=f"El resultado es: {resultado}")
        etiqueta_resultado.pack(padx=20, pady=20)
         
    def polar_cartesiana():

        r = Fraction(simpledialog.askstring("Ingresar numeros","r ( cosθ + jsenθ )" "\n" "Ingrese r:"))       
        theta = Fraction(simpledialog.askstring("Ingresar numeros","r ( cosθ + jsenθ )" "\n" "Ingrese θ:"))
        a= Fraction("{:.2f}".format(r*cos(theta)))
        b= Fraction("{:.2f}".format(r*sin(theta)))
        
        resultado = f"({a},{b}j)"
        ventana_resultado = tk.Toplevel()
        ventana_resultado.title("Resultado")
        frame=customtkinter.CTkFrame(master=ventana_resultado,fg_color="#f0f0f0")
        frame.pack(pady=20, padx= 20, fill= "both", expand= True)
     
        etiqueta_resultado = tk.Label(frame, text=f"El resultado es: {resultado}")
        etiqueta_resultado.pack(padx=20, pady=20)

    def exponencial_cartesiana():
        r = Fraction(simpledialog.askstring("Ingresar numeros","re^(jθ)" "\n" "Ingrese r:"))    
        theta = Fraction(simpledialog.askstring("Ingresar numeros","re^(jθ)" "\n" "Ingrese θ:"))
        a= Fraction("{:.2f}".format(r*cos(theta)))
        b= Fraction("{:.2f}".format(r*sin(theta)))

        resultado = f"({a},{b}j)"
        ventana_resultado = tk.Toplevel()
        ventana_resultado.title("Resultado")
        frame=customtkinter.CTkFrame(master=ventana_resultado,fg_color="#f0f0f0")
        frame.pack(pady=20, padx= 20, fill= "both", expand= True)
        etiqueta_resultado = tk.Label(frame, text=f"El resultado es: {resultado}")
        etiqueta_resultado.pack(padx=20, pady=20)

    def binomica_cartesiana():
        a = Fraction(simpledialog.askstring("Ingresar numeros","a + bj" "\n" "Ingrese a:"))    
        b = Fraction(simpledialog.askstring("Ingresar numeros","a + bj" "\n" "Ingrese b:"))

        resultado = (f"({a},{b})j")
        ventana_resultado = tk.Toplevel()
        ventana_resultado.title("Resultado")
        frame=customtkinter.CTkFrame(master=ventana_resultado,fg_color="#f0f0f0")
        frame.pack(pady=20, padx= 20, fill= "both", expand= True)
      
        etiqueta_resultado = tk.Label(frame, text=f"El resultado es: {resultado}")
        etiqueta_resultado.pack(padx=20, pady=20)



    def formapolar():
        ventana1 = tk.Toplevel()
        ventana1.title("Operacion con complejos")
        ventana1.config(bg="#FFFFFF")
        frame=customtkinter.CTkFrame(master=ventana1,fg_color="#f0f0f0")
        frame.pack(pady=20, padx= 20, fill= "both", expand= True)
        etiqueta2 = tk.Label(frame, text = "Escoja la forma en la que esta representado el numero")
        etiqueta2.pack(padx=10, pady=5)
        
        
        boton2 = customtkinter.CTkButton(frame, text="Forma Exponencial", command= exponencial_polar,fg_color="#a3d9f3", text_color="black", hover_color="#FFFFFF")
        boton2.pack(padx=10, pady=5)
        
        boton3 = customtkinter.CTkButton(frame, text="Forma Binomica ", command = binomica_polar,fg_color="#a3d9f3", text_color="black", hover_color="#FFFFFF")
        boton3.pack(padx=10, pady=5)
            
        boton4 = customtkinter.CTkButton(frame, text="Forma Cartesiana", command = cartesiana_polar,fg_color="#a3d9f3", text_color="black", hover_color="#FFFFFF")
        boton4.pack(padx=10, pady=5)

    def formaexponencial():
        ventana1 = tk.Toplevel() 
        ventana1.title("Operacion con complejos")
        ventana1.config(bg="#ffffff")
        frame=customtkinter.CTkFrame(master=ventana1,fg_color="#f0f0f0")
        frame.pack(pady=20, padx= 20, fill= "both", expand= True)       
        etiqueta2 = tk.Label(frame, text = "Escoja la forma en la que esta representado el numero")
        etiqueta2.pack(padx=10, pady=5)

        boton1 = customtkinter.CTkButton(frame, text="Forma Polar", command= polar_exponencial,fg_color="#a3d9f3", text_color="black", hover_color="#FFFFFF")
        boton1.pack(padx=10, pady=10)
        boton3 = customtkinter.CTkButton(frame, text="Forma Binomica ", command = binomica_exponencial,fg_color="#a3d9f3", text_color="black", hover_color="#FFFFFF")
        boton3.pack(padx=10, pady=5)  
        boton4 = customtkinter.CTkButton(frame, text="Forma Cartesiana", command = cartesiana_exponencial,fg_color="#a3d9f3", text_color="black", hover_color="#FFFFFF")
        boton4.pack(padx=10, pady=5)

    def formabinomica(): 
        ventana1 = tk.Toplevel()
        ventana1.title("Operacion con complejos")
        ventana1.config(bg="#ffffff")
        frame=customtkinter.CTkFrame(master=ventana1,fg_color="#f0f0f0")
        frame.pack(pady=20, padx= 20, fill= "both", expand= True)
        etiqueta2 = tk.Label(frame, text = "Escoja la forma en la que esta representado el numero")
        etiqueta2.pack(padx=10, pady=5)

        boton1 = customtkinter.CTkButton(frame, text="Forma Polar", command= polar_binomica,fg_color="#a3d9f3", text_color="black", hover_color="#FFFFFF")
        boton1.pack(padx=10, pady=10)
        boton2 = customtkinter.CTkButton(frame, text="Forma Exponencial", command= exponcial_binomica,fg_color="#a3d9f3", text_color="black", hover_color="#FFFFFF")
        boton2.pack(padx=10, pady=5)
        boton4 = customtkinter.CTkButton(frame, text="Forma Cartesiana", command = cartesiana_binomica,fg_color="#a3d9f3", text_color="black", hover_color="#FFFFFF")
        boton4.pack(padx=10, pady=5)

    def cartesiana():
        ventana1 = tk.Toplevel()
        ventana1.title("Operacion con complejos")
        ventana1.config(bg="#ffffff")
        frame=customtkinter.CTkFrame(master=ventana1,fg_color="#f0f0f0")
        frame.pack(pady=20, padx= 20, fill= "both", expand= True)
        etiqueta2 = tk.Label(frame, text = "Escoja la forma en la que esta representado el numero")
        etiqueta2.pack(padx=10, pady=5)

        boton1 = customtkinter.CTkButton(frame, text="Forma Polar", command= polar_cartesiana,fg_color="#a3d9f3", text_color="black", hover_color="#FFFFFF")
        boton1.pack(padx=10, pady=10)
        boton2 = customtkinter.CTkButton(frame, text="Forma Exponencial", command= exponencial_cartesiana,fg_color="#a3d9f3", text_color="black", hover_color="#FFFFFF")
        boton2.pack(padx=10, pady=5)
        boton3 = customtkinter.CTkButton(frame, text="Forma Binomica ", command = binomica_cartesiana,fg_color="#a3d9f3", text_color="black", hover_color="#FFFFFF")
        boton3.pack(padx=10, pady=5)

    def division():
     
            a = Fraction(simpledialog.askstring("Ingrese el número", """Ingrese la parte real (a)
            Recuerde que (a + bj) / (c + dj)"""))
            b = Fraction(simpledialog.askstring("Ingrese el número", """Ingrese la parte imaginaria (b)
            Recuerde que (a + bj) / (c + dj)"""))
            c = Fraction(simpledialog.askstring("Ingrese el número", """Ingrese la parte real (c)
            Recuerde que (a + bj) / (c + dj)"""))
            d = Fraction(simpledialog.askstring("Ingrese el número", """Ingrese la parte imaginaria (d)
            Recuerde que (a + bj) / (c + dj)"""))
      
            m = a + b*1j
            n = c + d*1j
            resultado = np.divide(m, n)
          
            ventana_resultado = tk.Toplevel()
            ventana_resultado.title("Resultado")
            parte_real = Fraction(resultado.real).limit_denominator()
            parte_imaginaria = Fraction(resultado.imag).limit_denominator()
            resultado_fraccion = f"{parte_real} + {parte_imaginaria}j"
            etiqueta_resultado = tk.Label(ventana_resultado, text=f"El resultado de la división es: \n {resultado_fraccion}")
            etiqueta_resultado.pack(padx=20, pady=20)
    
    def resta(): 
        a = Fraction(simpledialog.askstring("ingrese el numero", "Introduzca la parte real(a)" "\n" "recuerde que ( a ± bj ) - ( c ± dj )"))
        b = Fraction(simpledialog.askstring("ingrese el numero", "Introduzca la parte imaginaria(b)" "\n" "recuerde que ( a ± bj ) - ( c ± dj )" ))
        c = Fraction(simpledialog.askstring("ingrese el numero", "Introduzca la parte real(c)" "\n" "recuerde que ( a ± bj ) - ( c ± dj )"))
        d = Fraction(simpledialog.askstring("ingrese el numero", "Introduzca la parte imaginaria(d)" "\n" "recuerde que ( a ± bj ) - ( c ± dj )"))
        m = a + b*1j
        n = c + d*1j
        result = np.sum(m - n)
        ventana_resultado = tk.Toplevel()
        ventana_resultado.title("Resultado")
        parte_real = Fraction(result.real).limit_denominator()
        parte_imaginaria = Fraction(result.imag).limit_denominator()
        resultado_fraccion = f"{parte_real} + {parte_imaginaria}j"
        etiqueta_resultado = tk.Label(ventana_resultado, text=f"El resultado de su resta es: {"\n"} {resultado_fraccion}")
        etiqueta_resultado.pack(padx=20, pady=20)
    def suma():
        a = Fraction(simpledialog.askstring("ingrese el numero", "Introduzca la parte real(a)" "\n" "recuerde que ( a + bj ) ± ( c + dj )"))
        b = Fraction(simpledialog.askstring("ingrese el numero", "Introduzca la parte imaginaria(b)" "\n" "recuerde que ( a + bj ) ± ( c + dj )" ))
        c = Fraction(simpledialog.askstring("ingrese el numero", "Introduzca la parte real(c)" "\n" "recuerde que ( a + bj ) ± ( c + dj )"))
        d = Fraction(simpledialog.askstring("ingrese el numero", "Introduzca la parte imaginaria(d)" "\n" "recuerde que ( a + bj ) ± ( c + dj )"))
        m = a + b*1j
        n = c + d*1j
        result = np.sum(m + n)
        ventana_resultado = tk.Toplevel()
        ventana_resultado.title("Resultado")
        parte_real = Fraction(result.real).limit_denominator()
        parte_imaginaria = Fraction(result.imag).limit_denominator()
        resultado_fraccion = f"{parte_real} + {parte_imaginaria}j"
        etiqueta_resultado = tk.Label(ventana_resultado, text=f"El resultado de su suma es: {"\n"} {resultado_fraccion}")
        etiqueta_resultado.pack(padx=20, pady=20)
    def multiplicacion():
        a = Fraction(simpledialog.askstring("ingrese el numero", "Introduzca la parte real(a)" "\n" "recuerde que ( a + bj ) x ( c + dj )"))
        b = Fraction(simpledialog.askstring("ingrese el numero", "Introduzca la parte imaginaria(b)" "\n" "recuerde que ( a + bj ) x ( c + dj )" ))
        c = Fraction(simpledialog.askstring("ingrese el numero", "Introduzca la parte real(c)" "\n" "recuerde que ( a + bj ) x ( c + dj )"))
        d = Fraction(simpledialog.askstring("ingrese el numero", "Introduzca la parte imaginaria(d)" "\n" "recuerde que ( a + bj ) x ( c + dj )"))
        m = a + b*1j
        n = c + d*1j
        result = np.multiply(m , n)
        ventana_resultado = tk.Toplevel()
        ventana_resultado.title("Resultado")
        parte_real = Fraction(result.real).limit_denominator()
        parte_imaginaria = Fraction(result.imag).limit_denominator()
        resultado_fraccion = f"{parte_real} + {parte_imaginaria}j"
        etiqueta_resultado = tk.Label(ventana_resultado, text=f"El resultado de su multiplicacion es: {"\n"} {resultado_fraccion}")
        etiqueta_resultado.pack(padx=20, pady=20)
    boton1 = customtkinter.CTkButton(frame, text="Forma Polar", command= formapolar,fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    boton1.pack(padx=1, pady=10)
    boton2 = customtkinter.CTkButton(frame, text="Forma Exponencial", command= formaexponencial,fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    boton2.pack(padx=1, pady=5)
    boton3 = customtkinter.CTkButton(frame, text="Forma Binomica ", command = formabinomica,fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    boton3.pack(padx=1, pady=5)
    boton4 =customtkinter.CTkButton(frame, text="Forma Cartesiana", command = cartesiana,fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    boton4.pack(padx=1, pady=5)
    boton6 = customtkinter.CTkButton(frame, text="Suma", command= suma,fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    boton6.pack(padx=40, pady=5)
    boton7 = customtkinter.CTkButton(frame, text="Division", command = division,fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    boton7.pack(padx=40, pady=5)
    boton7 = customtkinter.CTkButton(frame, text="Multiplicacion", command = multiplicacion,fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
    boton7.pack(padx=40, pady=5)
    boton8 = customtkinter.CTkButton(frame, text="Resta", command = resta,fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")

    boton8.pack(padx=40, pady=5)

    
ventana = Tk("Calculadora")
ventana.geometry("577x319")
ventana.configure(bg = "#FFFFFF")
frame=customtkinter.CTkFrame(master=ventana,fg_color="#f0f0f0")
frame.pack(pady=20, padx= 20, fill= "both", expand= True)
principal=customtkinter.CTkLabel(master=frame, text="𝙹³𝙼 𝙲𝙰𝙻𝙲𝚄𝙻𝙰𝚃𝙾𝚁", font=("Doble struck",34),text_color="black" )
principal.pack( pady= 12, padx= 10)
boton1=customtkinter.CTkButton(master=frame, text="Calculadora", command = calculadora, fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
boton1.pack( pady=38, padx=146,)
boton1.place(x=370, y=95,)
boton2=customtkinter.CTkButton(master=frame, text="Matrices", command= sistemas_de_ecuaciones,fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
boton2.pack( pady=38, padx=146,)
boton2.place(x=370, y=165,)
boton3=customtkinter.CTkButton(master=frame, text="Integrales", command= integrales,fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF" )
boton3.pack( pady=38, padx=146,)
boton3.place(x=370, y=200,)
boton4=customtkinter.CTkButton(master=frame, text="Derivadas", command=derivar,fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
boton4.pack( pady=38, padx=146,)
boton4.place(x=370, y=130,)
boton5=customtkinter.CTkButton(master=frame, text="Operaciones con Complejos", command= operacion_con_complejos,fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
boton5.pack( pady=38, padx=146,)
boton5.place(x=340, y=235,)
boton6=customtkinter.CTkButton(master=frame, text="Graficar", command= grafica,fg_color="#a3d9f3",text_color="black", hover_color="#FFFFFF")
boton6.pack( pady=38, padx=146,)
boton6.place(x=370, y=60,)
i = PhotoImage(file="imagen.png")
i.configure( )
l = tk.Label(frame, image=i)
l.pack()
l.place(relx=0.09, rely=0.45,relheight=.45,relwidth=.45)
ventana.resizable(0,0)
def confirmar():
                ans = askyesno(title="Salir", message= '¿Deseas salir?')
                if ans:
                    ventana.destroy()

ventana.protocol('WM_DELETE_WINDOW', confirmar)
ventana.mainloop()



