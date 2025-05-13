import requests

try:
    response = requests.get('https://jsonplaceholder.typicode.com/users')

    data = response.json()

    for user in data:
        print(user["name"])

except Exception:
    print("Ha ocurrido un error")