num = input("我猜猜你填写的数是不是10的倍数：")
num = int(num)

if num % 10 == 0:
	print(f"这个数{num}是10的倍数")
else:
	print(f"这个数{num}不是10的倍数")
