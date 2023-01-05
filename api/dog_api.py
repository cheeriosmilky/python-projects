import requests

burl = 'https://dog.ceo/api/'

endp = 'breeds/image/random'

r = requests.get(burl + endp)

print(r.json())

