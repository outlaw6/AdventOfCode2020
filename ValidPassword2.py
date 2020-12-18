# A program from lasy year CodeAdvent
# Check if passwd is valid ;]
def isVlid(l):
	# Divides the line into list elements and takes the 1st element of 1st
	position1 = (l.split(" ")[0]).split("-")[0]
	#print(minimalOccurance)
	# Rather complex structure takes the second number of the 1st element
	# i.e. 6-9 = takeves everything from -to the end and then strips the '-'
	position2 = ((l.split(" ")[0])[-2::]).strip("-")
	#print(maximalOccurance)
	print(l.split(" "))
	element = l.split(" ")[1].strip(":")
	#print(element)
	# The work begins here
	# Line by line
	numOfOccuranceInList = 0
	string1 = l.split(" ")[2].strip("\n")
	print(string1, position2, position1)
	print(string1[int(position1) - 1])
	if (string1[int(position1) - 1] == element) and (string1[int(position2) - 1] == element):
		return False
	else:
		return (string1[int(position1) - 1] == element) or (string1[int(position2) - 1] == element)
	#return (int(numOfOccuranceInList) >= int(minimalOccurance)) and (int(numOfOccuranceInList) <= int(maximalOccurance))

f = open("passwords.txt", "r")
isVlid(f.readline())
print(isVlid(f.readline()))
c = 0
for linea in f:
	print(isVlid(linea))
	if isVlid(linea) == True:
		c+= 1

print(c)