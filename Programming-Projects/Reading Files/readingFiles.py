'''
with open('Computer-Science/Programming-Projects/Reading Files/names.txt') as file_object:
	contents = file_object.read()
	print(contents)


with open('Computer-Science/Programming-Projects/Reading Files/names.txt') as file_object:
	contents = file_object.read()
	print(contents.rstrip())

with open('Computer-Science/Programming-Projects/Reading Files/names.txt') as file_object:
	for line in file_object:
	    print(line)
'''
myNames = []
with open('Computer-Science/Programming-Projects/Reading Files/names.txt') as file_object:
	lines = file_object.readlines()
	for line in lines:
		line = line.rstrip()
		myNames.append(line)
	print(myNames)
