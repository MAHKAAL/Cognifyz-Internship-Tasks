import random
import math

lower, upper = 1, 100
x = random.randint(lower, upper)

count = 0
while True:
	count += 1
	guess = int(input("Guess a number: "))
	if x > guess:
		print("Too low!")
	elif x < guess:
		print("Too high!")
	else :
		print("Congratulations! you guessed correct answer in",count, "try")
		break