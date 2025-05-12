// Funciones
/* 

1. Funcion de Nombre 

function nombreFuncion(params...){
    codigo
}

2. Funciones Anonimas

const variable = function(params...){
    codigo
}

3. Funciones Flecha

const nombreFuncion = (params...) => retorno

*/

function saludar(){
    console.log("Hola Mundo!")
}

saludar()

const sumar = (a, b) => a + b


sumar(10, 15)


function imprimirNombre(nombre="John Doe"){
    return `Hola, ${nombre}`
}

imprimirNombre("Luis") // Hola Luis
imprimirNombre() // Hola John Doe