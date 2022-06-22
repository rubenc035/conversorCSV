from itertools import chain
from time import time
import tkinter as tk
from tkinter import PhotoImage, Toplevel, ttk
from tkinter import filedialog
import tkinter.font as tkFont
from tkinter import StringVar
import gestionArchivos
from tkinter import messagebox
import numpy as np
import csv
import os
import sys
import time
from os import remove

class Gui:
    listadoAgrupado = []
    listadoRetorno = []
    archivos = []
    diccionarioKardex = {}
    altura_ventana = 0
    anchura_ventana = 0
    def __init__(self,altura_ventana,anchura_ventana):
        
        #Función que crea la ventana Acerca de
        def acerca():
            ventanaAcerca = Toplevel()
            ventanaAcerca.title("Acerca de")
            #Definimos la altura y anchura de la ventana
            altura_ventana = 200
            anchura_ventana = 350

            #Cogemos el alto y ancho de la pantalla en la que estamos trabajando, le restamos la variable correspondiente
            #y lo dividimos entre 2 con // para obtener un número entero. De esta manera obtendremos la parte que 
            #ha de quedar por cada lado
            altura_pantalla = (window.winfo_screenheight() - altura_ventana) // 2
            anchura_pantalla = (window.winfo_screenwidth() - anchura_ventana) // 2

            #Pasamos primero el tamaño de la ventana y después el lugar en el que queremos colocarla
            ventanaAcerca.geometry(f"{anchura_ventana}x{altura_ventana}")
            ventanaAcerca.geometry(f"+{anchura_pantalla}+{altura_pantalla}")
            ventanaAcerca.resizable(0,0)

        #Función que crea la ventana Acerca de
        def ayuda():
            pass
        
        #función para crear una ventana de login y acceder al cambio de rutas
        def ventanaLogin():
            #Función para cerrar la ventana
            def cerrarVentana():
                ventanaLogin.destroy()

            def comprobacion():
                usuario = "rcordero"
                password = "1111"

                if inpUsuario.get() == usuario and inpPass.get() == password:
                    cerrarVentana()
                    cambioRutas()
                else:
                    messagebox.showerror("Error","Usuario o contraseña incorrectos")

            ventanaLogin = Toplevel()
            ventanaLogin.title("Login")
            #Definimos la altura y anchura de la ventana
            altura_ventana = 200
            anchura_ventana = 350

            #Cogemos el alto y ancho de la pantalla en la que estamos trabajando, le restamos la variable correspondiente
            #y lo dividimos entre 2 con // para obtener un número entero. De esta manera obtendremos la parte que 
            #ha de quedar por cada lado
            altura_pantalla = (window.winfo_screenheight() - altura_ventana) // 2
            anchura_pantalla = (window.winfo_screenwidth() - anchura_ventana) // 2

            #Pasamos primero el tamaño de la ventana y después el lugar en el que queremos colocarla
            ventanaLogin.geometry(f"{anchura_ventana}x{altura_ventana}")
            ventanaLogin.geometry(f"+{anchura_pantalla}+{altura_pantalla}")
            ventanaLogin.resizable(0,0)

            etqUsuario = tk.Label(ventanaLogin,text="Introduce el usuario")
            inpUsuario = tk.Entry(ventanaLogin,width=50)
            etqPass = tk.Label(ventanaLogin,text="Introduce el password")
            inpPass = tk.Entry(ventanaLogin,show="*",width=50)
            btnCancelar = tk.Button(ventanaLogin, text="CANCELAR", command=cerrarVentana)
            btnCambiar = tk.Button(ventanaLogin, text="ACEPTAR", command=comprobacion)

            etqUsuario.grid(column=0, row=1, sticky=tk.W, padx=20, pady=5)
            inpUsuario.grid(column=0, row=2, sticky=tk.W, padx=20, pady=5)
            etqPass.grid(column=0, row=3, sticky=tk.W, padx=20, pady=5)
            inpPass.grid(column=0, row=4, sticky=tk.W, padx=20, pady=5)
            btnCancelar.grid(column=0, row=5, sticky=tk.W, padx=100, pady=30)
            btnCambiar.grid(column=0, row=5, sticky=tk.W, padx=200, pady=30)

        #Función que crea una ventana secundaria para el cambio de rutas
        def cambioRutas():
            #Función para cerrar la ventana
            def cerrarVentana():
                ventanaRutas.destroy()
            
            #Abrimos los archivos correspondientes, cogemos la linea escrita de cada input
            #reemplazamos las barras invertidas y añadimos una al final para que no de problemas 
            #al copiar las rutas directamente desde Windows
            def cambiarRutas():
                arcTxt = open('rttxt.txt', 'w')
                arcCsv = open('wttxt.txt', 'w')
                arcXlm = open('cttxt.txt', 'w')

                lineaTxtN = inpRutaTxt.get()
                lineaCsvN = inpRutaCsv.get()
                lineaXlmN = inpRutaXlm.get()
                lineaTxt = lineaTxtN.replace('\\','/') + '/'
                lineaCsv = lineaCsvN.replace('\\','/') + '/'
                lineaXlm = lineaXlmN.replace('\\','/') + '/'
                
                arcTxt.writelines(lineaTxt)
                arcCsv.writelines(lineaCsv)
                arcXlm.writelines(lineaXlm)
                messagebox.showinfo("Final", "Las rutas se han modificado correctamente")
                cerrarVentana()

            ventanaRutas = Toplevel()
            ventanaRutas.title("Cambio de rutas principales")
            #Definimos la altura y anchura de la ventana
            altura_ventana = 300
            anchura_ventana = 600

            #Cogemos el alto y ancho de la pantalla en la que estamos trabajando, le restamos la variable correspondiente
            #y lo dividimos entre 2 con // para obtener un número entero. De esta manera obtendremos la parte que 
            #ha de quedar por cada lado
            altura_pantalla = (window.winfo_screenheight() - altura_ventana) // 2
            anchura_pantalla = (window.winfo_screenwidth() - anchura_ventana) // 2

            #Pasamos primero el tamaño de la ventana y después el lugar en el que queremos colocarla
            ventanaRutas.geometry(f"{anchura_ventana}x{altura_ventana}")
            ventanaRutas.geometry(f"+{anchura_pantalla}+{altura_pantalla}")
            ventanaRutas.resizable(0,0)
            
            aXlm = open('cttxt.txt', 'r')
            aTxt = open('rttxt.txt', 'r')
            aCsv = open('wttxt.txt', 'r')
            lXlm = aXlm.readline()
            lTxt = aTxt.readline()
            lCsv = aCsv.readline()
            
            etqRutaXlm = tk.Label(ventanaRutas,text="Carga de los archivos Excel")
            inpRutaXlm = tk.Entry(ventanaRutas,width=80)
            etqRutaTxt = tk.Label(ventanaRutas,text="Ruta de los archivos txt")
            inpRutaTxt = tk.Entry(ventanaRutas,width=80)
            etqRutaCsv = tk.Label(ventanaRutas,text="Ruta de guardado de los archivos CSV")
            inpRutaCsv = tk.Entry(ventanaRutas,width=80)
            btnCancelar = tk.Button(ventanaRutas, text="CANCELAR", command=cerrarVentana)
            btnCambiar = tk.Button(ventanaRutas, text="CAMBIAR", command=cambiarRutas)

            etqRutaXlm.grid(column=0, row=1, sticky=tk.W, padx=20, pady=5)
            inpRutaXlm.grid(column=0, row=2, sticky=tk.W, padx=20, pady=5)
            etqRutaTxt.grid(column=0, row=3, sticky=tk.W, padx=20, pady=5)
            inpRutaTxt.grid(column=0, row=4, sticky=tk.W, padx=20, pady=5)
            etqRutaCsv.grid(column=0, row=5, sticky=tk.W, padx=20, pady=5)
            inpRutaCsv.grid(column=0, row=6, sticky=tk.W, padx=20, pady=5)
            btnCancelar.grid(column=0, row=7, sticky=tk.W, padx=200, pady=30)
            btnCambiar.grid(column=0, row=7, sticky=tk.W, padx=300, pady=30)

            inpRutaXlm.insert(0,lXlm)
            inpRutaTxt.insert(0,lTxt)
            inpRutaCsv.insert(0,lCsv)

        #Función para borrar los archivos de la ruta
        def borrarArchivos():
            for archivo in self.archivos:
                remove(archivo)

        #Función que para un poco el tiempo para evitar errores, llama a borrarArchivos()
        #limpia todos los arrays para que se sumen otros involuntariamente
        #y llama a cargar lista sin ningún argumento para que esta se vacíe
        def restart():  
            time.sleep(3)
            borrarArchivos()
            self.listadoAgrupado.clear()
            self.listadoRetorno.clear()
            self.archivos = []
            self.diccionarioKardex.clear()
            cargarLista()

        #Función para guardar la lista ordenada como csv
        def guardarCsv(diccionario, archivo):

            caracter1 = archivo.rfind('/')+1
            caracter2 = archivo.rfind('.')
            nombreArchivo = archivo[caracter1:caracter2]+".csv"
            #Leemos la linea del archivo donde está cargada la ruta y la combinamos con el nombre del archivo
            ficheroRuta = open('wttxt.txt', 'r')
            ruta = ficheroRuta.readline() + nombreArchivo
            #ruta = f"C:/Users/Ruben/Documents/PROYECTOS PERSONALES/CONVERSOR_CSV/{nombreArchivo}"
            with open(ruta, 'w', newline='') as datos:
                almacenar = csv.writer(datos)
                almacenar.writerows(diccionario)

            

        #Función para llamar a la función de procesar archivos. Si la lista archivos[] está
        #vacía, lanzaremos un mensaje de aviso para que se seleccionen los achivos
        #en caso de que contenga algo, se llamará al proceso y luego se mostrará un mensaje
        # diciendo que todo se ha procesado correctamente  
        def procesarArchivos():
            if len(self.archivos) > 0:
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

                guardarCsv(diccionarioOrdenado,self.archivos[0])

                messagebox.showinfo("Final", "Todos los archivos se han procesado correctamente")

                restart()
            else:
                messagebox.showwarning("Aviso", "Para poder continuar, primero seleccione los archivos")

        #Método cargarLista() que crea un listBox con los archivos seleccionados
        def cargarLista():
            lista = tk.StringVar(value=self.archivos)
            listBox = tk.Listbox(window, background="white",height=20, width=60, border=0, listvariable=lista)

            listBox.grid(column=0, row=3, sticky=tk.W, padx=5, pady=10)

        #Método que lee los archivos y los guarda en la variable
        #Una vez que se han seleccionado los archivos, llamamos al método cargarLista()
        def abrirArchivo():
            archivo = open('cttxt.txt', 'r')
            ruta = archivo.readline()
            self.archivos = filedialog.askopenfilenames(initialdir=ruta, title="Seleccione archivos", filetypes = (('xlsm files','*.xlsm'), ('xls files','*.xls')))
            cargarLista()

        #Creamos una instancia de Tk
        window = tk.Tk()
        window.title("CONVERSOR ARCHIVOS CSV")

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
        window.columnconfigure(1, weight=1)
        window.columnconfigure(2, weight=1)
        window.columnconfigure(3, weight=1)
        window.columnconfigure(4, weight=1)

        #Creamos un botón para llamar a la ventana secundaria de cambio de rutas
        btnModificarRuta = tk.Button(window, text="Modificar rutas", borderwidth=0, command=ventanaLogin)
        btnModificarRuta.grid(column=0, row=0, sticky=tk.W,padx=5, pady=5)

        btnAcerca = tk.Button(window, text="Acerca de", borderwidth=0, command=acerca)
        btnAcerca.grid(column=0, row=0, columnspan=2, sticky=tk.W,padx=100, pady=5)

        btnAyuda = tk.Button(window, text="Ayuda", borderwidth=0, command=ayuda)
        btnAyuda.grid(column=0, row=0, columnspan=4, sticky=tk.W,padx=170, pady=5)

        #Creamos una etiqueta que muestra el selector de archivos
        #Creamos los fontstyles para darle estilos a la misma
        fuenteEtqSelFile = tkFont.Font(family="Lucida Grande", size=15)
        etqSelFile = tk.Label(window, text="Seleccionar archivos", font=fuenteEtqSelFile)
        etqSelFile.grid(column=0, row=1,columnspan=2, sticky=tk.W, padx=5, pady=20)

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
        btProcesar.grid(column=0, row=2, columnspan=2,sticky=tk.W, padx=300, pady=20)

        window.mainloop()

