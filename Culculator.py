def calculator():
    print("This is Calculator and we will start now!")
    while True:
        try:
            num1 = float(input("Enter the 1st number:> "))
            operation = input("Select an operation [ + , - , * , / ]:> ")
            
            while True:
                try:
                    num2 = float(input("Enter the 2nd number:> "))
                    if operation == '/' and num2 == 0:
                        print("Error: Division by zero is not allowed. Please enter a non-zero number.")
                        continue  # วนซ้ำเพื่อขอค่า num2 ใหม่
                    break
                except ValueError:
                    print("Invalid input for the second number! Please enter a valid number.")
            
            if operation == '+':
                result = num1 + num2
                symbol = "+"
            elif operation == '-':
                result = num1 - num2
                symbol = "-"
            elif operation == '*':
                result = num1 * num2
                symbol = "*"
            elif operation == '/':
                result = num1 / num2
                symbol = "/"
            else:
                print("Invalid operation. Please try again.")
                continue

            print(f"The result of {num1} {symbol} {num2} = {result}")

        except ValueError:
            print("Invalid input! Please enter numbers only.")
            continue

        choice = input("Would you like to make another calculation? (yes/no): ").lower()
        if choice != 'yes':
            print("See ya next time!")
            break

calculator()
