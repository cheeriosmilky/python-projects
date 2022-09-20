from time import sleep
import santuccicode as sc

sc.clearconsole()

def answer():
    password = input("whats is the answer to life, the universe and everything? ")
    if(password == '42'):
        print("welcome wise one. i see you have traveled the galaxy. let us begin.")
        sleep(2)
        sc.clearconsole()
    elif(password == 'bob'):
        print("this is no time for jokes")
    else:
        print("i see you are new. go get more experience and come back.")

def  level1():
    print("the man opens the door.")
    sleep(2)
    sc.clearconsole()
    print("an old wizard approaches you.")
    sleep(2)
    sc.clearconsole()
    beginquest = input("are you ready to begin your adventures? y/n")
    if(beginquest == "y"):
        print("the adventure begins...")
    else:
        print("you are correct. best if you go get some sleep.")

answer()