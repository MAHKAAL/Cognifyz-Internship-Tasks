import random
import math

lower, upper = map(int,input("Enter and range of Number(a and b): ").split("and"))
x = random.randint(lower, upper)
z = round(math.log(upper - lower + 1, 2))
print("\nOnly",z,"chances are there to guess the correct answer!\n")

count = 0
while count < z:
	count += 1
	guess = int(input("Guess a number: "))
	if x > guess:
		print("Too low!")
	elif x < guess:
		print("Too high!")
	else:
		print("Congratulations! you guessed correct answer in",count, "try")
		break
	print("\nNow",z - count,"chances are left to guess the correct answer!\n")

	
if count > z:
	print("\nThe number is %d" % x)
	print("Well Tried!  Better Luck Next time!\n")
