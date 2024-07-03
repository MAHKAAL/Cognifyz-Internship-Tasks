# Method 1 using loop
print("""
      Options:

      + = To Perform Addition(+) Operation.
      - = To Perform Substraction(-) Operation.
      * = To Perform Multiplication(*) Operation.
      / = To Perform Dvivsion(/) Operation.
      % = To Perform Modulus(%) Operation.
      E = To Close the Program.
    """)

for operator in ("+","-","*","/","%","E","e"):
    operator = input("Enter Operator of Your Choice:  \n")
    if operator == "+":
        a = int(input("Enter the First Number here:  "))
        b = int(input("Enter the Second Number here:  "))
        c = a+b
        print(f"Summation of the given numbers {a} and {b} is: {c}\n")
        continue
    elif operator == "-":
        a = int(input("Enter the First Number here:  "))
        b = int(input("Enter the Second Number here:  "))
        c = a-b
        print(f"Differnce between the given numbers {a} and {b} is: {c}\n")
        continue
    elif operator == "*":
        a = int(input("Enter the First Number here:  "))
        b = int(input("Enter the Second Number here:  "))
        c = a*b
        print(f"Multiplication of the given numbers {a} and {b} is: {c}\n")
        continue
    elif operator == "/":
        a = int(input("Enter the First Number here:  "))
        b = int(input("Enter the Second Number here:  "))
        c = a/b
        print(f"Division between the given numbers {a} and {b} is: {c}")
        continue
    elif operator == "%":
        a = int(input("Enter the First Number here:  "))
        b = int(input("Enter the Second Number here:  "))
        c = a%b
        print(f"Remainder after division between the given numbers {a} and {b} is: {c}")
        continue
    elif operator == "E" or "e":
        print("Thank You for using this Program.\n")
        break
else:
    print("\nPlease choose a valid option....!!!")
    print("Program is going to close. Please run again..!\n")


# Method 2 using function


# def cal(a,b,op):
#     for op in ("+", "-", "*", "/", "%", "E", "e"):
#         if op == "+":
#             c = a + b
#             return (f"Result:  {c}")
#         elif op == "-":
#             c = a - b
#             return (f"Result:  {c}")
#         elif op == "*":
#             c = a * b
#             return (f"Result:  {c}")
#         elif op == "/":
#             c = a / b
#             return (f"Result:  {c}")
#         elif op == "%":
#             c = a % b
#             return (f"Result:  {c}")
#         else:
#             return ("Please Valid option...!!!")
#     print("Thank you for using this program.")
        
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# op = input("Enter operator: ")

# print(cal(a,b,op))