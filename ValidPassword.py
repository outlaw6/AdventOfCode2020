# A program from lasy year CodeAdvent
# Check if passwd is valid ;]
def isVlid(l):
	# Divides the line into list elements and takes the 1st element of 1st
	minimalOccurance = (l.split(" ")[0]).split("-")[0]
	#print(minimalOccurance)
	# Rather complex structure takes the second number of the 1st element
	# i.e. 6-9 = takeves everything from -to the end and then strips the '-'
	maximalOccurance = ((l.split(" ")[0])[-2::]).strip("-")
	#print(maximalOccurance)
	print(l.split(" "))
	element = l.split(" ")[1].strip(":")
	#print(element)
	# The work begins here
	# Line by line
	numOfOccuranceInList = 0
	for x in l.split(" ")[2].strip("\n"):
		if x == element:
			numOfOccuranceInList += 1
	
	
	return (int(numOfOccuranceInList) >= int(minimalOccurance)) and (int(numOfOccuranceInList) <= int(maximalOccurance))

f = open("passwords.txt", "r")

#print(isVlid(f.readline()))0
counter = 0
for linea in f:
	if isVlid(linea):
		counter += 1

print(counter)