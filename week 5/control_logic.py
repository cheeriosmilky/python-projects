charname = input("what is your name? ").title()

def welcomescreen():
    if(charname == "Ninja"):
        print("hello warrior...")
    if(charname == "Bob"):
        print("i bet you like to build things.")
    if(charname != "Bob" and charname != "Ninja"):
        print("hmmm... i dont think weve met.")
    if(charname == "Bob" or charname == "Ninja"):
        print("i figured one of you two would show up.")
welcomescreen()
print(charname)