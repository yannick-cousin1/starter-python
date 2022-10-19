""" Please note that the job has changed after I've done it
	The original goal was to count the number of unique extension """


#import regex mod
import re

# length function will return length of a list
def length(list):
	c = 0
	for j in list:
		c += 1
	return c

#open the file domains.xml
with open("domains.xml") as file:

#search for a regular expression : beginning with "." and followed by any string (containing at least 2 characters) and ending by "<" or " " or "/"
	x = re.findall(r"\.[a-z]{2,}[<\s/]" , file.read())
#create new empty list to remove final character of every variable in x
#Indeed, each variable finish by "<" or "/"
	list = []
#remove those final char
	for i in x:
		i = i[:-1]
		list.append(i)
#create new empty list to remove duplicates
	final_list = []
#remove duplicates
	for k in list:
		if k not in final_list:
			final_list.append(k)
#print final list and length of final list
	print (final_list)
	print ("Nombre d'extension = ", length(final_list))
