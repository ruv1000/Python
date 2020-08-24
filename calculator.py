# First steps
# Simply calculator 

from colorama import Back
from colorama import init

init()


def first_number():
    x1 = input("Enter first number: ")
    condition = x1.isdigit() and not x1.isspace() and (x1 != "+" or x1 != "-" or x1 != "*" or x1 != "/")
    while not condition:
        x1 = input("Please, enter a number: ")
        condition = x1.isdigit() and not x1.isspace() and (x1 != "+" or x1 != "-" or x1 != "*" or x1 != "/")
    return float(x1)


def second_number():
    x2 = input("Enter second number: ")
    condition = x2.isdigit() and not x2.isspace() and (x2 != "+" or x2 != "-" or x2 != "*" or x2 != "/")
    while not condition:
        x2 = input("Please, enter a number: ")
        condition = x2.isdigit() and not x2.isspace() and (x2 != "+" or x2 != "-" or x2 != "*" or x2 != "/")
    return float(x2)


function = input("What arithmetic operations we will perform(+, -, /, *): ")
i = function == "+" or function == "-" or function == "*" or function == "/"

while not i:
    print(Back.RED, "Wrong! Division by zero, no answer!")
    print(Back.RESET)
    function = input("Please, enter the correct arithmetic sign(+, -, /, *): ")
    i = function == "+" or function == "-" or function == "*" or function == "/"

if function == "+":
    c = first_number() + second_number()
    print("Result: " + str(c))

elif function == "-":
    c = first_number() - second_number()
    print("Result: " + str(c))

elif function == "*":
    c = first_number() * second_number()
    print("Result: " + str(c))

elif function == "/":
    a = first_number()
    b = second_number()

    while b == 0:
        print(Back.RED, "Wrong! Division by zero, no answer!")
        print(Back.RESET)
        b = float(input("Enter a divisor other than zero: "))

    r = a % b
    if r == 0:
        c = a / b
        print("Result: " + str(c))
    else:
        c = a // b
        print("Result: " + str(c) + " remainder of the division: " + str(r))

input()
