# create a program that takes some input, strips it of its vowels, then
# sorts it in alphabetical order

string_set = set(input("Enter some texts: "))
vowels_set = frozenset("aeiou")
new_set = set(string_set - vowels_set)
print(sorted(new_set))

				#or

string_set = set(input("Enter some texts: "))
vowels_set = frozenset("aeiou")
new_set = set()

for letter in string_set:
	if letter not in vowels_set:
		new_set.add(letter)

print(sorted(new_set))

