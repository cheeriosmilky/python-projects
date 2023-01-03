import random

q = int(input('how many digs: '))
a = int(input('how many combos: '))     #questions

def repeat(times, defs, *repeats):                        #repeat function
    for answerToA in range(times): defs(*repeats)           #if answer in range(amount of times), it repeats it that many times
                ##combo function^##
def nums(): 
    lock = ''
    ops = '1234567890'          #lock is empty  options(ops) are choices
    while len(lock) < q:    
        char = random.choice(ops)  #characters(char)
        lock += char     #adding the chars to final lock combo
    if a > 0:    
        print(lock)
repeat(a, nums)     #calling main func and combo repeat func