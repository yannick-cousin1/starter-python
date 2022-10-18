#regex mod
import re

#function to return length of a list
def length(list):
	c = 0
	for j in list:
		c += 1
	return c

#open file and read
with open("data.txt") as file:
	content = file.read()
#Note sure if it's considered cheating :
#	number = content.split()
#	print ("Nombre de mots = ", length(number))


#using regex to isolate all words in a list
	words = re.findall(r"\b[a-zA-Z]{1,}\b", content)
	print ("Nombre de mots = ", length(words))
	
