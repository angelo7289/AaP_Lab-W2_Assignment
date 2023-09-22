number1 = input("Enter first number: ")
operator = input("Enter the operator ")
number2 = input("Enter second number: ")
result = number1 + operator + number2

if number1.isdigit() == True and number2.isdigit() == True:
    if operator == '+':
        result = int(number1) + int(number2)
    elif operator == '-':
        result = int(number1) - int(number2)
    elif operator == '*':
        result = int(number1) * int(number2)
    elif operator == '/':
        result = int(number1) / int(number2)
    print (result)
else:
    print("Operation is not valid.")
