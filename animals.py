import requests

def cat():
    url = 'https://api.thecatapi.com/v1/images/search'
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    
    return {}

print(cat())
