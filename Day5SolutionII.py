# Day 5 is very interesting
# This is day 5 part I 
# Solution II
# This is a very elegant
# Byte-wise solution for the Day5 problem

# Check this out...
# Very cool and very smart!

import sys
with open(sys.argv[1], "r") as f:
    seats = (
        f.read()
        .strip()
        .replace("B", "1")
        .replace("F", "0")
        .replace("R", "1")
        .replace("L", "0")
        .split("\n")
    )
'''
print(f"Part 1: {max([int(s, 2) for s in seats])}") # -----> This is to convert in 0s and 1s
'''
# The idea is that each B or F convert to 1 or 0
# And R & L respectively to 1 and 0 also
# Then just do some byte arithmetics
# This is indeed an elegant solution 
# And it was suggested in the website
# Lets rewrite this for proof of concept
# This was proposed by a user
# 0xcdf

s1 = 'FBFBBFFRLR'
s1 = '0101100' + '101'
# Row & Column, 
# Seat Id left
# If you want to completely understand this  you need to dive into bite-shifting
# Here I will just post the solution
# Because I dont want to completely understand this
# But I knew there is some super simple soluton 
# When I saw the 0-127 and 0-7 (1 byte) ranges
# Im joking, just visit https://wiki.python.org/moin/BitwiseOperators
# It will be clear in the second



