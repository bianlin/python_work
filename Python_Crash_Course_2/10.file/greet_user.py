import json

filename = 'username.json'

with open(filename, encoding='utf-8') as f:
	username = json.load(f)
	print(f"Welcome back, {username}")