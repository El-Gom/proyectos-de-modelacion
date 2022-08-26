# Creado por el equipo 2
# Kimberly Melgar Sanchez, Kirill Makienko Tkachenko, Luis Arturo Reinoso Borja y Samuel Miranda Alvarez
# Para la materia de modelación de la ingenieria y ciencias

#IMPORTANTE LEER
#------------------------------------------------------------------------------------------------------------------------------------------|
#Tienes que tener el archivo ocn los calculos de las coordenadas y haberle eliminado la 1ra fila de texto para que te deje usar el programa|
#ESTE PROGRAMA SOLO ESCUPE EL 1er VALOR CORRECTO, LOS DEMAS VALORES SE NECESITAN SACAR MEDIANTE R1V1=R2V2, SOLO ES VALIDA LA VEL PARA EL PERIHELIO|
#------------------------------------------------------------------------------------------------------------------------------------------|



#importar librerias importantes
import math
import csv
#import matplotlib.pyplot as plt
#import pandas as pd
import os



#las 2 locaciones de los archivos, el programa va a leer path y va a escribir path2
path2 = r"Desktop/hoja_de_velocidades_completa_t.csv"
path = r"Desktop/hoja_de_velocidades_tierra.csv"


V=23.23456
R1 = 0.983
V1R1=22.83957248
V1R12=29.99

with open(path,'r') as file:
    reader= csv.reader(file)

    for row in reader:

        print(row[1])
        V2 = ((V1R1)/float(row[1]))
        V3 = ((V1R12)/float(row[1]))
        print(V2)
        V2 = float(V2)
        V3 = float(V3)


        data = [V2, row[1], V3]
        with open(path2, 'a', newline='\n', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(data)
            