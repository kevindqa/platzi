# Los corchetes ([]) se utilizan para acceder a caracteres individuales dentro de una cadena


#An iterator is an object that contains a countable number of values.

text = 'Ella sabe programar en Python'

'''
print('JavaScript' in text)          #intext sirve para consultar si cierto texto esta dentro de un string
print('Python' in text)

if 'JS' in text:
  print('Elegiste bien!!')
else:
  print('Tambien elegiste bien')

'''

size = len(text)                    # len nos da el numero de caracteres que tiene un string, esto incluye los espacios
print(size)

print(text)
print(text.upper())                # la instruccion upper pasa todo a mayusculas
print(text.lower())                # lower pasa todo a minusculas
print(text.count('a'))             # count nos da el numero de veces en las que aparece un caracter o letra 

print(text.swapcase())             # swapcase pasa las mayuscula a minuscula y las minusculas a mayusculas
print(text.startswith('Ella'))     # startswith consulta si un string comimenza con una palabra
print(text.endswith('Rust'))       # endswith consulta si un string termina concierta palabra   
print(text.replace('Python', 'Go'))   #replace remplaza la plabra de un dtring por la que le demos

text_2 = 'este es un titulo'
print(text_2)
print(text_2.capitalize())        # capitalize pone la primera letra en mayuscula
print(text_2.title())             # pone la primera letra de cada palabra en mayuscula 
print(text_2.isdigit())           # isdigit consulta si el string es un numero
print("398".isdigit())