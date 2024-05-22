'''
Escribir un programa que guarde en una variable el diccionario {'Euro':, 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.

'''

divisas = {
    'euro': '€',
    'dollar': '$',
    'Yen': '¥'
}

print ('cual es tu divisa?')

divisa = input()


print (divisas.get(divisa, 'la divisa no esta'))

