print("Simple calculator")

num1 = float(input("Enter the first number:"))
operation = input("Select operation (+ - * /):")
num2 = float(input("Enter the second number:"))


print("\nResults:")
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} / {num2} = {num1 / num2}")

if operation == "+": 
    print(num1 + num2)
elif operation == "-":
    print(num1 - num2)
elif operation == "*":
    print(num1 * num2)
elif operation == "/":
    print(num1 / num2)
else:
    print("Invalid result. Please try again.")