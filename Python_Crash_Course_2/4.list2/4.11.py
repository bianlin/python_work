pizzas = ["腊肠披萨", "鸡肉披萨", "沙拉披萨"]
frient_pizzas = pizzas[:]

pizzas.append('藤椒鸡披萨')
frient_pizzas.append('黄焖鸡披萨')

print('My favorite pizzas are:')
for pizza in pizzas:
	print(pizza)

print("My friend's favorite pizzas are:")
for pizza in frient_pizzas:
	print(pizza)