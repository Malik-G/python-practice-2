#Practice using break
print("This meal comes with: Turkey, Eggs, Peppers, Spinach")
exclude = input("Do you want everything on that? What do you want removed? ")
meal = ["turkey", "eggs", "peppers", "spinach"]

for item in meal:
	if item == exclude.casefold():
		exclude = item
		print("No {}".format(exclude))
		break
else: #this else is attached to the for instead of the if, so the print executes only when the break is not needed
	print("The works!")


#Practice using continue
full_shopping_list = ["milk", "eggs", "turkey", "bread"]
priority_list = "Priority items: "
for item in full_shopping_list:
	if item == "eggs" or item == "turkey":
		continue #use this command to bypass a particular instance, i.e. "eggs"
	priority_list += (item + ", ")


print(priority_list[:-2]) #removes the space and comma at the end for a cleaner look



