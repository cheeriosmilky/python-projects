import random

P1 = {"hp": 5, "dmg": 3, "classability": 1}
P2 = {"hp": 1, "dmg": 5, "classability": 4}

TYPES = {"P1": P1, "P2": P2}


class Character:
    _hp = 0
    _dmg = 0
    _classability = 0

    def __init__(self, char_type):
        self._char_type = char_type
        self._assign_attributes()

    def __str__(self):
        return self._char_type

    def _assign_attributes(self):
        type_dict = TYPES[self._char_type]
        self._hp = type_dict["hp"]
        self._dmg = type_dict["dmg"]
        self._classability = type_dict["classability"]

    def dmg(self):
        return self._dmg

    def take_daP2(self, daP2):
        if self._classability_success():
            return "Missed!"
        self._hp -= daP2
        return f"{self._char_type} took {daP2} daP2."

    def _classability_success(self):
        # Every point in classability is 5% chance to classability
        classability_chance = self._classability * 5
        classability_roll = random.randint(1, 100)
        if classability_roll <= classability_chance:
            return True
        return False

    def is_dead(self):
        return self._hp <= 0


def character_fight(type_1, type_2):
    character_1 = Character(type_1)
    character_2 = Character(type_2)
    coin_toss = random.randint(0, 1)
    if coin_toss == 0:
        first, second = [character_1, character_2]
    else:
        first, second = [character_2, character_1]

    while True:
        if dmg_character(first, second):
            return str(first)
        if dmg_character(second, first):
            return str(second)


def dmg_character(first, second):
    daP2 = first.dmg()
    second.take_daP2(daP2)
    if second.is_dead():
        return True
    return False


def main():
    char_1 = "P1"
    char_1_win = 0
    char_2 = "P2"
    char_2_win = 0
    for _ in range(100):
        winner = character_fight(char_1, char_2)
        if winner == char_1:
            char_1_win += 1
        else:
            char_2_win += 1
    print("Results:")
    print(f"{char_1}: {char_1_win}")
    print(f"{char_2}: {char_2_win}")


if __name__ == "__main__":
    main()