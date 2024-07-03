print("""
      Options:

      1 = To Convert Celcius into Farenheit.
      2 = To Convert Farenheit into Celcius.
      3 = To Close the Program.
    """)
print("Choose any option from above for Performing Conversion.")


for option in (1,2,3):
    option = int(input("Enter Your Choice:  "))
    if option == 1:
        temp_C = float(input("\nEnter the Temperature in Celcius(No. only): "))
        temp_F = ((9/5) * temp_C) + 32
        print(f"Temperature in Celcius is: {temp_C} C.")
        print(f"Temperature in Farenheit is: {temp_F} F.\n")
        continue
    elif option == 2:
        temp_F = float(input("\nEnter the Temperature in Farenheit(No. only): "))
        temp_C = (5/9)*(temp_F - 32)
        print(f"Temperature in Farenheit is: {temp_F} F.")
        print(f"Temperature in Celcius is: {temp_C} C.|\n")
        continue
    elif option == 3:
        print("Thank You for using this Program.\n")
        break
else:
    print("\nPlease choose a valid option....!!!")
    print("Program is going to close. Please run again..!\n")