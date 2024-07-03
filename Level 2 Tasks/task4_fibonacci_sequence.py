from numpy import size


def fibonacci(n):
	if n < 1:
		print("Given number is a negative value!\n....\nNegative values are not allowed! Try again.\n")
		return
	
	p = 0
	q = 1
	print(f"Fibonacci Series for {n} is:  ")
	for i in range(1, n + 1):
		if i == 1:
			print(p,end=" ")
		elif i == 2:
			print(q,end=" ")
		elif i > 2:
			sum = p + q
			p = q
			q = sum
			print(sum,end=" ")

size_ = int(input("Enter a number upto which you want to find fibonacci series.\n...\nEnter Here:  "))
fibonacci(size_)