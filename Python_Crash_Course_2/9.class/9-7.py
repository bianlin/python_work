from classes.user import User

class Admin(User):
	def __init__(self, first_name, last_name):
		super().__init__(first_name, last_name)
		self.privileges = [
			"can add post",
			"can delete post",
			"can ban user",
		]

	def show_privileges(self):
		for v in self.privileges:
			print(f"管理员拥有：{v}")

admin = Admin("Li", "CODE")
admin.show_privileges()