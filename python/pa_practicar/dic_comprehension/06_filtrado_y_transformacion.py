# Ejemplo 3: Filtrar valores mayores que un umbral y transformar claves
# Crea un diccionario que contenga solo los elementos cuyo valor sea mayor que 50 y convierte las claves a mayúsculas.

productos = {'manzana': 45, 'banana': 55, 'naranja': 60, 'pera': 30}

ddcc = {fruit.upper(): cantidad for fruit, cantidad in productos.items( )  if cantidad  > 50  }

print(ddcc)