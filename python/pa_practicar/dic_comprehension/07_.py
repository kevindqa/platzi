# Ejemplo 7: Filtrar valores menores que un umbral y transformar claves
# Crea un diccionario que contenga solo los elementos cuyo valor sea menor que 20 y convierte las claves a minúsculas.

productos = {'Manzana': 25, 'Banana': 15, 'Naranja': 8, 'Pera': 30, 'Uva': 12}

M20= {fruta.lower(): cantidad for fruta ,cantidad  in productos.items() }
print (M20)