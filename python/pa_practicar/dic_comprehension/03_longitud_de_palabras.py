'''
Ejercicio 3: Longitud de palabras
Instrucciones:
Dada una lista de palabras, crea un diccionario que contenga las palabras como claves y su longitud como valores.
{clave: valor for elemento in iterable}
'''
palabras = ['manzana', 'banana', 'cereza', 'durazno', 'pera']





palabrasv2={word: len(word) for word in palabras }
print(palabrasv2)
