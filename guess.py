import random

print("---ADIVINA EL NÚMERO---")

aleatorio =  random.randint(1,100)

monedas = 5

seguir = True

while seguir:
    numero = int(input("Elige un número: "))

    if aleatorio == numero:
        print("¡Has ganado!")
        seguir = False
    elif aleatorio < numero:
        print("¡Menos!")
    elif aleatorio > numero:
        print("¡Más!")
        
    if seguir:
        monedas -= 1
        if monedas == 0:
            monedas = int(input("Inserta monedas: "))
            if monedas > 5:
                print("Te sobra el partner, ¿eh?")
                print("Tienes",monedas,"monedas")
            elif monedas >= 1:
                print("Tienes",monedas,"monedas") 
                seguir = True
            elif monedas == 0:
                print("¡Has perdido!")
                seguir = False