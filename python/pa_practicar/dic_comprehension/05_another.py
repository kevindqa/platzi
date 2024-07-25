# Ejercicio 4: Filtrado de valores
# Dado un diccionario con números como claves y valores, crea un nuevo diccionario que contenga solo los elementos cuyo valor sea mayor que 5.

dicC={1:2,
      2:4,  
      3:6,
      4:8 }
print(dicC)


nm5 = {n: r for n, r in dicC.items() if r >5 }
print (nm5)