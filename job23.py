#function to return length of a string/list
def length(string):
	c = 0
	for i in string:
		c += 1
	return c

word = input("Entrez un mot : ")
#create a list containing the string
LIST = []
tmp = ''
for i in word:
	LIST.append(i)

#if last char is equal to the char right before it, do nothing and go to the next step of the loop
#at the next step, we compare char -2 and -3. We'll do that till they are different ( to swap them )
for j in range(1,length(LIST)):
	if LIST[-j] == LIST[-1-j]:
		print ('', end = '')
#if it's not equal, then swap them and break
	else:
		tmp = LIST[-1-j]
		LIST[-1-j] = LIST[-j]
		LIST[-j] = tmp
		break

for k in LIST:
	print(k, end = '')   #print each value in the list side by side
print ("")
