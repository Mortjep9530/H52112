

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

def Current_balance:




print("Select operation.")
print("1. Add funds")
print("2. Subtract funds")
print("3. check current funds")



while True:
    # take input from the user
    choice = input("Enter choice(1, 2 or 3): ")

    # check if choice is one of the two options
    if choice in ('1', '2', '3'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':



        elif choice == '2':
            if subtract(num1, num2) > 0:
                print(num1, "-", num2, "=", subtract(num1, num2))

            elif subtract(num1, num2) < 0:
                print("Invalid, not enough mikkel")

        elif choice == '3':
            print(Current_Balance)

        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Need anything else? (yes/no): ")
        if next_calculation == "no":
            break

    else:
        print("Invalid Input")