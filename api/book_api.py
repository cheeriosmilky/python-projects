import os
import requests
\
query = input('book: ')
q = query.replace(' ', '%20')

link = 'https://www.googleapis.com/books/v1/volumes?q='+q
linkk = requests.get(link)

nums = 
print(nums)
