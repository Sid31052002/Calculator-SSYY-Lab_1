def multiply(a, b):
    """Multiplication Operation"""
    return a * b
    
def divide(a, b):
    """Division Operation"""
    if b == 0:
        return "Error! Division by zero."
    return a / b

def main():
    print("Welcome to the Calculator!")
    print("Choose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    try:
        choice = int(input("Enter your choice (1/2/3/4): "))
        if choice not in [1, 2, 3, 4]:
            print("Invalid choice. Exiting.")
            return
        
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))

        if choice == 1:
            print(f"The result of addition is: {add(a, b)}")
        elif choice == 2:
            print(f"The result of subtraction is: {subtract(a, b)}")
        elif choice == 3:
            print(f"The result of multiplication is: {multiply(a, b)}")
        elif choice == 4:
            print(f"The result of division is: {divide(a, b)}")
    
    except ValueError:
        print("Invalid input! Please enter numbers only.")

if __name__ == "__main__":
    main()