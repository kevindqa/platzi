# crud create, read, update 

lista = [1,2,3,4,5,6,7,8,9]

print (lista[0])

lista [0]= 212
print (lista)

# <<<<<<<<<<  append  >>>>>>>>>

lista.append (10)     #A ñade un ítem al final de la lista.

print (lista)

# <<<<<<<<<<  insert  >>>>>>>>>

lista.insert(0, 0)      # Agrega un ítem a la lista en un índice específico.
print (lista)

tasks = [ "do the laundry", "cycling"]

mix_de_listas = tasks+lista        # fusionamos las listas 

print(mix_de_listas)


index_de_cycling = mix_de_listas.index("cycling")    # con la funcion index consultamos la posicion de un item de la lista

mix_de_listas [index_de_cycling]= " wash the bike"

print(mix_de_listas)

# <<<<<<<<<<  remove  >>>>>>>>>

mix_de_listas.remove(9)    #remove se utiliza para remover elementos de la lista con el nombre especifico                           
print(f"mix de listas sin el 9 = {mix_de_listas}  ")

# <<<<<<<<<<  pop  >>>>>>>>>

mix_de_listas.pop(0)        # pop se utiliza para elimiar por pocisiones elemento de la lista. si no le especificamos la posicion del elemento que queremos que elimine eliminara el ultimo elemento de la lista

print(mix_de_listas)

# <<<<<<<<<<  reverse  >>>>>>>>>

mix_de_listas.reverse()        # reverse se utiliza para poner la lista al reves

print(f"lista al reves{mix_de_listas}")

# <<<<<<<<<<  sort  >>>>>>>>>      # oraganiza los elementos de una lista

numeros1 = [4,8,3,2,9,6,45,]
print(numeros1)
numeros1.sort()

print(f" numeros en orden ede la anteior lista{numeros1} ")

strings= ["abue", "mamá", "kevin", "karen"]
print(strings)
strings.sort()
print(f"strings ordenados alfabeticamente = {strings}")