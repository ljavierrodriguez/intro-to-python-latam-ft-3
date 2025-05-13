# OOP

class Persona:
    nombre = ""
    apellido = ""
    edad = 0

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"
    

p1 = Persona("Jane", "Doe")
print(p1.nombre_completo())

class Estudiante(Persona):
    grado = None

    def __init__(self, nombre, apellido, grado):
        super().__init__(nombre, apellido)
        self.grado = grado

    def nombre_completo(self):
        return f"Estudiante: {self.nombre} {self.apellido}"
    

est1 = Estudiante("Jane", "Doe", "3ero")
print(est1.nombre_completo())


def sumar(a, b):
    return a + b