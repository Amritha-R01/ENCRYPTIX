import math

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

    if choice in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        try:
            a, b = map(float, input("Enter two numbers separated by space: ").split())
        except ValueError:
            print("Invalid input. Please enter two numbers.")
            continue

        if choice == '1':
            print("Result:", a + b)
        elif choice == '2':
            print("Result:", a - b)
        elif choice == '3':
            print("Result:", a * b)
        elif choice == '4':
            if b == 0:
                print("Error: Division by zero!")
            else:
                print("Result:", a / b)
        elif choice == '5':
            print("Result:", a % b)
        elif choice == '6':
            print("Result:", a ** b)
        elif choice == '7':
            if b == 0:
                print("Error: Division by zero!")
            else:
                print("Result:", a // b)
        elif choice == '8':
            print("Result:", abs(a))
        elif choice == '9':
            if a < 0:
                print("Error: Negative Number Entered")
            else:
                print("Result:", math.sqrt(a))
    elif choice == '10':
        print("Exiting the calculator. Thank You!")
        break
    else:
        print("Invalid choice. Please select from 1 to 10.")
