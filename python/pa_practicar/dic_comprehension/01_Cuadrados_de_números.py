# Crea un diccionario que contenga los números del 1 al 5 como claves y sus cuadrados como valores.
list = [1,2,3,4,5]
cuadrados = {x: x**2  for x  in list}

print( cuadrados)