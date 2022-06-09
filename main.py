import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from gui import Gui

def main():
    #Creamos una instancia de la Gui y le pasamos el alto y ancho de la ventana
    ventana = Gui(600,800)

    #Comprobamos los archivos elegidos
    print(ventana.archivos)


if __name__ == '__main__':
    main()