try:
	with open('booktemp.txt', encoding='utf-8') as f:
		content = f.read()
except FileNotFoundError:
	pass
else:
	print(content.count('小说'))