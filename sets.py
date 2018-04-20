# two ways to create sets, one is using curly brackets
artists = {"Raury", "A$AP", "Kanye"}
for each in artists:
	print(each)

print("=" * 25)

# or you can use the set([]) function - lists inside parenthesis
artists2 = set(["Raury", "A$AP", "Kanye"])
for each in artists2:
	print(each)

#=============================================
# to transform an iterable object (e.g. range, lists, tuples) into a
# set you have to use the set() function
my_range = set(range(0, 15, 2))
my_list = set([1, 3, 5, 7, 9, 10])

# .union combines both sets, duplicate values are only recorded once
print(my_range.union(my_list)) # output -> {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14}
print(my_range | my_list)
# .intersection takes all of the values that appear in both sets, use '&' as alt
print(my_range.intersection(my_list)) # ouput -> {10}
print(my_range & my_list)

# symmetric _difference is everything except for the identical values (opposite of intersection)
print(my_range.symmetric_difference(my_list)) 
print(my_list.symmetric_difference(my_range))
print(my_list ^ my_range)

print(my_range.difference(my_list))
print(my_range - my_list)
print(my_list - my_range) # output -> {1,2,3,4,5,6,7,8,9}
print(my_range.difference_update(my_list))

my_range.add("milk")
my_range.discard(4)
my_list.remove(3) # .remove will return an error if the parameter is invalid, .discard will not
print(my_range)
print(my_list)

# superset if the set contains all of the elements of another set.. >=
# subset if all of a set's elements are contained in the other set.. <=



