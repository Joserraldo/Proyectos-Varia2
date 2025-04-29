import tkinter as tk

class Aplicacion:
    def  __init__(self):
        self.ventana1 = tk.Tk()
        self.ventana1.title("Ventana 1")
        self.ventana1.geometry("250x100")

        self.lblMesaje = tk.Label(self.ventana1, text =  "Soy ventana number one")
        self.lblMesaje.pack()

        self.btnIr=tk.Button(self.ventana1, text = "Ir a ventana number two",command=self.ir)
        self.btnIr.pack()

        self.ventana2 = tk.Tk()
        self.ventana2.title("Ventana number two")
        self.ventana2.geometry("250x300")

        self.lblMensaje2= tk.Label(self.ventana2, text="Soy ventana 2")
        self.lblMensaje2.pack()

        self.btnRegresar = tk.Button(self.ventana2, text = "volver a 1", command = self.volver)
        self.btnRegresar.pack()

        self.ventana2.withdraw()
        self.ventana1.mainloop()

    def ir(self):
        self.ventana1.withdraw()
        self.ventana2.deiconify()

    def volver(self):
        self.ventana2.withdraw()
        self.ventana1.deiconify()

app=Aplicacion()
