f = open("passports.txt",'r').readlines()

main_list = []
temp_list = []
char_eof = '\n'

for x in f:
	if x == char_eof:
		
		main_list.append(temp_list)
		temp_list = []
		continue
	
	temp_list.append(x.split("  "))
main_list.append(temp_list)
temp_list2 = []
main_list2 = []
for elemnt in main_list:
	temp_list2 = []
	for _ in elemnt:
		print(elemnt)
		print(str(_).split(" "))
		temp_list2 += str(_).split(" ")
	main_list2.append(temp_list2)
print(main_list2)
