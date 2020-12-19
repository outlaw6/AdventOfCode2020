lista1 = []
list_of_list = []
#print(lista1)\
f = open('input.txt', 'r')
temp_list = []
c=0
for x in f:
	temp_list.append(x.strip('\n'))
steps = 0
counter = 0
treeLine = 0
print(len(temp_list))

while treeLine <= len(temp_list) - 1:
	if temp_list[treeLine][steps % 31] == '#':
		counter+=1
		steps+=1
		treeLine+=2
	else:
		steps+=1
		treeLine+=2

print(counter, steps, steps%31, treeLine)

