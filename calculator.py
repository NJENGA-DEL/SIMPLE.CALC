print("****welcime to the calculator****")
print("please enter two numbers")
num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))
print("please select an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
operation = input("Enter the operation (1/2/3/4):")
if operation == '1':
    result = num1 + num2
    print(f"The result of addition is: {result}")
elif operation == '2':
    result = num1 - num2
    print(f"The result of subtraction is: {result}")
elif operation == '3':
    result = num1 * num2
    print(f"The result of multiplication is: {result}")
elif operation == '4':
    if num2 != 0:
        result = num1 / num2
        print(f"The result of division is: {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation selected. Please choose a valid operation (1/2/3/4).")
print("Thank you for using the calculator!")
