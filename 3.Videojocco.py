import random
import sys
import os

personaje = {}

def FINALBOSS ():
    print("Molyneux te da la bienvenida... MUERE")
    

def printEstado ():
    print("Vida:",personaje["vida"],"Dinero:",personaje["dinero"],"Fuerza:",personaje["fuerza"])

def lootbox (vida, fuerza):
    
    print("¡Una Lootbox salvaje apareció!")
    print("(Tiene",vida,"puntos de vida)")
    while vida > 0:
        print("")
        accion = input("¿Eliges: atacar o escapar? ")
        if accion == "atacar":
            vida = vida - personaje["fuerza"]
            if vida <= 0:
                print("¡Ganaste!")
                print("Has ganado 2 monedas")
                personaje["dinero"] += 2
            else:
                print("¡A Lootbox le quedan",vida,"puntos de vida")
                print("¡La Lootbox ataca!")
                personaje["dinero"] - fuerza
                if personaje["dinero"] <=0:
                    personaje["vida"] -= fuerza
                    if personaje["vida"] <= 0:
                        print("GAME OVER")
                        os.sys.exit
            printEstado()
        else:
            print("Escapaste")
            return

def crearLootbox ():
    loot = random.randint(1,5)
    if loot % 2 == 0:
        loot_vida = random.randint(1,20)
        loot_fuerza = random.randint(1,4)
        lootbox(loot_vida,loot_fuerza)
  
cofre4 = True  
def room4 ():
    print("ROOM4")
    crearLootbox()
    print("Hay un cofre y una puerta al norte que pone: ")
    print("Molineux")
    opcion = input("¿Abir el cofre, ir al norte o volver al sur? ")
    if opcion == "abrir" and cofre4:
        monedas = random.randint(2,6)
        print("Abres el cofre y consigues...",monedas,"monedas")
        personaje["dinero"] += monedas
        print("Ahora tienes",personaje["dinero"],"monedas")
        cofre4 = False
        opcion = input("¿Vas al norte o sur? ")
        if opcion == "norte":
            FINALBOSS()
        else:
            room2()
    elif opcion == "norte":
        FINALBOSS()
    else:
        room2()

def room3 ():
    print("ROOM3")
    print("Esta habitación está vacía.")
    direccion = input("¿Vuelves al oeste? ")
    if direccion == "si":
        room1()

def room2 ():
    print("ROOM2")
    crearLootbox()
    direccion = input("¿Vas al norte o al este? ")
    if direccion == "norte":
        room4()
    elif direccion == "este":
        room1()

    
def room1 ():
    #ESTE OESTE
    print("En la habitación no hay nada más que dos puertas:")
    print("Una da al Este y otra al Oeste")
    direccion = input("¿Este, Oeste o Sur? ")
    if direccion == "este":
        room2()
    elif direccion == "oeste":
        room3()
    else:
        entrada()



def entrada ():
    print("")
    print("Has entrado")
    print("Ves al norte una puerta")
    print("Al sur vuelves a la entrada")
    direccion = input("¿Vas al norte o sur? ")
    if direccion == "norte":
        room1()
    else:
        print("Cobarde gallina capitán de las sardinas")



os.system("cls")
print("The Quest for Directasa, The Videojocco")
print("=======================================")
print("")
print("La Directasa ha sido robada por un mago y la ha escondido en el fondo de una mazmorra.")
print("Antes de nada....")
print("¿Cómo te llamas? ")
opcion = input("¿pazos, caliebre o enoc? ")
if opcion == "pazos":
    personaje["nombre"] = "Pazos64"
    personaje["vida"] = 5
    personaje["dinero"] = 10
    personaje["fuerza"] = 10
elif opcion == "caliebre":
    personaje["nombre"] = "Caliebre"
    personaje["vida"] = 5
    personaje["dinero"] = 15
    personaje["fuerza"] = 5
elif opcion == "enoc":
    personaje["nombre"] = "Enoc"
    personaje["vida"] = 5
    personaje["dinero"] = 5
    personaje["fuerza"] = 15
else:
    print("Elige entre pazos, caliebre o enoc")
print("¿Quieres entrar en la mazmorra,",personaje["nombre"],"?")

respuesta = input("Escribe: si/no ")

if respuesta == "si":
    entrada()
else:
    print("Cobarde gallina capitán de las sardinas")
    

#personaje = {"Nombre":"Pazos", "Vidas":5, "Fuerza":10, "Dinero":1}
#print(personaje["Nombre","Vidas"])
