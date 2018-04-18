
# Goal is to identify the number of segments in the given IP address,
# as well as the length of each segment
string = input("Enter an IP address: ")
if string[-1] != ".":
	string += "."
sectionCount = 1
sectionLength = 0
totalCharacters = 0
for char in string:
	if char == ".":
		print("set {} contains {} characters".format(sectionCount, sectionLength))
		sectionCount += 1
		sectionLength = 0
	else:
		sectionLength += 1
		totalCharacters += 1

if sectionCount == 1:
	print("This IP address contains 1 set")
else:
	print("This IP address contains {} sets with a total of {} characters".format(sectionCount, totalCharacters))

