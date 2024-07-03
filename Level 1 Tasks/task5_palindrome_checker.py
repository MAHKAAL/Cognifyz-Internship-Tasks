string = input("Enter Your Message Here:  ")
string = (''.join(e for e in string if e.isalnum())).lower()
a = ""
for i in string:
    a = i + a

if a == string:
    print("The String is Palindrome.")
else:
    print("The String is not Palindrome.")