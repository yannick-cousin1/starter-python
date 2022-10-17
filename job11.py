import re

def length(list):
	c = 0
	for j in list:
		c += 1
	return c
		

with open("domains.xml") as file:
	x = re.findall(r"\.[a-z]{2,}[<\s/]" , file.read())
	list = []

	for i in x:
		i = i[:-1]
		list.append(i)

	final_list = []

	for k in list:
		if k not in final_list:
			final_list.append(k)
	print (final_list)
	print ("Nombre d'extension = ", length(final_list))
