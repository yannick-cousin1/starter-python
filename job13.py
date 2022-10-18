# regex mod
import re
#function to return length of a list
def length(list):
	c = 0
	for j in list:
		c += 1
	return c

user_input = int(input("Entrez un nombre : "))


with open("data.txt") as file:
	content = file.read()
	words = re.findall(r"\b[a-zA-Z]{%d}\b" %(user_input) , content)




	print (f"Nombre de mots contenant {user_input} caractères : {length(words)}")

