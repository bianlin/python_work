filename = 'learning_python.txt'

with open(filename) as file_object:
	# content = file_object.read()
	# for line in file_object:
	# 	print(line.rstrip())
	lines = file_object.readlines()

# print(content)
for line in lines:
	print(line.rstrip())