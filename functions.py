# Funciones

""" 
1. Funcion de Nombre

def nombre_funcion(params...):
    codigo

2. Funciones Lambda

nombre_funcion = lambda params : retorno

"""

def saludar():
    print("Hola Mundo!")

saludar() # Hola Mundo!

sumar = lambda a, b : a + b

print(sumar(10, 10)) # 20


# 1. Parametros Posicionales

sumar(10, 20)

# 2. Parametros por Defecto

def imprimir_nombre(nombre="John Doe"):
    return f"Hola, {nombre}"

print(imprimir_nombre("Luis")) # Hola, Luis
print(imprimir_nombre()) # Hola, John Doe

# 3. Parametros Keywords

def informacion_personal(nombre = "", apellido = "", edad = ""):
    return f"Nombre: {nombre} {apellido} Edad: {edad}"

print(informacion_personal(edad=43, apellido="Doe", nombre="Jane"))

# 4. Empaquetamiento de Parametros

def totalizar(*args):
    resultado = sum(args)
    return resultado

print(totalizar(1, 2, 3, 4, 5)) # 15

# 5. Empaquetamiento de Parametros Keywords

def informacion_personal_key(**kargs):
    return f"Nombre: {kargs["nombre"]} {kargs["apellido"]} Edad: {kargs["edad"]}"

print(informacion_personal_key(edad=43, apellido="Doe", nombre="Jane"))
# Nombre: Jane Doe Edad: 43
