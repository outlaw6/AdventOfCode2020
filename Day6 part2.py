#
#
#
import string
import sys


with open('day6.txt', "r") as f:
    answers = f.read().strip().split("\n\n")

part1 = sum([len(set(ans.replace("\n", ""))) for ans in answers])
print(part1)

count = 0
for ans in answers:
    ind_ans = ans.split("\n")
    for c in string.ascii_lowercase:
        count += all([c in a for a in ind_ans])

print(count)