# Key(Word or Variable): Value
# Key:Value Pairs

from curses import termname
from multiprocessing.sharedctypes import Value


sensors = {'living room':2, 'dining room':4, 'kitchen':6, 'basement':12, 'bedroom':1}
living_room = sensors['living_room']
print(f'the living room has {sensors}')
santucci = {'name':'santucci', 'age':16, 'status':True}
sweets = {'donuts':['blue', 'glaze', 'choco'], 'cake':['coco', 'vanilla', 'lemon'], 'cookies':['coco chip', 'oats', 'peanut butter']}
for i in sweets:
    print(i)

numofmembers = {}
numofmembers['silv'] = 27
numofmembers['gold'] = 21
numofmembers.update({'silv':44})
numofmembers.update({'2x gold':2})

drinks = ['espreso', 'chai', 'decaf']
caf = [64, 40, 0, 12]
zipped = zip(drinks, caf)
drinks2caf = {key:value for key, value in zipped}

heros = ['bastion', 'soldier76', 'reinhardt', 'moria', 'zenyatta']
roles = ['dps', 'dps', 'tank', 'support', 'support']
teamcomp = {heros:roles for [heros, roles] in zip(heros, roles)}
