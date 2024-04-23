//Recibe un array de números (de cualquier cantidad).
//Crea una variable “máxima” que inicie en 0.
//Recorre el array valor por valor.
//Pregunta si el valor de la variable máxima es mayor que el valor del número en la posición actual del array.
//Si la condición anterior es verdadera, asigna el valor de la posición actual del array a la variable máxima.
//Imprime el número más grande del array.

let numeros = [1,2,3,4];

let numeromaximo = 0

let tamaño = numeros.length

for (let i = 0; i < tamaño; i++) {

    if(numeromaximo < numeros[i]) {
        numeromaximo = numeros[i]
    }
    
}
console.log(numeromaximo);


let maximo = Math.max(1,2,3,4)

console.log(maximo)