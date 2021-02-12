from collections import defaultdict
with open('bags.txt', 'r') as bags:
	bags = bags.readlines()

dikt = {}
bagsz = defaultdict(dict)
for bag in bags:
	newb = bag.strip('\n').split(" ")
	color = ' '.join(newb[:2])
	in_parts = ' '.join(newb[4:]).split(",")

	for part in in_parts:

		if 'no other bags' not in part:
			sp = part.strip().split(' ')
			print(sp)
			bagsz[color][' '.join(sp[1:3])] = int(sp[0])
		else:
			bagsz[color] = {}	

print(bagsz)