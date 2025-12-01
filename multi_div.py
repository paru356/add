# Simple Python program to multiply and divide two numbers

# Input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Multiplication
product = num1 * num2

# Division (check to avoid division by zero)
if num2 != 0:
    quotient = num1 / num2
else:
    quotient = "Undefined (division by zero not allowed)"

# Output results
print(f"{num1} * {num2} = {product}")
print(f"{num1} / {num2} = {quotient}")