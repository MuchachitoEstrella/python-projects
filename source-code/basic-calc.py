# # DOES SIMPLE MATH

def operate():
    
    hasoperator = False
    hasnums = False
    hasawnser = False

    while hasoperator == False:
        operator = input("enter operator +(+) / -(-) / ×(x) / ÷(/): ")
        if operator != "+" and operator != "-" and operator != "x" and operator != "/":
            print("please try again")
        else:
            hasoperator = True

    while hasnums == False:
        try:
            num1 = float(input("enter num1: "))
            num2 = float(input("enter num2: "))
            hasnums = True
        except:
            print("please try again")

    if operator == "+":
        awnser = num1 + num2
    elif operator == "-":
        awnser = num1 - num2
    elif operator == "x":
        awnser = num1 * num2
        operator = "×"
    else:
        awnser = num1 / num2
        operator = "÷"
    
    r = int(round(awnser, 0))
    p = awnser

    print(f"\n{num1} {operator} {num2} =\n\nrounded: {r}\npresise: {p}\n")
    continue_running = input("would you like to power off [y]es / [n]o: ")
    return continue_running == "n"

while True:
    if operate() is False:
        exit(0)

