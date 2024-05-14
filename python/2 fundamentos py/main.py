# piedra papel o tijera 
# para comprender el algoritmo solo nesestito saber los casos en los que yo gano

jugador = input("piedra, papel o tijera  ").lower()
import random                             # aqui importamos el modulo random 

opciones = ("piedra","papel","tijera")   # cree la variable opciones que contiene en una tupla las opciones  que el pc puede usar 
pc = random.choice(opciones)             # aqui llamé a la funcion para que escojiera aleatoriamente una de las opciones que le habia dado anteriormente
print(f"ecojiste = {jugador} ")
print(f"tu oponente escoje {pc}")

if jugador == pc:
    print("empate")
elif jugador == "piedra":                   #piedra con papel y en en else se dedujo que el computador tenia tijera porque las otras opciones ya habian sido utilizadas
    if pc == "papel":
        print("perdiste")
        print("coputer gano")
    else:
        print("ganaste, piedra gana a tijera")
        print("user gano")
elif jugador == "tijera":                  #tijera con piedra
    if pc == "piedra":
        print("perdiste piedra gana a tijera")
    else: 
        print("ganaste tijera corta a papel")
elif jugador == "papel":
    if pc == "tijera":
        print("perdiste tijera corta a papel")    
    else:
        print("ganaste papel enbuelve a la piedra")         
else:
    print("Entrada inválida. Por favor, elige entre piedra, papel o tijera.")   
    


