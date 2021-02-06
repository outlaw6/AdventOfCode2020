# ADvent of Code 2020
# Day 5


# start
# BFFFBBFRRR
'''q = open('seats.txt', 'r').readlines()
keys = {"B", "F", "L", "R"}
for n in q:
	print(n.strip('\n'))'''

l1=[x for x in range(128)]
l2=l1[:]
print(l1)


s1 = 'FBFBBFF'
for char in s1:
	if char == 'B':
		num=128
		l1=l1[len(l1)//2:]
	elif char == 'F':
		l1=l1[:len(l1)//2]
seats="RLR"
print(l1)