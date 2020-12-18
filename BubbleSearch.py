def SortAlgo(x):
	#Implementing bubble sort
	#in Python
	#for better or worse
	carrier = x
	for times in range(len(x)):
		for num  in range(len(carrier) - 1):
			if carrier[num] > carrier[num+1]:
				carrier[num], carrier[num+1] = carrier[num+1], carrier[num]
	return carrier


if __name__ == '__main__':
	list1 = [2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 100]
	print(SortAlgo(list1))
	print(32 % 32)
	print(31 % 32)
	print(6 % 32)
	print(39 % 32)