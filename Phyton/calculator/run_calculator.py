import calculator

print("Welcome to the simple calculator!")
print("---")

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /): ")

    result = None

    if operation == '+':
        result = calculator.add(num1, num2)
    elif operation == '-':
        result = calculator.subtract(num1, num2)
    elif operation == '*':
        result = calculator.multiply(num1, num2)
    elif operation == '/':
        result = calculator.divide(num1, num2)
    else:
        result = "Error: Invalid operation entered."

    print(f"The result is: {result}")

except ValueError:
    print("Error: You did not enter valid numbers.")