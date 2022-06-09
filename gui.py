import tkinter as tk
from tkinter import PhotoImage, ttk
from tkinter import filedialog
import tkinter.font as tkFont

class Gui:
    archivos = []
    altura_ventana = 0
    anchura_ventana = 0
    def __init__(self,altura_ventana,anchura_ventana):

        #Método que lee los archivos y los guarda en la variable
        def abrirArchivo():
            self.archivos = filedialog.askopenfilenames(initialdir="/", title="Seleccione archivos", filetypes = (('xlsm files','*.xlsm'), ('xls files','*.xls')))
            
        #Creamos una instancia de Tk
        window = tk.Tk()

        #Definimos la altura y anchura de la ventana
        self.altura_ventana = altura_ventana
        self.anchura_ventana = anchura_ventana

        #Cogemos el alto y ancho de la pantalla en la que estamos trabajando, le restamos la variable correspondiente
        #y lo dividimos entre 2 con // para obtener un número entero. De esta manera obtendremos la parte que 
        #ha de quedar por cada lado
        altura_pantalla = (window.winfo_screenheight() - altura_ventana) // 2
        anchura_pantalla = (window.winfo_screenwidth() - anchura_ventana) // 2

        #Pasamos primero el tamaño de la ventana y después el lugar en el que queremos colocarla
        window.geometry(f"{anchura_ventana}x{altura_ventana}")
        window.geometry(f"+{anchura_pantalla}+{altura_pantalla}")

        #Hacemos que tenga un tamaño fijo y que no se pueda agrandar ni empequeñecer
        window.resizable(width=0, height=0)

        # (0,0)    (1,0)    (2,0)
        # (0,1)    (1,1)    (2,1)
        # (0,2)    (1,2)    (2,2)
        # (0,3)    (1,3)    (2,3)
        # (0,4)    (1,4)    (2,4)
        window.columnconfigure(0, weight=1)
        window.columnconfigure(0, weight=4)

        #Creamos una etiqueta que muestra el selector de archivos
        #Creamos los fontstyles para darle estilos a la misma
        fontStyle = tkFont.Font(family="Lucida Grande", size=15)
        etqSelFile = tk.Label(window, text="Seleccionar archivos", font=fontStyle)
        etqSelFile.grid(column=0, row=1, sticky=tk.W, padx=5, pady=20)

        #Seleccionamos una imagen para poner como botón
        imgBtn = PhotoImage(file='img/fileBtn.png')
        #Creamos el botón con la imagen y ponemos borderwidth=0 para que quede redondeado
        btSel = tk.Button(window, text="", image=imgBtn, borderwidth=0, command=abrirArchivo)
        btSel.grid(column=0, row=1, sticky=tk.W, padx=200, pady=20)

        window.mainloop()

