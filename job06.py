
x = True
# Since x = True, the loop will last till x changes. It will only change if user's input is "Au revoir"
while x:
	y = input("> ")
	if y == "Bonjour":
		print ("Bonjour à toi")
	elif y == "Au revoir": #Here we quit the loop by changing x to False
		x = False
	else:
		print (y) #If the input is not "Bonjour" or "Au revoir" then just print the input.
