def make_sandwich(*toppings):
	"""概述要制作的三明治"""
	print("\n制作三明治需要下面的食材：")
	for topping in toppings:
		print(f"- {topping}")

make_sandwich("火腿")
make_sandwich("火腿", "鸡蛋")
make_sandwich("火腿", "鸡蛋", "面包")
