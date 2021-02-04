# 3.10.py
list = ["中国", "美国", "法国", "英国", "俄罗斯"]

print(list)
print(f"今天没有参加会议，去掉他：{list.pop()}")
print(list)
list.append("日本")
print(list)
list.insert(1, "朝鲜")
print(list)
del list[4]
print(list)
list.pop(3)
print(list)
list.remove("朝鲜")
print(list)
list.reverse()
print(list)
list.reverse()
print(list)
list.sort()
print(list)
list.sort(reverse=True)
print(list)