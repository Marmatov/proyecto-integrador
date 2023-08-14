import os
import readchar

numero = 0


def terminal():
    os.system('cls' if os.name=='nt' else 'clear')
    print(numero)


while True:
    global sumaa
    sumaa = numero+1
    k = readchar.readkey()
    if k == "n":
        numero =sumaa
    if numero ==50:
        break
    terminal()
        
    