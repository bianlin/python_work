class User(object):
	"""docstring for User"""
	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name
		self.login_attempts = 0

	def describe_user(self):
		print(f"我是{self.first_name} {self.last_name}")

	def greet_user(self):
		print(f"你好啊{self.first_name} {self.last_name}")

	def increment_login_attempts(self):
		self.login_attempts += 1

	def reset_login_attempts(self):
		self.login_attempts = 0

u = User("BBB", "CCCC")
u.increment_login_attempts()
u.increment_login_attempts()
u.increment_login_attempts()
u.increment_login_attempts()
print(u.login_attempts)
u.reset_login_attempts()
print(u.login_attempts)