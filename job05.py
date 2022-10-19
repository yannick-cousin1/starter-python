
x = int(input("Entrez un nombre : "))
y = int(input("Entrez un autre nombre : "))

# if the first number is smaller than the second
if x < y:
	print ("Valeur 1 : ", x)
	print ("Valeur 2 : ", y)
	# loop to increase x every turn before printing it (Increasing it at the first loop before printing it permit to exclude the first value)
	# range from x to y-1 permit to exclude the second value (y)
	for i in range(x,y-1):
		x += 1
		print (x)
# if the first number is greater than the second
elif x > y:
	print ("Valeur 1 : ", x)
	print ("Valeur 2 : ", y)
	# Same loop as before but in reverse (i is going from x to y-1(to exclude the second number) decreasing itself)
	for i in range(x,y+1,-1):
		x -= 1
		print (x)
elif x == y:
	print ("Valeur 1 : ", x)
	print ("Valeur 2 : ", y)
	print ("Valeurs égales")
else:
	print ("Erreur, il faut entrer des nombres")
