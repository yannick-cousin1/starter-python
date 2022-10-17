
x = int(input("Entrez un nombre : "))
y = int(input("Entrez un autre nombre : "))


if x < y:
	print ("Valeur 1 : ", x)
	print ("Valeur 2 : ", y)
	for i in range(x,y-1):
		x += 1
		print (x)
elif x > y:
	print ("Valeur 1 : ", x)
	print ("Valeur 2 : ", y)
	for i in range(x,y+1,-1):
		x -= 1
		print (x)
elif x == y:
	print ("Valeur 1 : ", x)
	print ("Valeur 2 : ", y)
	print ("Valeurs égales")
else:
	print ("Erreur, il faut entrer des nombres")
