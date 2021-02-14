from collections import defaultdict
from functools import lru_cache
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
def can_hold(in_color, out_color):
    if in_color in str(bagsz[out_color]):
        return True
    return any([can_hold(in_color, b)for b in bagsz[out_color]])

part1 = sum([can_hold('shiny gold', bag) for bag in bagsz])
print(part1)

def num_inside(color):
    return sum([bagsz[color][b] * (1 + num_inside(b)) for b in bagsz[color]])


part1 = sum([can_hold("shiny gold", bag) for bag in bags])
print("Part 1: ",part1)
print('Part 2: ',num_inside("shiny gold"))