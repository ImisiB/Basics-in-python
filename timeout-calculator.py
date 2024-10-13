import time

while True:
    print("WELCOME TO THE CALCULATOR APP")
    time.sleep(1.5)
    print("WHAT CALCULATION DO YOU WANT TO PERFORM?")
    time.sleep(1.5)
    print("A = Addition")
    time.sleep(1.5)
    print("B = subtraction")
    time.sleep(1.5)
    print("C = Multiplication")
    time.sleep(1.5)
    print("D = Division")
    time.sleep(1.5)
    print("E = Quit")
    time.sleep(1.5)
    option = input("WHAT IS YOUR OPTION? ")


    if option.lower() == "A".lower():
        num1 = input("Enter your first number: ")
        num2 = input("Enter your second number: " )
        print(num1, "+", num2, "=", str(int(num1) + int(num2)))
        print()
    elif option.lower() == "B".lower():
        num1 = input("Enter your first number: ")
        num2 = input("Enter your second number: " )
        print(num1, "-", num2, "=", str(int(num1) - int(num2)))
        print()
    elif option.lower() == "C".lower():
        num1 = input("Enter your first number: ")
        num2 = input("Enter your second number: " )
        print(num1, "*", num2, "=", str(int(num1) * int(num2)))
        print()
    elif option.lower() == "D".lower():
        num1 = input("Enter your first number: ")
        num2 = input("Enter your second number: " )
        print(num1, "/", num2, "=", str(int(num1) / int(num2)))
        print()
    elif option.lower() == "E".lower():
        print("Thanks for using the calculator-app")
        quit()