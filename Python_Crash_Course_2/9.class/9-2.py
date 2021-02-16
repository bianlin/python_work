class Restaurant(object):
	"""docstring for Restaurant"""
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		
	def describe_restaurant(self):
		print(self.restaurant_name)
		print(self.cuisine_type)

	def open_restaurant(self):
		print(f"{self.restaurant_name}正在营业")

kfc = Restaurant('肯德基', '西式快餐')
macDonald = Restaurant('麦当劳', '西式快餐')
chaoyixing = Restaurant('超意兴', '中式快餐')
kfc.describe_restaurant()
macDonald.describe_restaurant()
chaoyixing.describe_restaurant()
