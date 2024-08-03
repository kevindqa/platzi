def suma_range(min,max):
    suma = 0
    print(min,max)
    for i in range( min,max):
        suma += i   # suma cada elemento por cada elemento en el rango dado
    return suma


result = suma_range(2,5)

print(result)

result2= suma_range (result, result + 10)
print(result2)