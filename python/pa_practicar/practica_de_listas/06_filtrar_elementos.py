# Dada una lista de números, crea una nueva lista que contenga el cuadrado de los números pares y el cubo de los impares

lista_de_numeros= [i for i in range (1,11)]



new_list=[ numero**2 if numero %2 == 0 else numero**3 for numero in lista_de_numeros]
print(new_list)