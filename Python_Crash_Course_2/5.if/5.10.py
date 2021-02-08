current_users = ['admin', 'bianl', 'han', 'doudou', 'xiaoming']

new_users = ['admin', 'lili', 'hally', 'pote', 'xxxxx']

for nu in new_users:
	if nu in current_users:
		print(f"{nu}已经被使用，请输入别的用户名")
	else:
		print(f"{nu}用户名未被使用")
