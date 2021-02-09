number = input("输入一个数，我告诉你它是奇数还是偶数：")
number = int(number)

if number % 2 == 0:
	print(f"\n这个数{number}是偶数")
else:
	print(f"\n这个数{number}是奇数")
