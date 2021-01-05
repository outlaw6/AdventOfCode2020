f = open('passports.txt', 'r').readlines()
temp_list1 = [] # store the passports
temp_list2 = [] # stpre 1 by 1
c=0

while c <= len(f) - 1:
	#print(f[c])
	if f[c] != '\n':
		temp_list2.append(f[c])
		c+=1
	elif f[c] == '\n':
		temp_list1.append(temp_list2)
		temp_list2 = []
		c+=1
	else:
		c+=1
	temp_list1.append(temp_list2)

print(temp_list2)
print(temp_list1)