# First steps
# Simply calculator 

from colorama import init
from colorama import Fore, Back, Style
init()

what=input("What arithmetic operations we will perform(+, -, /, *): ")

if what == "+":
	a=float(input("First number: "))
	b=float(input("Second number: "))
	c = a + b
	print("Result: " + str(c))
elif what == "-":
	a=float(input("First number: "))
	b=float(input("Second number: "))
	c = a - b
	print("Result: " + str(c))
elif what == "*":
	a=float(input("First number: "))
	b=float(input("Second number: "))
	c = a * b
	print("Result: " + str(c))
elif what == "/":
	a=float(input("First number: "))
	b=float(input("Second number: "))
	if b != 0:
		r = a % b 
		if r == 0:
			c = a / b
			print("Result: " + str(c))
		else:
			c = a // b 
			print("Result: " + str(c) + " remainder of the division: " + str(r))
	else:
		print(Back.RED)
		print("Wrong! Division by zero, no answer!")
else:
	print(Back.RED)
	print("This arithmetic sign does not exist!")
input()