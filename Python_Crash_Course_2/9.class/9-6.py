from classes.restaurant import Restaurant

class IceCreamStand(Restaurant):
	"""docstring for IceCreamStand"""
	def __init__(self, restaurant_name, cuisine_type):
		super().__init__(restaurant_name, cuisine_type)
		self.flavors = ["草莓冰淇淋", "香草冰淇淋"]

	def show_flavors(self):
		print(f"最爱的冰淇淋：{self.flavors}")


ice = IceCreamStand('七七冰淇淋', '冷饮店')
ice.show_flavors()