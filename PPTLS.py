import random

print("¡Pierda, papel, tijerass, lagarto o Spock!")
contador = 3

while contador > 0:
    opcion = input("Escribe tu opción: ")
    oponente = random.randint(1,5)



    if oponente == 1:
        opcion_oponente = "piedra"
    elif oponente == 2:
        opcion_oponente = "papel"
    elif oponente == 3:
        opcion_oponente = "tijeras"
    elif oponente == 4:
        opcion_oponente = "lagarto"
    else:
        opcion_oponente = "spock"

    print(opcion,"VS",opcion_oponente)

    if opcion == opcion_oponente:
        print("Has empatado")
        
    elif opcion == "piedra":
        if opcion_oponente == "papel":
            print("Papel envuelve a piedra. Has perdido")
        elif opcion_oponente == "tijeras":
            print("Piedra rompe tijeras. Has ganado")
        elif opcion_oponente == "lagarto":
            print("Piedra aplasta lagarto. Has ganado")
        else:
            print("Spock vaporiza piedra. Has perdido")

    elif opcion == "papel":
        if opcion_oponente == "piedra":
            print("Papel envuelve a piedra. Has ganado")
        elif opcion_oponente == "tijeras":
            print("Tijeras cortan papel. Has perdido")
        elif opcion_oponente == "lagarto":
            print("Lagarto devora papel. Has perdido")
        else:
            print("Papel desautoriza Spock. Has ganado")

    elif opcion == "tijeras":
        if opcion_oponente == "piedra":
            print("Piedra rompe tijeras. Has perdido")
        elif opcion_oponente == "papel":
            print("Tijeras cortan papel. Has ganado")
        elif opcion_oponente == "lagarto":
            print("Tijeras decapitan lagarto. Has ganado")
        else:
            print("Spock rompe tijeras. Has perdido")

    elif opcion == "lagarto":
        if opcion_oponente == "piedra":
            print("Piedra aplasta lagarto. Has perdido")
        elif opcion_oponente == "papel":
            print("Lagarto devora papel. Has ganado")
        elif opcion_oponente == "tijeras":
            print("Tijeras decapitan lagarto. Has perdido")
        else:
            print("Lagarto envenena Spock. Has ganado")

    elif opcion == "spock":
        if opcion_oponente == "piedra":
            print("Spock vaporiza piedra. Has ganado")
        elif opcion_oponente == "papel":
            print("Papel desautoriza Spock. Has perdido")
        elif opcion_oponente == "tijeras":
            print("Spock rompe tijeras. Has ganado")
        else:
            print("Lagarto envenena Spock. Has perdido")
    
    contador -= 1
print("Fin del juego")