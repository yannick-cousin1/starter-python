#Function to get length of a list
def length(list):
	c = 0
	for j in list:
		c += 1
	return c
#Function to determine the smallest number of a list
def smallest_one(list):
	min = 2147483647 #maximum value for integer 32 bits
	for z in list:
		if z < min:
			min = z
	return min


def mySort(myList):
	#While first number of the list is greater than the smallest one
	while myList[0] > min(myList):
		for y in range(0,length(myList)-1):
			#Check if the next number is smaller than the current one. If it's the case, swap both numbers
			if myList[y+1] < myList[y]:
				tmp = myList[y]
				myList[y] = myList[y+1]
				myList[y+1] = tmp
	return myList

def myDisplay(myList):
	for x in myList:
		print (x)

myList=[5,5,4,6,10,12,12,12,12,43,433,3,2,1]
mySort(myList)
myDisplay(myList)
