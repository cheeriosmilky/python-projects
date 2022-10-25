temps = []
f = open('Grill_1.txt')
for line in f.readlines():
    temps.append(float(line))
f.close()

lowest = temps[0]
highest = temps[0]

for t in temps:
    if t < lowest:
        lowest = t
    if t > highest:
        highest = t

print('Lowest temp = '+str(lowest))
print('Highest temp = '+str(highest))