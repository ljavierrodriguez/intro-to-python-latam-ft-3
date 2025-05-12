# Ciclos
""" 

for in:

for indice in coleccion:
    codigo


while:

while condicion:
    codigo

"""

nombres = ["Hugo", "Paco", "Luis"]

for i in range(1, 11): # start = 0, stop = x, step = 1
    print(i) # 1 2 3 ... 10

for i in range(0, len(nombres), 1):
    print(nombres[i])

for nombre in nombres:
    print(nombre) # Hugo Paco Luis


i = 1
while i <= 10:
    print(i)
    i+=1 # i = i + 1

i = 0
while i < len(nombres):
    print(nombres[i])
    i+=1