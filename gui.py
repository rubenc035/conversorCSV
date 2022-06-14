import tkinter as tk
from tkinter import PhotoImage, ttk
from tkinter import filedialog
import tkinter.font as tkFont
from tkinter import StringVar
import gestionArchivos
from tkinter import messagebox
import numpy as np

class Gui:
    listadoAgrupado = []
    listadoRetorno = []
    archivos = []
    diccionarioKardex = {}
    altura_ventana = 0
    anchura_ventana = 0
    def __init__(self,altura_ventana,anchura_ventana):
        
        #Función para llamar a la función de procesar archivos. Si la lista archivos[] está
        #vacía, lanzaremos un mensaje de aviso para que se seleccionen los achivos
        #en caso de que contenga algo, se llamará al proceso y luego se mostrará un mensaje
        # diciendo que todo se ha procesado correctamente  
        def procesarArchivos():
            for archivo in self.archivos:
                retorno = gestionArchivos.leerDatos(archivo)
                self.listadoRetorno.append(retorno)

            #Primero añadimos el primer array a listadoAgrupado
            self.listadoAgrupado = self.listadoRetorno[0]
            
            longitud = 1
            #Iteramos mediante un while si la longitud es mayor que 1
            while len(self.listadoRetorno) > longitud:
                np.concatenate((self.listadoAgrupado, self.listadoRetorno[longitud]), axis=0)
                longitud = longitud + 1

            #Buscamos los valores en el diccionario. Si están repetidos sumamos las cantidades
            #si no, lo añadimos al mismo
            for valor in self.listadoAgrupado:
                if valor[0] in self.diccionarioKardex:
                    self.diccionarioKardex[valor[0]] = valor[1] + self.diccionarioKardex.get(valor[0])
                else:
                    self.diccionarioKardex[valor[0]] = valor[1]

            #Ordenamos el diccionario en otro llamado diccionarioOrdenado
            diccionarioOrdenado = sorted(self.diccionarioKardex.items())

            print("------comienza el diccionario ordenado----")
            print(diccionarioOrdenado)
            
        #Método cargarLista() que crea un listBox con los archivos seleccionados
        def cargarLista():
            lista = tk.StringVar(value=self.archivos)
            listBox = tk.Listbox(window, height=20, width=50, border=0, listvariable=lista)

            listBox.grid(column=0, row=3, sticky=tk.W, padx=5, pady=10)

        #Método que lee los archivos y los guarda en la variable
        #Una vez que se han seleccionado los archivos, llamamos al método cargarLista()
        def abrirArchivo():
            self.archivos = filedialog.askopenfilenames(initialdir="/", title="Seleccione archivos", filetypes = (('xlsm files','*.xlsm'), ('xls files','*.xls')))
            cargarLista()

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
        fuenteEtqSelFile = tkFont.Font(family="Lucida Grande", size=15)
        etqSelFile = tk.Label(window, text="Seleccionar archivos", font=fuenteEtqSelFile)
        etqSelFile.grid(column=0, row=1, sticky=tk.W, padx=5, pady=20)

        #Seleccionamos una imagen para poner como botón
        imgBtn = PhotoImage(file='img/fileBtn.png')
        #Creamos el botón con la imagen y ponemos borderwidth=0 para que quede redondeado
        btSel = tk.Button(window, text="", image=imgBtn, borderwidth=0, command=abrirArchivo)
        btSel.grid(column=0, row=1, sticky=tk.W, padx=200, pady=20)

        fuenteTextoLista = tkFont.Font(family="Lucida Grande", size=11)
        textoLista = tk.Label(window, text="Archivos seleccionados", font=fuenteTextoLista)
        textoLista.grid(column=0, row=2, sticky=tk.W, padx=5, pady=15)

        imgProceso = PhotoImage(file='img/btnProceso.png')
        btProcesar = tk.Button(window, image=imgProceso, borderwidth=0, command=procesarArchivos)
        btProcesar.grid(column=0, row=2, sticky=tk.W, padx=300, pady=20)

        window.mainloop()

