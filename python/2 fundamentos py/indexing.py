# Los corchetes [] se utilizan para acceder a caracteres individuales dentro de una cadena
texto = "hola mundo"
#remember that the first character has the position 0
print(texto[3])  # for that reason the third position is the a 
size = len(texto[-1]) #Aquí se calcula la longitud de la cadena texto. len() es una función incorporada en Python que devuelve la longitud de un objeto, en este caso, la longitud de la cadena texto. texto[-1] accede al último carácter de la cadena, porque el índice -1 representa el último elemento de una secuencia en Python. Luego, len() devuelve el tamaño de esa cadena, que es 1.
print(texto[size])


#  SLICING

print (texto[0])
print (texto[1])
print (texto[2])
print (texto[3])
print (texto[4])

print (texto[0:3]) # aqui le estamos diciendo a Python que imprima el texto desde la posición 0 hasta una posición anterior a la 3 (o sea posición 2). por eso no imprimiria hol

# lo correcto para que nos imporima hola seria de la siguinete manera
print (texto[0:4])
print (texto[:4]) # aqui automaticamen te inicia en 0
print(texto[5:]) # aqui le damos un inicio pero si no ponemos nada despues de los : automaticamente va al final del texto
print (texto[:]) # lo mismo en este caso

print(texto[0:4])
