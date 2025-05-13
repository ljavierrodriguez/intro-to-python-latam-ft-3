// OOP

class Persona {
    nombre = ""
    apellido = ""
    edad = 0

    constructor(nombre, apellido){
        this.nombre = nombre
        this.apellido = apellido
    }

    asignarNombre(nombre){
        this.nombre = nombre
    }

    nombreCompleto(){
        return `${this.nombre} ${this.apellido}`
    }
}

let p1 = new Persona("John", "Doe") // constructor
p1.nombreCompleto() // John Doe
p1.nombre = "Jane"


class Estudiante extends Persona {
    grado = null

    constructor(nombre, apellido, grado){
        super(nombre, apellido)
        this.grado = grado
    }
}

let est1 = new Estudiante("John", "Doe", "1ero")
console.log(est1.nombreCompleto())