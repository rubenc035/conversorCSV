#Importamos pandas. Para ello primero ha de estar instalado
#pip3 install pandas para python 3
#pip install pandas para pithon 2
import pandas as pd

listaFinalKardex = []

def leerDatos(archivo):

    #Leemos el archivo
    resultado = pd.read_excel(archivo)
    
    imprimirListado(archivo)
    
    #Filtramos por los elementos que estén ubicados en KARDEX
    inKardex = resultado['Ubicación'] == 'KARDEX'

    #Sacamos los valores a una lista
    valoresKardex = resultado[inKardex]

    #Convertimos esos valores a una lista para poder trabajar con ellos
    listadoKardex = valoresKardex.to_numpy().tolist()

    #Recorremos el listadoKardex y vamos comprobando que no haya repetidos en
    #listaFinalKardex, de ser así, sumamos las cantidades, si no, añadimos el elemento
    for val in listadoKardex:
        positivo = val[3]*-1
        arrayTemp = [val[0],positivo]
        listaFinalKardex.append(arrayTemp)

    return listaFinalKardex

#Función para imprimir un archivo con el nombre del archivo y los datos ordenados
#KARDEX aparecerá primero ordenado de la A a la Z y el resto ordenado por ubicación
def imprimirListado(archivo):
    pass