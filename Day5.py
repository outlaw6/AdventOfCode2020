# ADvent of Code 2020
# Day 5


# start
# BFFFBBFRRR
'''q = open('seats.txt', 'r').readlines()
keys = {"B", "F", "L", "R"}
for n in q:
	print(n.strip('\n'))'''

def f1(arg1):


	l1=[x for x in range(128)]
	l2=[x for x in range(8)]

	s1=arg1[:7]
	s2=arg1[-3:]

	for char in s1:
		if char == 'B':
			num=128
			l1=l1[len(l1)//2:]
		elif char == 'F':
			l1=l1[:len(l1)//2]

	for char in s2:
		if char == 'R':
			l2=l2[len(l2)//2:]
		elif char == 'L':
			l2=l2[:len(l2)//2]
	print(l1[0], l2[0])
	return str(int(l1[0]) * 8 + int(l2[0]))

l1=[x for x in range(128)]

print(l1)
q = open('seats.txt', 'r').readlines()
print(q)
#s1 = 'FBFBBFF'
'''for char in q:
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
		l2=l2[:len(l2)//2]'''

#print("Final seat is: " + str(int(l1[0]) * 8 + int(l2[0]))) # Sry for this mumbo jumbo 
l2=[]
for ar in q:
	#print(f1(ar.strip('\n')))
	l2.append(int(f1(ar.strip('n'))))
print(max(l2))

import sys

with open('seats.txt', "r") as f:
    seats = (
        f.read()
        .strip()
        .replace("B", "1")
        .replace("F", "0")
        .replace("R", "1")
        .replace("L", "0")
        .split("\n")
    )

print(max([int(s,2) for s in seats]))
