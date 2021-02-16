def read_file(filename):
	try:
		with open(filename, encoding='utf-8') as f:
			content = f.read()
	except FileNotFoundError:
		pass
	else:
		print(content.rstrip())

filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
	read_file(filename)