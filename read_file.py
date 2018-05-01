# read_file.py and sample.txt have the same path since they are in the same
# folder, therefore I don't have to include "/Users/Malik/desktop/udemy_ex/section10/"
# in order for open() to work
my_file = open("/Users/Malik/desktop/udemy_ex/section10/sample.txt", "r")
for line in my_file:
	print(line, end='')
print("\n")
my_file.close()

# =============================================

# Using a with-as statement catches the error of omitting .close()\
# readline() reads a single line, returns it as a string
with open("sample.txt", "r") as my_file:
	line = my_file.readline()
	while line:
		print(line, end='')
		line = my_file.readline()
print("\n")

# =============================================

# .readlines() reads the entire file, returns as a list of strings
with open("sample.txt", "r") as my_file:
	entire_file = my_file.readlines()
for lines in entire_file:
	print(lines, end='')
print("\n")

# =============================================
# read() reads the entire file. If it is a txt file the contents are returned as a string
with open("sample.txt", "r") as my_file:
	entire_file = my_file.read()
print(entire_file)
print("\n")



