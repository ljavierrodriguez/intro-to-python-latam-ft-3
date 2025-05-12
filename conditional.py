# Condicionales
"""

if condicion:
    codigo

if condicion:
    codigo
else:
    codigo

if condicion:
    codigo
elif condicion:
    codigo
else:
    codigo

"""

a = 6
b = 8
c = 10

if a > b:
    print("Verdadero")


if a > b:
    print("Verdadero")
else:
    print("Falso")

if a > b:
    print("A")
elif b > c:
    print("B")
else:
    print("Otro")


# Operadores Logicos (and, or, not)
""" 
and or not
"""

if a > b and a > c:
    print("A")
elif b > c:
    print("B")
else:
    print("C")

if not a > b:
    print("B")

activo = True

if not activo:
    print("Inactivo")