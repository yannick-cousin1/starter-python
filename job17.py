
def fill_myList_and_print_even_numbers(*args):
	myList = args
	for x in myList:
		if x % 2 == 0:
			print (x)

fill_myList_and_print_even_numbers(1,2,3,4,5,6,7,8,9,10)
