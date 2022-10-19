
x = 1

while x <= 100:
	# modulo operation gives us the remainder of division.
	# If i%j = 0 ( The remainder of "i" divided by "j" is 0) then "i" is a multiple of "j"
	#we just need to test all numbers from 1 to 100 in a loop
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
