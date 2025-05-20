import math
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return a / b

def modulus(a, b):
    return a % b

def exponent(a, b):
    return a ** b

def floor_divide(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return a // b

def absolute(a):
    return abs(a)

def square_root(a):
    if a<0:
        return "Error: Negative Number Entered"
    return math.sqrt(a)

def calculator():
    while True:
        print("\n<--Simple Calculator-->")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modulus")
        print("6. Exponentiation")
        print("7. Floor Division")
        print("8. Absolute of first number")
        print("9. Square Root of first number")
        print("10. Exit")

        choice = input("Choose an operation (1-10): ")

        if choice in ['1','2','3','4','5','6','7','8','9']:
            try:
                a, b = map(float, input("Enter two numbers separated by space: ").split())
            except ValueError:
                print("Invalid input. Please enter two numbers.")
                continue

            if choice == '1':
                print("Result:", add(a, b))
            elif choice == '2':
                print("Result:", subtract(a, b))
            elif choice == '3':
                print("Result:", multiply(a, b))
            elif choice == '4':
                print("Result:", divide(a, b))
            elif choice == '5':
                print("Result:", modulus(a, b))
            elif choice == '6':
                print("Result:", exponent(a, b))
            elif choice == '7':
                print("Result:", floor_divide(a, b))
            elif choice == '8':
                print("Result:", absolute(a))
            elif choice == '9':
                print("Result:", square_root(a))
        elif choice == '10':
            print("Exiting the calculator. Thank You!")
            break
        else:
            print("Invalid choice. Please select from 1 to 10.")

calculator()
