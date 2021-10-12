'''
Se requiere un Scrip en Python que se permita simular el juego de 
carrera numerica con dos Players.
La carrera inicia en la posicion CERO y finaliza en la posicion 100.
El juego se realiza por default con 2 jugadores
El jugador que llegue primero a la meta (posicion 100 sera el ganador)
Si un jugador generara 3 pares consecutivos en el lanzamiento de los dados 
sera directamente gandor.
Repite tiro si y solo si saca PAR.
'''

##randint => Genera valores numericos enteros[Z](+,-)
#uniform => Genera valores numericos reales[R](+,-)
import os
from random import randint, uniform

os.system("clear")

dice1 = randint(1,6)
dice2 = randint(1,6)

print("Dice1: ", dice1)
print("Dice2: ", dice2)