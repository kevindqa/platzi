# Dictionary Comprehension 


# structure = {clave: valor for elemento in iterable}
import random 
countries = ['col','mexico', 'bol','pe']

population ={country: random.randint(1, 100) for country in countries } 


print(population)

# another execise

names=['nico','zule', 'santi']
ages= [12,56,98]
print(list(zip(names, ages)))

diccionario ={name: age for (name, age) in zip(names,ages)}