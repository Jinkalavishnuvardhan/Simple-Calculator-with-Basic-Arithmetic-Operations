
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("\nSelect Operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("Enter choice (1/2/3/4 or + - * /): ")


if choice == '1' or choice == '+':
    result = num1 + num2
    print(f"Result: {num1} + {num2} = {result}")
elif choice == '2' or choice == '-':
    result = num1 - num2
    print(f"Result: {num1} - {num2} = {result}")
elif choice == '3' or choice == '*':
    result = num1 * num2
    print(f"Result: {num1} * {num2} = {result}")
elif choice == '4' or choice == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"Result: {num1} / {num2} = {result}")
    else:
        print("Error: Division by zero is not allowed!")
else:
    print("Invalid operation choice!")
