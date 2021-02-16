class Privileges:
	"""docstring for Privileges"""
	def __init__(self):
		self.privileges = [
			"can add post",
			"can delete post",
			"can ban user",
		]

	def show_privileges(self):
		for v in self.privileges:
			print(f"管理员拥有：{v}")
		