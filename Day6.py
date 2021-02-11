# Day 6 AoC 2020

def count(arg1):

	l1 = []
	c  = 0

	for a in arg1:
		l1 += a.strip('\n')
	return len(set(l1))



ans = open('day6.txt', 'r')
#print(ans.readlines())
l1 = ans.readlines()
l2 = []
l3 = []
l4 = ['hlqbanmtjy', 'tdrvxcajgnfpoke', 'jtiunkpsroa]']
l3 += l4
for line in l1:
	if line != '\n':
		l2.append(line)
	else:
		l3.append(l2)
		l2 = []
	
# cur = [x.strip('\n') for x in l1]

#print(l3)
print(l3)
c=0
for l in l3:
	print(l)
	c += count(l)


with open('day6.txt', "r") as f:
    answers = f.read().strip().split("\n\n")

part1 = sum([len(set(ans.replace("\n", ""))) for ans in answers])
print(part1)

#print(answers)

