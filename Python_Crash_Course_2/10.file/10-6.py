print("请输入2个数")
print("输入q退出")

while True:
	first_num = input("请输入第一个数：")
	if first_num == 'q':
		break
	second_num = input("请输入第二个数：")
	if second_num == 'q':
		break
	try:
		num = int(first_num) + int(second_num)
	except ValueError as e:
		print("请输入数字！")
	else:
		print(num)