# Creado por el equipo 2
# Kimberly Melgar Sanchez, Kirill Makienko Tkachenko, Luis Arturo Reinoso Borja y Samuel Miranda Alvarez
# Para la materia de modelación de la ingenieria y ciencias

#IMPORTANTE LEER
#------------------------------------------------------------------------------------------------------------------------|
#hay un detalle con que solo de 0 a 6.28 genera la parabola y la verdad para este punto ya no quiero corregir nada       |
#en la salida del documento .csv, al angulo hay que multiplicarla por (2)*(1000)*(angulo/360) para obtener el angulo real|
#------------------------------------------------------------------------------------------------------------------------|


#importar librerias importantes
import math
import csv
import os

#condiciones iniciales

#Escoger el directorio donde se va a guardar el arcchivo .csv
#para linux es un poco diferente el path
path = r"Desktop/hoja_de_calculos.csv"
#assert os.path.isfile(path)

#"x" y "y" son las excentricidad.
x = 0.017
y = .777
semejante_mayor = 1
semejante_mayor_2 = 1.587
i=0
z=0
c=180


# esto es para escribir en un documento .cvs

header = ['Coordenadas en X de la tierra', 'Coordenadas en Y de la tierra', 'Magnitud', 'angulo','Coordenadas en X del cometa', 'Coordenadas en Y del cometa','Magnitud', 'angulo','']
with open(path, 'a', newline='\n', encoding="utf-8") as f:
    writer = csv.writer(f) 
    writer.writerow(header)

# aqui es donde se hacen las operaciones
while i < 6.28:



    r = (semejante_mayor*(1-(x**2)))/(1+x*(math.cos(i))) 
    r2 = (semejante_mayor_2*(1-(y**2)))/(1+(y)*(math.cos(i)))
    
    #Obtenemos los resultados como vector magnitud y angulo
    print("la magnitud es: ",r)
    
    print("la magnitud es: ",r2)


    #Transformamos los vectores en coordenadas cartesianas (X,Y)
    c1= (r*(math.cos(i)))
    c2= (r*(math.sin(i)))
    c3= (r2*(math.cos(i)))
    c4= (r2*(math.sin(i)))

    print("Coordenadas X de la tierra=",c1," ","Coordenadas Y de la tierra=", c2)
    print("Coordenadas X del cometa=",c3," ","Coordenadas Y del cometa=", c4)

    #Mientras seguimos en el loop esscribimos los datos en una hoja de datos .csv y le decimos al programa que depsues de escribir que se salte a la siguiente linea
    data = [[c1 , c2, r, i, c3,c4,r2,i]]   
    with open(path, 'a', newline='\n', encoding="utf-8") as f:
       writer = csv.writer(f) 
       writer.writerows(data)
    #Este es el numero de iteraciones que realiza el programa
    i=i+.01
i=0
