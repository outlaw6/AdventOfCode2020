lista1 = []
list_of_list = []
#print(lista1)\
f = open('input.txt.txt', 'r')
temp_list = []
c=0
for x in f:
	temp_list.append(x.strip('\n'))
steps = 3
counter = 0
treeLine = 1


while treeLine <= len(temp_list) - 1:

	if temp_list[treeLine][steps % 31] == '#':
		print("Correct: ", treeLine, steps, len(temp_list[treeLine]))
		counter+=1
		steps+=7
		treeLine+=1

	else:
		steps+=3
		treeLine+=1
	#print(x)
print(counter, steps, steps%31, treeLine)

