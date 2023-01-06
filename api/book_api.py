import os
import requests
import json

query = input('book: ')
q = query.replace(' ', '%20')

link = requests.get('https://www.googleapis.com/books/v1/volumes?q='+q)
linkk = json.loads(link.text)
items = linkk['items']
info = linkk['items'][4]

val = linkk['items'][1]['id']
val2 = linkk['items'][2]['etag']
val3 = linkk['items'][3]['selfLink']

print('total items:', linkk['totalItems'])
print('id:', val)
print('etag:', val2)
print('selflink:', val3)
