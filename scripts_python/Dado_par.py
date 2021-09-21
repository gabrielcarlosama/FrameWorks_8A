'''
    Description: Script en Python que permita lanzar los dados de manera indefinida Y sólo 
    finalizará cuando se genere un PAR de DADOS (1,1 - 2,2 - 3,3 - 4,4 - 5,5 - 6,6)
'''
import os
from random import randint

#Functions
def dices() :
    status = True

    while status :     #while status ==> while status == True
        os.system("clear")
        dice1 = randint(1,6)
        dice2 = randint(1,6)
        print("D1: ", dice1)
        print("D2: ", dice2)

        if dice1 == dice2 :
            status = False
            print("::: Los dados son pares. El lanzamiento ha finalizado :::")
        else :
            key = input(".:: Presiona cualquier tecla para lanzar los dados nuevamente ...")    

#Main
dices()
import random


def main():
    print("DADOS IGUALES")
    numero = int(input("Número de dados: "))
    if numero < 2:
        print("¡Imposible!")
    else:
        print("Dados: ", end="")
        repetido = False
        anterior = random.randrange(1, 7)
        print(f"{anterior} ", end="")
        for _ in range(1, numero):
            dado = random.randrange(1, 7)
            print(f"{dado} ", end="")
            if dado == anterior:
                repetido = True
            anterior = dado
        print()
        if repetido:
            print(f"El jugador ha perdido.")
        else:
            print(f"El jugador ha ganado.")


if __name__ == "__main__":
    main()
