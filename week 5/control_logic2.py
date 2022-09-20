charname = input("what is your name? ").title()
charclass = input("what typr of adventureer are you? ").title()

def welcomescreen():
    if(charname == "Ninja" and charclass == "Mage"):
        print("hello mage. watch them fireballs.")
    elif(charname == "Bob" or charclass == "Builder"):
        print("i bet you like to build things.")
    elif(charname != "Bob" and charname != "Ninja"):
        print("hmmm... i dont think weve met.")
    elif(charname == "Bob" or charname == "Ninja"):
        print("i figured one of you two would show up.")
    else:
        print("weve reached the final else.")
welcomescreen()
print(charname)