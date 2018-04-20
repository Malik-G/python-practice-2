r1 = range(2, 13)
modr1 = r1[::3]
print(modr1) # --> (2, 13, 3)
print(modr1.index(11)) # --> 3 , different from indexing an array

# this shows that modr2 == range(7, 16, 2)
r2 = range(0,26)
modr2 = r2[7:16:2]
for i in modr2:
	print(i)

print("=" * 40)

for i in range(7, 16, 2):
	print(i)

# these two are also equal because you get the same set of numbers for both
print(range(0, 5, 2) == range(0, 6, 2))
print(list(range(0, 5, 2)))
print(list(range(0, 6, 2)))

print(range(0, 100)[::-2] == range(99, 0, -2))
print(range(99, 0, -2) == range(99, -1, -2))
print(list(range(99, -1, -2)))

# iterate through something backwards using negative splice
message = "taerg eb"
print(message[::-1])

# count down from a given number
for i in range(1,11)[::-1]:
	print(i)

