#DAy 5 part 2

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

claimed = set([int(s, 2) for s in seats])
print("Part 1:{0}".format({max(claimed)}))

allseats = set(range(128 * 8))
openseats = allseats - claimed
myseat = [
    seat
    for seat in openseats
    if seat + 1 not in openseats and seat - 1 not in openseats
]

print("Part 2:{0}".format({myseat[0]}))