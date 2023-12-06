import random

print("---Adivina el numero---")

numero_aleatorio = random.randint(1,100)

numero_usuario = int(input("Digite un numero del 1 al 100:\n"))

contador = 0

while True:

    if numero_usuario < numero_aleatorio:
        print("El numero es más alto")
        numero_usuario = int(input(f"Digie un numero mayor que {numero_usuario}:\n"))
        contador += 1
    elif numero_usuario > numero_aleatorio:
        print("El numero es más bajo")
        numero_usuario = int(input(f"Digite un numero menor que {numero_usuario}:\n"))
        contador += 1
    else:
        print("Lo has adivinado")
        contador += 1
        print(f"Has necesitado {contador} intentos")
        break