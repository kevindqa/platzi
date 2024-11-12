# piedra papel o tijera 
# para comprender el algoritmo solo nesestito saber los casos en los que yo gano
print("""
      [  Bienvenido al juego Piedra, Papel o tijera  ]
                  >>> Ingresa una opción <<<
      """)



import random                             # aqui importamos el modulo random 

        # '''variables''' 
opciones = ("piedra","papel","tijera")   # cree la variable opciones que contiene en una tupla las opciones  que el pc puede usar 
rounds = 1
rondasganadas_pc = 0
rondasganadas_jugador = 0
games_wins_by_pc = 0
games_wins_by_jugador=0



while True:
    print('*' *10) 
    print('ROUND', rounds)
    print('*' *10)

    jugador = input("piedra, papel o tijera  ").lower()
    
    rounds += 1
    if not jugador in opciones:
        print ('no es una option')
        continue
 

    


    print (f' player => {rondasganadas_jugador} pc => {rondasganadas_pc}')
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
            print("perdiste, piedra gana a tijera")
            rondasganadas_pc +=1
        else: 
            print("ganaste, tijera corta a papel")
            rondasganadas_jugador += 1
    elif jugador == "papel":
        if pc == "tijera":
            print("perdiste, tijera corta a papel")    
            rondasganadas_pc +=1
        else:
            print("ganaste, papel enbuelve a la piedra")      
            rondasganadas_jugador += 1   
    else:
        print("Entrada inválida. Por favor, elige entre piedra, papel o tijera.")
    if rondasganadas_jugador == 3:
        print('      ganaste  😎   ')
        print (f' player => {rondasganadas_jugador} pc => {rondasganadas_pc}')
        rondasganadas_jugador= 0
        rondasganadas_pc = 0
        rounds = 1
        games_wins_by_jugador += 1
        print (f'haz ganado {games_wins_by_jugador} ')
        
    elif rondasganadas_pc == 3:
        print('      PERDISTE 🥱   ') 
        print (f' player => {rondasganadas_jugador} pc => {rondasganadas_pc}')
        rondasganadas_jugador= 0
        rondasganadas_pc = 0
        rounds = 1
        games_wins_by_pc += 1
        print (f'haz ganado {games_wins_by_pc} ')
    


