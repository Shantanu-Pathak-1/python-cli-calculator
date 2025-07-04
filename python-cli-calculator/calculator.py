def subtract_num(a, b):
    return a - b

def add_num(a, b):
    return a + b

def multiply_num(a, b):
    return a * b

def divide_num(a, b):
    return a / b

print("Choose an operation:")
print("1. Add") 
print("2. Multiply")
print("3. Subtract")
print("4. Divide")
print("Enter the number corresponding to your choice:")

user_input = int(input())
if user_input < 1 or user_input > 4:
    print("Invalid choice. Please select a number between 1 and 4.")
    exit()

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if user_input == 1:
    print(f"Sum: {add_num(a, b)}")
elif user_input == 2:
    print(f"Product: {multiply_num(a, b)}")
elif user_input == 3:
    print(f"Difference: {subtract_num(a, b)}")
elif user_input == 4:
    if b != 0:
        print(f"Division: {divide_num(a, b)}")
    else:
        print("Error: Division by zero is not allowed.")