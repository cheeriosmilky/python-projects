
msirtxa5000price = 4199.35
gigabyteaeroprice = 4296.54
razerblade15price = 3696.99
asuszephyrusm16price = 1849.79
addpc = msirtxa5000price + gigabyteaeroprice + razerblade15price + asuszephyrusm16price

# def mini():
#     (asuszephyrusm16price)
# min = mini
# def maxi():
#     (gigabyteaeroprice)
# max = maxi

def minmax():
    print(f"The most expensive laptop amount is: {gigabyteaeroprice}")
    print(f"The least expensive laptop amount is: {asuszephyrusm16price}")
minmax()

roundedRTX = round(msirtxa5000price)
roundedAERO = round(gigabyteaeroprice)
roundedRAZER = round(razerblade15price)
roundedASUS = round(asuszephyrusm16price)

def roundedpc():
    print(f"The rounded price of the MSI 5000 is {roundedRTX}")
    print(f"The rounded price of Gigabyte Aero is {roundedAERO}")
    print(f"The rounded price of the Razer Blade 15 is {roundedRAZER}")
    print(f"The rounded price of the Asus Zephyrus is {roundedASUS}")
roundedpc()

def avepc():
    print(f"The average price of all computers is: {addpc / 4}")
avepc()
