#Importamos pandas. Para ello primero ha de estar instalado
#pip3 install pandas para python 3
#pip install pandas para pithon 2
import pandas as pd

def leerDatos(archivo):
    #Leemos el archivo
    resultado = pd.read_excel(archivo)
    
    #Filtramos por los elementos que estén ubicados en KARDEX
    inKardex = resultado['Ubicación'] == 'KARDEX'

    #Sacamos los valores a una lista
    valores = resultado[inKardex]

    #Convertimos esos valores a una lista para poder trabajar con ellos
    listado = valores.to_numpy().tolist()

    print(listado[10][2])