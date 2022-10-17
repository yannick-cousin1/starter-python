
x = 1

while x <= 100:
	a = x%3
	b = x%5

	if a == 0 and b == 0:
		print ("FizzBuzz")
	elif a == 0:
		print ("Fizz")
	elif b == 0:
		print ("Buzz")
	else:
		print (x)
	x += 1

