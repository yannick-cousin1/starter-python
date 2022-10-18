
def fill_myList_and_sort(*args):
	myList = []
	for x in args:
		myList.append(x)
	myList.sort()
	for y in myList:
		print (y)

fill_myList_and_sort(10,9,8,7,6,5,4,3,2,1)
