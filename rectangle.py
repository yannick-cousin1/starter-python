
l = int(input("Largeur : "))
h = int(input("Hauteur : "))


for j in range(0,h):
	print("|", end = '')
	if j == 0 or j == h-1:
		for i in range(0,l):
			print ("-", end = '')
	else:
		for i in range(0,l):
			print (" ", end = '')

	print("|")




