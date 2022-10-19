
l = int(input("Largeur : "))
h = int(input("Hauteur : "))


for j in range(0,h):
	#First, we need a "|" at the beginning of each line
	print("|", end = '')
	#Then we check if we're at the first or the last line, cause those lines will be filled with "-"
	if j == 0 or j == h-1:
		for i in range(0,l):
			print ("-", end = '') 
	else:
	#If we're not in the first or the last line, then we're inside, and we'll need to put whitespaces
		for i in range(0,l):
			print (" ", end = '')

	print("|") #Finally we print the last "|" at the end of each line
