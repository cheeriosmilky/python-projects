import statistics
grill1 = open('Grill_1.txt', 'r')
read1 = grill1.readlines()
mod1 = []
for line1 in read1:
    mod1.append(int(line1.strip('ï»¿')))

grill2 = open('Grill_2.txt', 'r')
read2 = grill2.readlines()
mod2 = []
for line2 in read2:
    mod2.append(int(line2.strip('ï»¿')))
    
grill3 = open('Grill_3.txt', 'r')
read3 = grill3.readlines()
mod3 = []
for line3 in read3:
    mod3.append(int(line3.strip('ï»¿')))

grill4 = open('Grill_4.txt', 'r')
read4 = grill4.readlines()
mod4 = []
for line4 in read4:
    mod4.append(int(line4.strip('ï»¿')))

grill5 = open('Grill_5.txt', 'r')
read5 = grill5.readlines()
mod5 = []
for line5 in read5:
    mod5.append(int(line5.strip('ï»¿')))

# Grill 1
calculate = [mod1, mod2, mod3, mod4, mod5]
sum1 = sum(calculate[0])
min1 = min(calculate[0])
max1 = max(calculate[0])
mean1 = sum1 / 99
dev1 = statistics.stdev(mod1)
dev1x2 =  dev1 * 2
addmean1 = mean1 - dev1x2
submean1 = mean1 + dev1x2
def end1():
    if submean1 < min1:
        print('Too Cold')
    elif addmean1 > max1:
        print("Too Hot")
    else:
        print('Pass!')
print('Grill 1:')
print(f'Min: {min1}')
print(f'Max: {max1}')
print(f'Mean: {mean1}')
print(f'Standard Deviation of temps is {dev1}')
end1()
print('')

# Grill 2
calculate = [mod1, mod2, mod3, mod4, mod5]
sum2 = sum(calculate[1])
min2 = min(calculate[1])
max2 = max(calculate[1])
mean2 = sum2 / 99
dev2 = statistics.stdev(mod2)
dev2x2 =  dev2 * 2
addmean2 = mean2 - dev2x2
submean2 = mean2 + dev2x2
def end2():
    if submean2 < min2:
        print('Too Cold')
    elif addmean2 > max2:
        print("Too Hot")
    elif addmean2 > max2 and submean2 < min2 :
        print('Too Hot and Cold')
    else:
        print('Pass!')
print('Grill 2:')
print(f'Min: {min2}')
print(f'Max: {max2}')
print(f'Mean: {mean2}')
print(f'Standard Deviation of temps is {dev2}')
end2()
print('not working one ^')
print('')

# Grill 3
calculate = [mod1, mod2, mod3, mod4, mod5]
sum3 = sum(calculate[2])
min3 = min(calculate[2])
max3 = max(calculate[2])
mean3 = sum3 / 99
dev3 = statistics.stdev(mod3)
dev3x2 =  dev3 * 2
addmean3 = dev3x2 + mean3
submean3 = dev3x2 - mean3
def end3():
    if submean3 < min3:
        print('Too Cold')
    elif addmean3 > max3:
        print("Too Hot")
    else:
        print('Pass!')
print('Grill 3:')
print(f'Min: {min3}')
print(f'Max: {max3}')
print(f'Mean: {mean3}')
print(f'Standard Deviation of temps is {dev3}')
end3()
print('')

# Grill 4
calculate = [mod1, mod2, mod3, mod4, mod5]
sum4 = sum(calculate[3])
min4 = min(calculate[3])
max4 = max(calculate[3])
mean4 = sum4 / 99
dev4 = statistics.stdev(mod4)
dev4x2 =  dev4 * 2
addmean4 = dev4x2 + mean4
submean4 = dev4x2 - mean4
def end4():
    if submean4 > min4:
        print('Too Cold')
    elif addmean4 < max4:
        print("Too Hot")
    else:
        print('Pass!')
print('Grill 4:')
print(f'Min: {min4}')
print(f'Max: {max4}')
print(f'Mean: {mean4}')
print(f'Standard Deviation of temps is {dev4}')
end4()
print('')

# Grill 5
calculate = [mod1, mod2, mod3, mod4, mod5]
sum5 = sum(calculate[4])
min5 = min(calculate[4])
max5 = max(calculate[4])
mean5 = sum5 / 99
dev5 = statistics.stdev(mod5)
dev5x2 =  dev5 * 2
addmean5 = mean5 - dev5x2
submean5 = mean5 + dev5x2
def end5():
    if submean5 < min5:
        print('Too Cold')
    elif addmean5 > max5:
        print("Too Hot")
    else:
        print('Pass!')
print('Grill 5:')
print(f'Min: {min5}')
print(f'Max: {max5}')
print(f'Mean: {mean5}')
print(f'Standard Deviation of temps is {dev5}')
end5()