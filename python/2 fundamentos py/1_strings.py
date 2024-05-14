name = "kevin"
last_name = 'quiroga aponte'
print(name)
print(last_name)

full_name = name + " " + last_name
print(full_name)

quote = "I'm kevin"
print(quote)

quote2 = ' She said "Hello"  '
print(quote2)




#formas diferentes de concatenar

#operación de unir o combinar dos o más cadenas de texto 



# format
template = "Hola, mi nombre es " + name + " y mi apellido es " + last_name
print('v1 ', template)

template = "Hola, mi nombre es {} y mi apellido es {}".format(name, last_name)   # format sirve para cuando tenemos llaves este repemplazaen el orden que le demos la variables

print('v2', template)

template = f"Hola, mi nombre es {name} y mi apellido es {last_name}"  # en este caso tambien se usaformat poniendo la " f " al principio y despues en las llaves se ponenlas variables 
print('v3', template)                    