#!/usr/bin/python3
def arithmetic(first_arg, second_arg, operation):
	if operation == '+':
		return first_arg + second_arg
	elif operation == '-':
		return first_arg - second_arg
	elif operation == '*':
		return first_arg * second_arg
	elif operation == '/':
		return first_arg / second_arg
	else:
		return "Ошибка. Доступны операторы: +, -, *, /"
