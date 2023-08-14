import os
import readchar

numero = 0

def contador():
    global suma_a
    suma_a=numero+1

while True:
    contador()
    
    k = readchar.readkey()
    if k == "n":
        numero=suma_a
    os.system('cls' if os.name=='nt' else 'clear')
    print(numero)
    if numero ==50:
        break
    