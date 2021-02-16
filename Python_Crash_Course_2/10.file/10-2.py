filename = 'learning_python.txt'

with open(filename) as file_object:
	lines = file_object.readlines()

py_string = ''
for line in lines:
	py_string += line.strip()

print(py_string.replace('Python', 'C'))