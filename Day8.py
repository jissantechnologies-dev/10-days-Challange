#Function to check if a number is prime

def add(a,b):
    return a + b

print("The sum of 10 and 5 is:", add(10, 5))

print("The sum of 20 and 30 is:", add(20, 30))

def greet(name):
    print("Hello, " + name + "! Welcome to the world of Python programming.")
    print(f"This is a simple Python program that demonstrates the use of functions {name}")

greet("Geevee")


def calculator(a, b, operation):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operation"
    
print(calculator(10, 5, "add"))
print(calculator(10, 5, "subtract"))
print(calculator(10, 5, "multiply"))
print(calculator(10, 5, "divide"))      
print(calculator(10, 0, "divide"))
print(calculator(10, 5, "modulus"))

calc = int(input("Enter first number: "))
calc2 = int(input("Enter second number: "))
operation = input("Enter operation (add, subtract, multiply, divide): ")    
print(calculator(calc, calc2, operation))
