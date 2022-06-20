#Importamos pandas. Para ello primero ha de estar instalado
#pip3 install pandas para python 3
#pip install pandas para pithon 2
import pandas as pd
import pprint
import os
import operator
from collections import OrderedDict 
from operator import getitem 
from os import remove
from subprocess import Popen
import threading 
import time

listaFinalKardex = []

def leerDatos(archivo):

    #Leemos el archivo
    resultado = pd.read_excel(archivo)
    
    imprimirListado(resultado,archivo)
    
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
def imprimirListado(resultado,archivo):
    listaKardex = {}
    listaNotKardex = {}

    caracter1 = archivo.rfind('/')+1
    caracter2 = archivo.rfind('.')
    nombreArchivo = archivo[caracter1:caracter2]

    inKardex = resultado['Ubicación'] == 'KARDEX'
    notKardex = resultado['Ubicación'] != 'KARDEX'

    datosKardex = resultado[inKardex]
    datosNotKardex = resultado[notKardex]


    listadoKardex = datosKardex.to_numpy().tolist()
    listadoNotKardex = datosNotKardex.to_numpy().tolist()

    
    #Buscamos los valores en el diccionario. Si están repetidos sumamos las cantidades
    #si no, lo añadimos al mismo

    for valor in listadoKardex:
        if valor[0] in listaKardex:
            suma = round(listaKardex[valor[0]].get('cantidad')) + round(valor[3])
            listaKardex[valor[0]] = {
                'material':valor[0],
                'texto':valor[1],
                'ubicacion':valor[2],
                'cantidad':suma,
                'und':valor[4]
            }
        else:
            listaKardex[valor[0]] = {
                'material':valor[0],
                'texto':valor[1],
                'ubicacion':valor[2],
                'cantidad':valor[3],
                'und':valor[4]
            }


    for valor2 in listadoNotKardex:
        if valor2[0] in listaNotKardex:
            suma = round(listaNotKardex[valor2[0]].get('cantidad')) + round(valor2[3])
            listaNotKardex[valor2[0]] = {
                'material':valor2[0],
                'texto':valor2[1],
                'ubicacion':valor2[2],
                'cantidad':suma,
                'und':valor2[4]
            }
        else:
            listaNotKardex[valor2[0]] = {
                'material':valor2[0],
                'texto':valor2[1],
                'ubicacion':valor2[2],
                'cantidad':valor2[3],
                'und':valor2[4]
            }

    #Ordenamos el diccionario en otro llamado diccionarioOrdenado
    diccionarioOrdenado = sorted(listaKardex.items())
    #diccionarioOrdenado2 = sorted(listaNotKardex.items())
    #Ordenamos el diccionario multidimensional
    diccionarioOrdenado2 = sorted(listaNotKardex.items(), key = lambda x: x[1]['ubicacion'])


    caracter1 = archivo.rfind('/')+1
    caracter2 = archivo.rfind('.')
    nombreArchivo = archivo[caracter1:caracter2]+".txt"
    nombreArchivo2 = archivo[caracter1:caracter2]

    #ruta = "C:\Users\Ruben\Documents\PROYECTOS PERSONALES\CONVERSOR_CSV"+ "\"+ archivo+ ".txt"
    
    #Leemos la linea del archivo donde está cargada la ruta y la combinamos con el nombre del archivo
    ficheroRuta = open('rttxt.txt', 'r')
    ruta = ficheroRuta.readline() + nombreArchivo
    #ruta = f"C:/Users/Ruben/Documents/PROYECTOS PERSONALES/CONVERSOR_CSV/{nombreArchivo}"
    fichero = open(ruta, 'w')

    fichero.write(f"Documento de material: {nombreArchivo2}")
    fichero.write('\n')
    fichero.write('\n')
    fichero.write ("{:<10} {:<45} {:<8} {:<9} {:<3}".format('Material','Texto','Ubicación','Cantidad','UND'))
    fichero.write('\n')
    contador = 0
    while contador < len(diccionarioOrdenado):
        fichero.write('\n')
        fichero.write ("{:<10} {:<45} {:<8} {:<9} {:<3}".format(
            diccionarioOrdenado[contador][1].get('material'),
            diccionarioOrdenado[contador][1].get('texto'),
            diccionarioOrdenado[contador][1].get('ubicacion'),
            diccionarioOrdenado[contador][1].get('cantidad'),
            diccionarioOrdenado[contador][1].get('und'),
        ))
        fichero.write('\n')
        fichero.write('________________________________________________________________________________')


        contador = contador + 1

    contador2 = 0
    while contador2 < len(diccionarioOrdenado2):
        fichero.write('\n')
        fichero.write ("{:<10} {:<45} {:<8} {:<9} {:<3}".format(
            diccionarioOrdenado2[contador2][1].get('material'),
            diccionarioOrdenado2[contador2][1].get('texto'),
            diccionarioOrdenado2[contador2][1].get('ubicacion'),
            diccionarioOrdenado2[contador2][1].get('cantidad'),
            diccionarioOrdenado2[contador2][1].get('und'),
        ))
        fichero.write('\n')
        fichero.write('________________________________________________________________________________')


        contador2 = contador2 + 1
    
    fichero.close()
    
    #Imprimimos el archivo por la impresora predeterminada
    os.startfile(ruta, "print")

    #Evitamos errores tales como el archivo no existe con un time.sleep
    time.sleep(5)

    #Eliminamos el archivo
    os.remove(ruta)
    #print(len(diccionarioOrdenado))
    #print(diccionarioOrdenado[0][1].get('material'))