import random

name = 'santucci'
question = 'will i fall today'
answer = ''

print(name + " asks: " + question)
print("Magic 8 Ball's answer:" + answer)

random_number = random.randint(1,9)
# print(random_number)

if random_number == 1:
  print("Yes - definitly")
elif random_number == 2:
  print('It is decidedly so.')
elif random_number == 3:
  print('Without a doubt.')
elif random_number == 4:
  print('reply hazy, try again.')
elif random_number == 5:
  print('ask agaiun later')
elif random_number == 6:
  print('better not telling you now')
elif random_number == 7:
  print('my sources say no')
elif random_number == 8:
  print('outlook not so good')
elif random_number == 9:
  print('very doubtful')
else:
  answer = print("error")