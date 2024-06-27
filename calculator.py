while True:
    # Get user input for numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Get user input for operator
    operator = input("Choose an operator (+, -, *, /): ")

    # Perform calculation using if statements
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            print("Error: Division by zero")
            continue
        else:
            result = num1 / num2
    else:
        print("Error: Invalid operator")
        continue

    # Print result if no errors
    print(f"{num1} {operator} {num2} = {result}")

    # Check if the user wants to perform another calculation
    if input("Do you want to perform another calculation? (yes/no): ").lower() != 'yes':
        break
