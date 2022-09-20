amount = int(input("How many pennies would you like to deposit? "))
dollars = amount // 100
d = amount / 100
amount = amount % 100
qtrs = amount // 25
amount = amount % 25
dimes = amount // 10
amount = amount % 10
nickles = amount // 5
amount = amount % 5

def output():
    print(f"Dollars: ${dollars}")
    print(f"Quarters: ¢{qtrs}")
    print(f"Dimes: ¢{dimes}")
    print(f"Nickles: ¢{nickles}")
    print(f"Pennies: ¢{amount}")
    print(f"Money Amount: ${d}")
output()