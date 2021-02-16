import json

username = input("你叫什么名字？")

filename = 'username.json'
with open(filename, 'w') as f:
	json.dump(username, f)
	print(f"如果你回来，我将记住你，{username}")