
def length(string):
	c = 0
	for i in string:
		c += 1
	return c

word = input("Entrez un mot : ")

LIST = []
tmp = ''
for i in word:
	LIST.append(i)

for j in range(1,length(LIST)):
	if LIST[-j] == LIST[-1-j]:
		print ('', end = '')
	else:
		tmp = LIST[-1-j]
		LIST[-1-j] = LIST[-j]
		LIST[-j] = tmp
		break
	
print (LIST)



