# {diccionario}
#sobre me
lenguajes = []

principlal = input("ingresa tu principal lenguaje de programacion => ")
secundario = input("ingresa tu secundario lenguaje de programacion => ")

lenguajes.append(principlal)
lenguajes.append(secundario)

diccionario =  {
    "name": str (input("ingresa tu nombre " )),
    "apellido":  str (input("ingresa tu apellido " )),
    "edad":  int (input("ingresa tu edad " )),
    "lenguajes de programacion": lenguajes
    
}

if diccionario["edad"] >= 18:
    print ("eres mayor de edad") 
else:
    print("eres menor de edad")  


print(diccionario)
print(f"nombre = {diccionario.get("name")}") # con <get> consultamos si una llave esta en el diccionario

del diccionario["apellido"]  # con <del> eliminamos un llave del diccionario
print (diccionario)

