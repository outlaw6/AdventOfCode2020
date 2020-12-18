lista1 = []
list_of_list = []
#print(lista1)
f = open('inp.txt', 'r')
temp_list = []
c=0
for x in f:
	temp_list.append(x.strip('\n'))
steps = 3
counter = 0
treeLine = 1


while treeLine <= len(temp_list):

	# print(steps)
	if steps >= 30:
		print(temp_list[treeLine][steps])
		if temp_list[treeLine][30] == '#':
			steps = steps % 30
			counter += 1
			treeLine += 1
			steps+=3
		else:
			steps = steps % 30
			treeLine += 1
	
	if temp_list[treeLine][steps] == '#':
		print(treeLine, steps, len(temp_list[treeLine]))
		counter+=1
		steps+=3
		treeLine+=1

	else:
		steps+=3
		treeLine+=1
	print("Continue !?")
	x = input()
	if x == 'y':
		print("Cyrrent status of elements: ", treeLine, steps)
		continue


	#print(x)
print(counter, steps, steps%31, treeLine)
