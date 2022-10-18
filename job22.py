
string = input("Entrez une chaine de caractères : ")

#func = input ("Entrez la fonction voulue : ")


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

print (myLower(string))
