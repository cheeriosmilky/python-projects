def greeting(x):
    # print('Hello')

    if x < 12:
        print('Good morning')
    else:
        print('Good afternoon')

time = int(input('What time is it?'))

greeting(time)