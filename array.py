from array import *
arr = array('i',[1,2,3,4,5])
print(arr)

arr1 = array('i',[])
n = int(input("Enter the length of the array"))

for i in range(n):
	x = int(input("Enter the next value"))
	arr1.append(x)
	print(arr1)
search_val = int(input("Enter value for search"))

for i in arr1:
	if i == search_val:
		print("Yes this value is here")



		