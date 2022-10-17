
h = int(input("Entrez la hauteur : "))
x = 1
y = h
while x <= h:

	for i in range (0,h-x):
		print (" ", end = '')
	print ("/", end = '')
	for j in range (0,h-y):
		if h-x == 0:
			print ("_", end = '')
		else:
			print (" ", end = '')
	print ("\\")
	x += 1
	y -= 2




