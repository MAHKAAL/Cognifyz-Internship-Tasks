string = input("Enter Your Message Here:  ")
a = ""
for i in string:
    a = i + a

print(f"Oringinal String is:  {string}")
print(f"Reversed String is:  {a}")