# Первые шаги
#Простейший калькулятор 

what=input("Действие, которое будем выполнять(+, -, /, *): ")
if what == "+":
	a=float(input("Первое число: "))
	b=float(input("Второе число: "))
	c = a + b
	print("Результат сложения: " + str(c))
elif what == "-":
	a=float(input("Первое число: "))
	b=float(input("Второе число: "))
	c = a - b
	print("Результат вычетания: " + str(c))
elif what == "*":
	a=float(input("Первое число: "))
	b=float(input("Второе число: "))
	c = a * b
	print("Результат умножения: " + str(c))
elif what == "/":
	a=float(input("Первое число: "))
	b=float(input("Второе число: "))
	if b != 0:
		r = a % b 
		if r == 0:
			c = a / b
			print("Результат деления: " + str(c))
		else:
			c = a // b 
			print("Результат деления: " + str(c) + " с остатком: " + str(r))
	else:
		print("Деление на ноль, ответа нет!")
else:
	print("Данного арифметического знака не существует!")