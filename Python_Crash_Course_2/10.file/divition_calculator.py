# try:
# 	print(5/0)
# except ZeroDivisionError:
# 	print("You can't division by zero!")

print("给我两个数，我将它们相除。")
print("输入q退出程序")

while True:
	first_name = input("\n第一个数字：")
	if first_name == 'q':
		break
	second_name = input("\n第二个数字：")
	if second_name == 'q':
		break
	try:
		answer = int(first_name) / int(second_name)
	except ZeroDivisionError:
		print("你不能除0")
	else:
		print(answer)