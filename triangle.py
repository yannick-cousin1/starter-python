
h = int(input("Entrez la hauteur : "))
x = 1 #We can determine number of whitespaces at the beginning of each line with this counter
y = h #With this one, we'll determine number of whitespaces inside the triangle at each line

#Indeed we can calculate this two values with height (h)

while x <= h:

	#Here we print a number of whitespaces at the beginning depending of h
	for i in range (0,h-x):
		print (" ", end = '')
	#Once it's done, we print "/" (left side of the triangle)
	print ("/", end = '')
	#Then, we need to print whitespaces inside the triangle
	for j in range (0,h-y):
		#If we're at the last line, it will not be whitespaces but "_" to close the triangle
		if h-x == 0:
			print ("_", end = '')
		#Else, we're not at the end and we need to print whitespaces
		else:
			print (" ", end = '')
	print ("\\") #we print "\" at the end of each line
	
	x += 1 # x is increased in order to reduce number of whitespaces at the begining of each line (One whitespace less at each line)
	y -= 2 # y is decreased by 2 in order to increase number of whitespaces inside the triangle (2 wwhitespaces more at each line)
