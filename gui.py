import tkinter as tk
#Esta librería traduce por debajo al lenguaje TCL y lo ejecuta

#Creamos una instancia de Tk
window = tk.Tk()

#Definimos la altura y anchura de la ventana
altura_ventana = 600
anchura_ventana = 800

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

window.mainloop()