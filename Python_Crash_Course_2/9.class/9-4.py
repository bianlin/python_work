class Restaurant(object):
	"""docstring for Restaurant"""
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0
		
	def describe_restaurant(self):
		print(self.restaurant_name)
		print(self.cuisine_type)

	def open_restaurant(self):
		print(f"{self.restaurant_name}正在营业")

	def set_number_served(self, num):
		self.number_served = num

	def increment_number_served(self, num):
		self.number_served += num

r = Restaurant("黄焖鸡米饭", "中式快餐")
print(f"就餐人数{r.number_served}")
r.number_served = 10
print(f"就餐人数{r.number_served}")
