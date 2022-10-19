


def length(string):
	c = 0
	for i in string:
		c += 1
	return c

def myUper(string):
	lowercase = "abcdefghijklmnopqrstuvwxyz"
	uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	uppered = '' #will be the string to return at the end

	#for each char in the string
	for c in string:
		#if the char is a whitespace, append it to "uppered"
		if c == " ":
			uppered += c
		#loop to compare each char with lowercase table and upercase table
		for x in range(26):
			#if current char is a lowercase char, use the same char in uppercase table and append it to "uppered"
			if c == lowercase[x]:
				uppered += uppercase[x]
			#if current char is an uppercase char, append it directly to "uppered"
			elif c == uppercase[x]:
				uppered += c
	return uppered

#myLower function works exactly like myUper but in reverse
def myLower(string):
	lowercase = "abcdefghijklmnopqrstuvwxyz"
	uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	lowered = ''
	for c in string:
		if c == ' ':
			lowered += c
		for x in range(26):
			if c == uppercase[x]:
				lowered += lowercase[x]
			elif c == lowercase[x]:
				lowered += c
	return lowered


#make first lowercase char of each word an uppercase
def myTitle(string):
	lowercase = "abcdefghijklmnopqrstuvwxyz"
	uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	titled = ''
	#for each char in string, if char is a whitespace, add it to the string "titled"
	for c in range(0,length(string)):
		if string[c] == ' ':
			titled += string[c]
		for x in range(26):
			#if a char in the string is a lowercase char AND if the char right before is a whitespace, then use the matching uppercase char
			if string[c] == lowercase[x] and string[c-1] == ' ':
				titled += uppercase[x]
			#if a char is a lowercase but with no whitespace before it, add it to the string "titled"
			elif string[c] == lowercase[x] and string[c-1] != ' ':
				titled += string[c]
	# Now we need to get the very first char of the string to be an uppercase (there is no whitespace before it)
	#string cannot be modified so let's use a list
	LIST = []
	final_titled = ''
	#Put every char of our string to the list
	for ca in titled:
		LIST.append(ca)
	#Find the matching uppercase of the first char of the list and use it
	for y in range(26):
		if string[0] == lowercase[y]:
			LIST[0] = uppercase[y]
	#And final transfer to the string to return
	for z in range(0,length(LIST)):
		final_titled += LIST[z]

	return final_titled

#Erase all useless whitespaces
def myClean(string):
	cleaned = ''
	#for each char in string, if it's a whitespace and the char before is not a whitespace, append it to "cleaned"
	for c in range(0,length(string)):
		if string[c] == ' ' and string[c-1] != ' ':
			cleaned += string[c]
		#of course, if it's not a whitespace, append it to "cleaned"
		elif string[c] != ' ':
			cleaned += string[c]

	#We now need to erase whitespaces at the begining and at the end of the string
	#We cannot modify the string, so again, let's use a new list
	LIST = []
	final_cleaned = ''
	z = 0
	#Append each char of the string to the list
	for x in cleaned:
		LIST.append(x)
	#replace current char by the next one untill the first char of the list is not a whitespace
	while LIST[0] == ' ':
		LIST[z] = LIST[z+1]
		z += 1
	#remove the last char of the list untill the last char is not a whitespace
	while LIST[-1] == ' ':
		LIST.pop(-1)
	#copy the list to a string to return
	for y in range(0,length(LIST)):
		final_cleaned += LIST[y]

	return final_cleaned


string = input("Entrez une chaine de caractères : ")
print ("choose : upper / lower / title/ clean :")
func = input ("Entrez la fonction voulue : ")

if func == "upper":
	print (myUper(string))
elif func == "lower":
	print (myLower(string))
elif func == "title":
	print (myTitle(string))
elif func == "clean":
	print (myClean(string))
else:
	print ("Erreur de choix, try again")
