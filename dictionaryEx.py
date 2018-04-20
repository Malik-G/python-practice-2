synonyms = {"inoculate": ["Inject", "Vaccinate"],
			"ostracize": ["Avoid", "Exclude", "Shun"]}

# add a key to the synonyms dictionary
synonyms["boisterous"] = ["Loud", "Rambunctious", "Rowdy"]
print(synonyms)

while True:
	
	wordChoice = input("Choose a word: ")
	
	if (wordChoice == "Quit") or (wordChoice == "quit") or (wordChoice == "QUIT"):
		break
	if wordChoice in synonyms:
		print("Here are some synonyms for the word {}: {}".format(wordChoice, synonyms.get(wordChoice)))
	elif wordChoice.lower() in synonyms:
		print("Here are some synonyms for the word {}: {}".format(wordChoice, synonyms.get(wordChoice.lower())))
	elif wordChoice not in synonyms:	
		print("{} is not in this Thesaurus".format(wordChoice))

#---------------------------------------------------------------

# The the dictionary, retrieve a key and its value
for word in synonyms.values():
	print(word)
				# or the faster solution
for word in synonyms:
	print(synonyms[word])

#---------------------------------------------------------------

# sort 'synonyms' alphabetically
synonyms_sorted = sorted(list(synonyms.keys()))
print(synonyms_sorted)
				# or
synonyms_sorted2 = list(synonyms)
synonyms_sorted2.sort()
print(synonyms_sorted2)

