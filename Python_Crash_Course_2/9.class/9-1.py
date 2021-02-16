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

dagefandian = Restaurant('大哥饭店', '中餐')
print(dagefandian.restaurant_name)
print(dagefandian.cuisine_type)
dagefandian.describe_restaurant()
dagefandian.open_restaurant()