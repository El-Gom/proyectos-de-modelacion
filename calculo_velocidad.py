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
path2 = r"Desktop/hoja_de_velocidades_tierra.csv"
path = r"Desktop/hoja_de_calculos.csv"

#condiciones iniciales, x va a valer la magnitud de la hoja de calculos, osea columna 6
M = 2000000000000000000000000000000
G = 0.00000000000667384
T=3980000000000
semejante_mayor = 1.587
e = .777
x=0
i=0

#abre path2 para Escribir el header
header = ['velocidad cometa', 'magnitud']
with open(path2, 'a', newline='\n', encoding="utf-8") as file:
            writer = csv.writer(file) 
            writer.writerow(header) 
#  abre path 1 para leer
with open(path,'r') as file:
    reader= csv.reader(file)

    for row in reader:
        #print(T2)
        #print(float(row[6]))
        x=float(row[2])
        #x=((x)*((180)/(3.14)))
        x = (x)*(15000000000000)
        print(x)
        y = 354000000000

        #vel = math.sqrt(((2)*(T))*((1+(e)*(math.cos(i))))/((1.587)*(1-(e**2)))-(1/(2)*(semejante_mayor)))
        vel2 = (((2)*(T))/(x))

        i= i+.1
        vel2=vel2*1000
        print(vel2)
        vel3 = (vel2 **.5)
        print(vel3)










        data = [[vel3, row[2], x]]
        with open(path2, 'a', newline='\n', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerows(data)

