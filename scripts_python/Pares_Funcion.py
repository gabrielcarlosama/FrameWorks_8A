'''
Developer: gabrielcarlosama
Date: 08 sep 2021
Description: Script Python que permite identificar el mayor de dos
numeros ingresados por consola a travez de una funcion 
'''

import os 

os.system("clear")

print("Ingrese primer numero:")
n1= int (input())
n2= int (input("Ingrese segundo numero:"))

if n1 > n2 :
        print("El mayor es: ", n1)
elif n1 < n2 :
    print("El mayor es: ", n2)
else :
    print("::: Los numeros son iguales :::")    

#suma = n1 + n2 
#print("La suma es: ", suma)