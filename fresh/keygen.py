import random

# # DAY
# def dayverify(key):
#     global score
#     score = 0
#     checkdig = key[1]
#     checkdigtimes = 0
#     chunks = key.split('-')
    
#     for i in chunks:
#         if len(i) != 4:
#             return False
#         for char in i:
#             if char == checkdig:
#                 checkdigtimes += 1
#             score += ord(char)
    
#     if score > 1400 and score < 1500 and checkdigtimes == 2:
#         return True
#     else:
#         False
    
# def daygen():
#     key = ''
#     sec = ''
#     checkdig = 0
#     letters = 'abcdefghijklmnopaqrstuvwxya1234567890'
    
#     while len(key) < 25:
#         char = random.choice(letters)
#         key += char
#         sec += char
        
#         if len(sec) == 4:
#             key += '-'
#             sec = ''
#     key = key[:-1]
    
#     if dayverify(key):
#         print(key)
#         print('valid DAY')
#         print(f'{score}')
#     else:
#         daygen()

# # WEEK
# def weekverify(key):
#     global score
#     score = 0
#     checkdig = key[1]
#     checkdigtimes = 0
#     chunks = key.split('-')
    
#     for i in chunks:
#         if len(i) != 4:
#             return False
#         for char in i:
#             if char == checkdig:
#                 checkdigtimes += 1
#             score += ord(char)
#     if score > 1500 and score < 1600 and checkdigtimes == 2:
#         return True
#     else:
#         False
    
# def weekgen():
#     key = ''
#     sec = ''
#     checkdig = 0
#     letters = 'abcdefghijklmnopaqrstuvwxya1234567890'
    
#     while len(key) < 25:
#         char = random.choice(letters)
#         key += char
#         sec += char
        
#         if len(sec) == 4:
#             key += '-'
#             sec = ''
#     key = key[:-1]
    
#     if weekverify(key):
#         print(key)
#         print('valid WEEK')
#         print(f'{score}')
#     else:
#         weekgen()

# MONTH

# def monthverify(key):
#     global score
#     global checkdigtimes3
    
#     score = 0
#     checkdig = key[1]
#     checkdigtimes3 = 0
#     chunks = key.split('-')
    
#     for i in chunks:
#         if len(i) != 4:
#             return False
#         for char in i:
#             if char == checkdig:
#                 checkdigtimes3 += 1
#             score += ord(char)
#     if score > 1600 and score < 1700 and checkdigtimes3 == 3:
#         return True
#     else:
#         False
q = int(input('digs: '))
def monthgen():
    key = ''
    sec = ''
    checkdig = 0
    letters = 'abcdefghijklmnopaqrstuvwxya1234567890'
    
    while len(key) < q:
        char = random.choice(letters)
        key += char
        sec += char
        
    #     if len(sec) == 4:
    #         key += '-'
    #         sec = ''
    # key = key[:-1]
    print(key)
    # if monthverify(key):
    #     print(key)
    #     print('valid MONTH')
    #     print(f'{score}')
    # else:
    #     monthgen()
monthgen()