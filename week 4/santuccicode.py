import os
from time import sleep
from turtle import clear

def clearconsole():
    # windows
    if os.name == "nt":
        return os.system('cls')
    
    # for mac & linux
    else:
        return os.system('clear')

# print("hello there.")
# sleep(2)
# clearconsole()
# print("it worked?")