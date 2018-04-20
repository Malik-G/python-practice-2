# tuples such as goats are immutable, menaing they can't be changed
goats = "Russell", "Robertson", "Chamberlain", "Jordan"
print(goats)

# to get around the immutability of tuples, assign the tuple variable to
# be something else. the goats below is different from the one above because
# it points to different data
goats = goats[0], goats[1], goats[2], "Abdul-Jabbar", goats[3]
print(goats)

# or we can unpack a tuple
goat1, goat2, goat3, goat4, goat5 = goats
print(goat3)

# like lists, tuples can nest inside of other tuples
goats = "Russell", "Robertson", "Chamberlain", "Jordan", ((6, "C"), (1, "PG"),
                                                          (13, "C"), (23, "SG"))
goat1, goat2, goat3, goat4, info = goats
spot = 0
for i in info:
	number, position = i
	reading = "{} was #{}, he played the {} position".format(goats[spot], number, position)
	spot += 1
	print(reading)


