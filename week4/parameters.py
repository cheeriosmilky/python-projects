from unicodedata import name


char_name = input("what is your name?")
char_role = input("what character role are you?")

def my_function(the_name, the_role):
    print(f"your name is {the_name}")
    print(f"your character role is {the_role}")

my_function(char_name, char_role)

char_name2 = input("what is your name?")
char_role2 = input("what character role are you?")

my_function(char_name2, char_role2)
