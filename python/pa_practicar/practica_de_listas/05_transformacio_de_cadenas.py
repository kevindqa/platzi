# Dada una lista de palabras, crea una nueva lista con las palabras en mayúsculas.

words= ["Serendipia", "petricor", "inefable", "susurros", "atardecer", "mariposa", "quimera", "aurora", "melodía", "efímero"]

wordsnew=[palabra.upper() for palabra in words]
print(wordsnew)