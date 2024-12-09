def calculator():
    print("This is Culculator and we will start now!")
    while True:
        try:
            num1 = float(input("Enter the 1st number:> "))
            operation = input("Select an operation [ 1.(+) 2.(-) 3.(*) 4.(/) ]:> ")
            num2 = float(input("Enter the 2cd number:> "))
            
            if operation == '1':
                result = num1 + num2
            elif operation == '2':
                result = num1 - num2
            elif operation == '3':
                result = num1 * num2
            elif operation == '4':
                if num2 != 0:
                    result = num1 / num2
                else:
                    print("Error: Division by zero is not allowed.")
                    continue
            else:
                print("Invalid operation. Please try again.")
                continue
            
            print(f"The result of {num1} {operation} {num2} = {result}")
        
        except ValueError:
            print("Invalid input! Please enter numbers only.")
            continue
        
        choice = input("Would you like to make another calculation? (yes/no): ").lower()
        if choice != 'yes':
            print("See ya next time!")
            break

calculator()
