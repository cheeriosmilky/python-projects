q = int(input('year: '))

for1 = q % 4
for2 = q % 100
for3 = q % 400
forother = for1, for3
forall = for1, for2, for3


if (for3 == 0) and (for2 == 0):
    print('leap year')
elif (for1 == 0) and (for2 != 0):
    print('leap year')
else:
    print('not leap year')