# piedra papel o tijera 
# para comprender el algoritmo solo nesestito saber los casos en los que yo gano
print("""
      [  Bienvenido al juego Piedra, Papel o tijera  ]
                  >>> Ingresa una opción <<<
      """)

opciones = ("piedra","papel","tijera")   # cree la variable opciones que contiene en una tupla las opciones  que el pc puede usar 

import random                             # aqui importamos el modulo random 


rounds = 1
rondasganadas_pc = 0
rondasganadas_jugador = 0

while True:

    jugador = input("piedra, papel o tijera  ").lower()
    rounds += 1
    
    print('*' *10) 

    print('ROUND', rounds)
    
    print('*' *10)
    print (rondasganadas_jugador,rondasganadas_pc)
    pc = random.choice(opciones)             # aqui llamé a la funcion para que escojiera aleatoriamente una de las opciones que le habia dado anteriormente
    print(f"ecojiste = {jugador} ")
    print(f"tu oponente escoje {pc}")

    if jugador == pc:
        print("empate")
    elif jugador == "piedra":                   #piedra con papel y en en else se dedujo que el computador tenia tijera porque las otras opciones ya habian sido utilizadas
        if pc == "papel":
            print("perdiste")
            print("coputer gano")
            rondasganadas_pc +=1
        else:
            print("ganaste, piedra gana a tijera")
            print("user gano")
            rondasganadas_jugador += 1
    elif jugador == "tijera":                  #tijera con piedra
        if pc == "piedra":
            print("perdiste piedra gana a tijera")
            rondasganadas_pc +=1
        else: 
            print("ganaste tijera corta a papel")
            rondasganadas_jugador += 1
    elif jugador == "papel":
        if pc == "tijera":
            print("perdiste tijera corta a papel")    
            rondasganadas_pc +=1
        else:
            print("ganaste papel enbuelve a la piedra")      
            rondasganadas_jugador += 1   
    else:
        print("Entrada inválida. Por favor, elige entre piedra, papel o tijera.")
    if rondasganadas_jugador == 3:
        print('ganaste')
        break
    if rondasganadas_pc == 3:
        print('perdiste')
            
            
        break
    print('')