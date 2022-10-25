num1 = 3.4
num2 = 7

def function():
    quiz = float(input(f"what is {num1} + {num2}: "))
    while(quiz != (num1 + num2)):
        print("no, thats wrong, try again.")
        function()
    print("congrats, thats the correct answer.")
function()