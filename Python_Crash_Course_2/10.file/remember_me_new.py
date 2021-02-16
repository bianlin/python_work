import json

def get_stored_username():
	"""如果存储了用户名，就获取它。"""
	filename = 'username.json'
	try:
		with open(filename) as f:
			username = json.load(f)
	except FileNotFoundError:
		return None
	else:
		return username

def get_new_username():
	"""提示用户输入用户名。"""
	username = input("你的名字是？")
	filename = 'username.json'
	with open(filename, 'w') as f:
		json.dump(username, f)
	return username

def greet_user():
	"""问候用户，并指出其名字"""
	username = get_stored_username()
	if username:
		print(f"欢迎回来，{username}")
	else:
		username = get_new_username()
		print(f"你回来时，我会记住你，{username}")


greet_user()