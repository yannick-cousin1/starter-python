
def fill_myList_and_print_even_numbers(*args):
	myList = args #creating "myList" with all args
	for x in myList:
		if x % 2 == 0: 		# For each value of myList, print it if the remainder of division by 2 is equal to 0 (=If it's an even number)
			print (x)

fill_myList_and_print_even_numbers(1,2,3,4,5,6,7,8,9,10)
