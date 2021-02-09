def build_profile(first, last, **user_info):
	"""创建一个字典，其中包括我们知道的有关用户的一切"""
	user_info['first_name'] = first
	user_info['last_name'] = last
	return user_info

user_profile = build_profile('卞', '林', age=36, location='济南', field='数学')

print(user_profile)
