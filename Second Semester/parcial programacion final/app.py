from casas import Casas
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import csv

class Aplicacion:
    def __init__(self):
        self.pagos_completados = []
        
        # Ventana principal
        self.ventana = tk.Tk()
        self.ventana.title("Pago Admon Quintas")
        self.ventana.geometry("700x800")
        self.ventana.config(bg="#f4f4f9")
        
        # Título principal
        self.lblTitulo = tk.Label(self.ventana, text="Control Pagos Administración - Quintas de Cañaveral",
                                  font=("Poppins", 18, "bold"), bg="#f4f4f9", fg="#333333")
        self.lblTitulo.pack(pady=20)
        
        # Input para número de casa
        self.numero = tk.Label(self.ventana, text="# Casa (sin espacios):", font=("Poppins", 12), bg="#f4f4f9", fg="#333333")
        self.numero.pack()
        self.textnumero = tk.Entry(self.ventana, font=("Poppins", 12), bd=2, relief="groove", width=30)
        self.textnumero.pack(pady=10)

        # Input para nombre del propietario
        self.propietario = tk.Label(self.ventana, text="Nombre del Propietario:", font=("Poppins", 12), bg="#f4f4f9", fg="#333333")
        self.propietario.pack()
        self.txtpropietario = tk.Entry(self.ventana, font=("Poppins", 12), bd=2, relief="groove", width=30)
        self.txtpropietario.pack(pady=10)

        # Input para número de pisos
        self.pisos = tk.Label(self.ventana, text="Pisos de la Casa:", font=("Poppins", 12), bg="#f4f4f9", fg="#333333")
        self.pisos.pack()
        self.txtpisos = tk.Entry(self.ventana, font=("Poppins", 12), bd=2, relief="groove", width=30)
        self.txtpisos.pack(pady=10)

        # Input para número de multas
        self.multas = tk.Label(self.ventana, text="Número de Multas (Si no tiene, digite 0):", font=("Poppins", 12), bg="#f4f4f9", fg="#333333")
        self.multas.pack()
        self.txtmultas = tk.Entry(self.ventana, font=("Poppins", 12), bd=2, relief="groove", width=30)
        self.txtmultas.pack(pady=10)

        # Botones de acción
        self.btnpago = tk.Button(self.ventana, text="Calcular Pago Admon", font=("Poppins", 12, "bold"), 
                                 command=self.calcular_admon, bg="#4CAF50", fg="white", bd=0, relief="flat", width=20)
        self.btnpago.pack(pady=20)

        self.crear_tabla()

        self.btnExportar = tk.Button(self.ventana, text="Exportar Pagos", font=("Poppins", 12, "bold"), 
                                     command=self.exportar, bg="#2196F3", fg="white", bd=0, relief="flat", width=20)
        self.btnExportar.pack(pady=10)
        
        # Ventana secundaria para confirmación del pago
        self.ventana2 = tk.Toplevel(self.ventana)
        self.ventana2.title("Confirmación del Pago (Factura)")
        self.ventana2.geometry("450x450")
        self.ventana2.config(bg="#f4f4f9")
        
        # Título en la ventana de confirmación
        self.lblTitulo2 = tk.Label(self.ventana2, text="Comprobante de Pago", font=("Poppins", 18, "bold"), bg="#f4f4f9", fg="#333333")
        self.lblTitulo2.pack(pady=20)
        
        # Resultado del cálculo de administración
        self.lblresultado = tk.Label(self.ventana2, text="Resultado", font=("Poppins", 12), bg="#f4f4f9", fg="#333333")
        self.lblresultado.pack(pady=10)

        # Pregunta de confirmación
        self.texto = tk.Label(self.ventana2, text="¿Desea continuar con el pago?", font=("Poppins", 12), bg="#f4f4f9", fg="#333333")
        self.texto.pack(pady=20)
        
        # Botones de confirmación
        self.btnsi = tk.Button(self.ventana2, text="Sí, continuar", font=("Poppins", 12, "bold"), command=self.confirmar_pago, 
                               bg="#4CAF50", fg="white", bd=0, relief="flat", width=12)
        self.btnsi.pack(side="left", padx=40)
        
        self.btnno = tk.Button(self.ventana2, text="No, volver", font=("Poppins", 12, "bold"), command=self.volver, 
                               bg="#f44336", fg="white", bd=0, relief="flat", width=12)
        self.btnno.pack(side="right", padx=40)


        self.ventana2.withdraw()
        self.ventana.mainloop()

    def calcular_admon(self):
        try:
            numero = int(self.textnumero.get())
            propietario = self.txtpropietario.get()
            pisos = int(self.txtpisos.get())
            multas = int(self.txtmultas.get())

            if numero <= 0 or numero > 84:
                messagebox.showerror("Error", "Ingrese un número de casa válido (1-84).\nRecuerde que los números se deben escribir sin espacios.")
                return
            if pisos <= 0:
                messagebox.showerror("Error", "Ingrese un número válido de pisos.\nRecuerde que los números se deben escribir sin espacios.")
                return
            if multas < 0:
                messagebox.showerror("Error", "Ingrese un número de multas válido (0 o positivo).\nRecuerde que los números se deben escribir sin espacios.")
                return
            
            operacion = Casas(numero, propietario, pisos, multas)
            pago = operacion.calcular_admon()
            self.lblresultado.config(
                font=("Courier", 12),  # Usa una fuente monoespaciada
                text=(
                    f"Factura de Administración\n"
                    f"Propietario: {propietario}\n"
                    f"Casa N°: {numero}\n"
                    "-------------------------------------------\n"
                    "DETALLE                     |    MONTO\n"
                    "-------------------------------------------\n"
                    f"Administración Base         | $300,000\n"
                    f"Incremento por Pisos ({pisos})  | ${((pisos - 1) * 50000):,}\n"
                    f"Sanciones por Multas ({multas}) | ${operacion.calcular_pago_multas():,}\n"
                    "-------------------------------------------\n"
                    f"Total a Pagar               | ${pago:,}\n"
                    "-------------------------------------------"
                )
            )
      
            self.ventana.withdraw()
            self.ventana2.deiconify()
        except ValueError:
            messagebox.showerror("Error", "Todos los campos deben contener valores numéricos válidos para el cálculo.")

    def volver(self):
        self.ventana2.withdraw()
        self.ventana.deiconify()

    def crear_tabla(self):
        """Función para crear la tabla de pagos completados."""
        # Crear contenedor para la tabla
        frame_tabla = tk.Frame(self.ventana)
        frame_tabla.pack(pady=20)

        # Crear la tabla
        self.tabla_pagos = ttk.Treeview(frame_tabla, columns=("casa", "propietario", "pisos", "multas", "monto"), show="headings")
        self.tabla_pagos.heading("casa", text="Casa")
        self.tabla_pagos.heading("propietario", text="Propietario")
        self.tabla_pagos.heading("pisos", text="Pisos")
        self.tabla_pagos.heading("multas", text="Multas")
        self.tabla_pagos.heading("monto", text="Monto ($)")

        # Configuración de tamaño para las columnas
        self.tabla_pagos.column("casa", anchor="center", width=60)
        self.tabla_pagos.column("propietario", anchor="center", width=150)
        self.tabla_pagos.column("pisos", anchor="center", width=60)
        self.tabla_pagos.column("multas", anchor="center", width=60)
        self.tabla_pagos.column("monto", anchor="center", width=100)
        
        # Agregar la tabla a la interfaz
        self.tabla_pagos.pack()

    def confirmar_pago(self):
        numero = int(self.textnumero.get())
        propietario = self.txtpropietario.get()
        pisos = int(self.txtpisos.get())
        multas = int(self.txtmultas.get())
        operacion = Casas(numero, propietario, pisos, multas)
        pago_total = operacion.calcular_admon()
        self.pagos_completados.append(operacion.presentar())
        
        # Agregar el pago a la tabla
        self.tabla_pagos.insert("", "end", values=(numero, propietario, pisos, multas,f"${pago_total:,}"))
        
        messagebox.showinfo("Pago Confirmado", "El pago ha sido registrado exitosamente.")
        self.volver()
    
    def exportar(self):
        try:
            with open('pagos.csv', 'a', newline='') as csvfile:
                fieldnames = ['Número de Casa', 'Propietario', 'Número de Pisos', 'Número de Multas', 'Pago de Multas', 'Pago de Administración']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for pago in self.pagos_completados:
                    writer.writerow(pago)
                messagebox.showinfo("Archivo Exportado", "El archivo de pagos ha sido exportado exitosamente.")
        except Exception as e:
            messagebox.showerror("Error", f"Ha ocurrido un error al exportar el archivo: {str(e)}")

app = Aplicacion()