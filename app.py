from oop import Persona, Estudiante, sumar
import requests

try:

    p1 = Persona("Jane", "Doe")

    print(sumar(10, 10))

    response = requests.get('https://jsonplaceholder.typicode.com/users')

    data = response.json()

    for user in data:
        print(user["name"])

except Exception:
    print("Ha ocurrido un error")