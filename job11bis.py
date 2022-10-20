""" new version of Job 11 without regex """

c = 0 #counter
LIST = []
#open the file domains.xml
with open("domains.xml") as file:
	x = file.readlines()
	   											# x is a list. Each value is a line of the file
	for i in x:									# For each line
		if "domain" in i and "column" in i:	  	# If the line contains the string "domain" and "column" 
												# ( One line contains "domain" but there is no domain in it)
			LIST.append(i)						# Add it to a new list
			c += 1								# count it

	for j in range(len(LIST)):				#Just another loop to compare every domains
		for k in range(j+1,len(LIST)):		#in order to decrease counter if a domain is in the list twice
			if LIST[j] == LIST[k]:
				c -= 1

	print ("Number of domains in domains.xml : ", c)
