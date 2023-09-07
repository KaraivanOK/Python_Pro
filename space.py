import requests

r = requests.get('http://api.open-notify.org/astros.json')

print(r.json()["number"])
