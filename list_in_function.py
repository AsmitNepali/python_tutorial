def count(lst):
	even = 0
	odd = 0

	for i in lst:
		if i%2==0:
			even +=1
		else:
			odd +=1
	return even,odd
lst = [20,21,25,16,15,23,27,29]
even,odd = count(lst)
print("Even: {} and Odd: {}".format(even,odd))