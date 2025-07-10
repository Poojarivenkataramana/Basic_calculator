
# ✅ 5. Menu-Driven Calculator
# Scenario: Display a menu with options (add, subtract, multiply, divide, exit). Keep taking input and performing operations until the user chooses exit.
# 1. Add
# 2. Subtract
# 3. Multiply
# 4. Divide
# 5. Exit

n1 = int(input("Enter the number1: "))
n2 = int(input("Enter the number2: "))

while True:
    print("""
    1.Add
    2.Subtract
    3.Multiply
    4.Divide
    5.Exit
""")
    choose = input("Enter what  operation you perform: ")
    if choose == "1":
        print("Output:",n1 + n2)
    elif choose == "2":
        print("Output:",n1 - n2)

    elif choose == "3":
        print("Output:",n1 * n2)

    elif choose == "4":
        if n2 != 0:
            print("Output:", n1 // n2)
        else:
            print("cannot divisible by zero")
    elif choose == "5":
        break























































































































