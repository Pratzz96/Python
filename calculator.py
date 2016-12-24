while True:
    print("Options:")
    print("Enter 'ADD' to add two numbers")
    print("Enter 'SUBTRACT' to subtract two numbers")
    print("Enter 'DIVIDE' to divide two numbers")
    print("Enter 'MULTIPLY' to nultiply two numbers")
    print("Enter 'QUIT' to end the program")
    user_input=input(":")
    if user_input == "quit":
        break
    elif user_input == "add":
        num1=float(input("Enter a number:"))
        num2=float(input("Enter another number:"))
        print(num1+num2)
    elif user_input == "subtract":
        ...
    elif user_input == "multiply":
        ...
    elif user_input == "divide":
        ...
    else:
        print("unknown input")
        
