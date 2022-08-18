# Creado por el equipo 2
# Kimberly Melgar Sanchez, Kirill Makienko Tkachenko, Luis Arturo Reinoso Borja y Samuel Miranda Alvarez
# Para la materia de modelación de la ingenieria y algo más



#importar librerias importantes, aun que varias no sirven
import math
import csv
import matplotlib.pyplot as plt
import pandas as pd
import os


# Esto no sirve
colision=bool


#condiciones iniciales

#Escoger el directorio donde se va a guardar el arcchivo .csv
path = r"C:\Users\elchi\Desktop\proyecto de modelacion/hoja_de_calculo_rotacion_parabolas.csv"
#assert os.path.isfile(path)
x = 0.017
y = .777
semejante_mayor = 1
semejante_mayor_2 = 2.82
i=0
z=0
c=180


# esto es para escribir en un documento .cvs

header = ['Coordenadas en X de la tierra', 'Coordenadas en Y de la tierra', 'Magnitud', 'angulo','Coordenadas en X del cometa', 'Coordenadas en Y del cometa','Magnitud', 'angulo','']
with open(path, 'a', newline='\n', encoding="utf-8") as f:
    writer = csv.writer(f) 
    writer.writerow(header)


# aqui es donde se hacen las operaciones
while i < 180:
    # Ponemos mientras nuestro iterador que mientras sea menor a 180 (porque tomamos nuestro iterador como los grados) y ocupamos las formulas de Kepler para simular una orbita
    r = (semejante_mayor*(1-(x**2)))/(1+x*(math.cos(i))) 
    r2 = (semejante_mayor_2*(1-(y**2)))/(1+y*(math.cos(i)))

    #Obtenemos los resultados como vector magnitud y angulo
    print("la magnitud es: ",r)
    print("el angulo es: ", i)

    #Transformamos los vectores en coordenadas cartesianas (X,Y)
    c1= (r*(math.cos(i)))
    c2= (r*(math.cos(180-i)))
    c3= (r2*(math.cos(i)))
    c4= (r2*(math.cos(180-i)))

    print("Coordenadas X de la tierra=",c1," ","Coordenadas Y de la tierra=", c2)
    print("Coordenadas X de la tierra=",c3," ","Coordenadas Y de la tierra=", c4)
    print("la magnitud es: ",r2)
    print("el angulo es: ", i)


    #Checar si las magnitudes coincide, y como los anguloss son los mismos esto nos va a decir si estos puntos coinciden y por lo tanto si los 2 objetos chocan 
    coord1=round(c1,2)
    coord2=round(c3,2)
    coord3=round(c2,2)
    coord4=round(c4,2)
    if coord1 == coord2 and coord3 == coord4:
       
        colision = True

    #Mientras seguimos en el loop esscribimos los datos en una hoja de datos .csv y le decimos al programa que depsues de escribir que se salte a la siguiente linea
    data = [[c1 , c2, r, i, c3,c4,r,i]]   
    with open(path, 'a', newline='\n', encoding="utf-8") as f:
       writer = csv.writer(f) 
       writer.writerows(data)
    #Este es el numero de iteraciones (O cuantos grados cambiamos) cada que realiza la operacion
    i=i+.001
i=0


if colision == True:
    print('los planetas se van a chocar en: ', coord1,' ', coord2)
else:
     print('no ps no')


