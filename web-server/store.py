import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code)
    print(r.text)
    print(type(r.text))#string
    categories = r.json()# Como el formato es de tipo texto, utilizamos esta función para convertirlo a Json
    for category in categories:
        print(category['name'])