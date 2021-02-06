# ADvent of Code 2020
# Day 5


# start
# BFFFBBFRRR
'''q = open('seats.txt', 'r').readlines()
keys = {"B", "F", "L", "R"}
for n in q:
	print(n.strip('\n'))'''

l1=[x for x in range(128)]

print(l1)


s1 = 'FBFBBFF'
for char in s1:
	if char == 'B':
		num=128
		l1=l1[len(l1)//2:]
	elif char == 'F':
		l1=l1[:len(l1)//2]

l2=[x for x in range(8)]
s2="RLR"

for char in s2:
	if char == 'R':
		l2=l2[len(l2)//2:]
	elif char == 'L':
		l2=l2[:len(l2)//2]
print(l1,l2)

print("Final seat is: " + str(int(l1[0]) * 8 + int(l2[0]))) # Sry for this mumbo jumbo 