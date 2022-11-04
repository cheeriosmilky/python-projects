
customername = input("Welcome, what is your name? ")
startingbalance = 5000.25

def greeting():
    print(f"Hello {customername} your starting balance is {startingbalance}")
greeting()

paycheck = float(input("How much of your paycheck would you like to deposit? $"))

expeditureitem = input("Looks like you went shopping. What did you buy? ")
expediture = float(input(f"How much did the {expeditureitem} cost? $"))

# subamount = startingbalance - expediture

def checkingbalance(customername, startingbalance, paycheck, expeditureitem, expediture):
    # endingbalance = float(input(f"Good day, {customername}. After spending money on {expeditureitem} in the amount of {expediture}, your current checking balance is: {startingbalance} - {expediture}"))
    # print(endingbalance)
    endingbalance = startingbalance - expediture + paycheck
    print(f"Good day, {customername}. After spending money on {expeditureitem} in the amount of ${expediture}, your current checking balance is: {endingbalance}")
    # print(endingbalance)
checkingbalance(customername, startingbalance, paycheck, expeditureitem, expediture)