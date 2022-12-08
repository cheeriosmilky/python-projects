q = int(input('year: '))
for1 = q % 4
for2 = q % 100
for3 = q % 400
if for1 == False and for2 != False:
    print('leap year')
elif for3 == False and for2 == False:
    print('leap year')
else:
    print('not leap year')