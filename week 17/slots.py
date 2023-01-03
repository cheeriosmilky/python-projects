import random

q = 3

key = ''
sec = ''
checkdig = 0
letters = '1234567890'
    
while len(key) < q:
    char = random.choice(letters)
    key += char
    sec += char


player = {f"roll1": {key}, "roll2": {key}, "roll3": {key}}

TYPES = {"P1": player}

class game:
    roll1 = 0
    roll2 = 0
    roll3 = 0

    def __init__(self, char_type):
        self._char_type = char_type
        self.rollatts()

    def __str__(self):
        return self._char_type

    def rollatts(self):
        type_dict = TYPES[self._char_type]
        self.roll1 = type_dict["roll1"]
        self.roll2 = type_dict["roll2"]
        self.roll3 = type_dict["roll3"]

def main():
    char_1 = "roll"
    char_1_win = key
    if key == [111, 222, 333, 444, 555, 666, 777, 888, 999, 000]:
        print("result:")
        print(f"{char_1}: {char_1_win}")
        print('winner!')
    else:
        print("result:")
        print(f"{char_1}: {char_1_win}")

if __name__ == "__main__":
    main()