import json

filename = 'username.json'

# 如果以前存储了用户名，就加载它
# 否则，提示用户输入用户名并存储它
try:
	with open(filename) as f:
		username = json.load(f)
except FileNotFoundError:
	username = input("输入你的名字：")
	with open(filename, 'w') as f:
		json.dump(username, f)
		print(f"如果你回来，我将记住你，{username}")
else:
	print(f"欢迎回来, {username}")