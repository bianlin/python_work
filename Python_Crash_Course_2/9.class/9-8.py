from classes.user import User
from classes.privileges import Privileges

class Admin(User):
	def __init__(self, first_name, last_name):
		super().__init__(first_name, last_name)
		self.privileges = Privileges()

admin = Admin("Li", "CODE")
admin.privileges.show_privileges()