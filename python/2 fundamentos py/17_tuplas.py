'''
Tuplas
Estructura de datos inmutables que contiene una secuencia ordenada de elementos
'''

numeros = (1,2,3,4,5,6,7,8,9)
strings =("pepe", "jero", "mom", "abue")

"""
-Los elementos están separados por espacios luego de las comas
-Puede contener cualquier tipo de datos
-Cada posición de la tupla tiene un índice
-Es inmutable y por lo tanto no puede ser modificada, lo que permite proteger mejor la data si no queremos que se modifique por error
"""

#para convertir la tupla a una lista ejecutamos 

numeros = list(numeros)
print(numeros)

print (type(numeros))

#normalmente convertimos las tuplas a listas para modificar los elementos que hay en ellas 

# para convertirla a tupla 

numeros = tuple(numeros)
print(numeros)

print (type(numeros))