list = ["han", "July", "Tom"]
print("我找到了更大的餐桌")
list.insert(0, "Lulu")
list.insert(2, "Mone")
list.append("Judy")
print("新购买的餐桌无法及时送达，我只能邀请两位嘉宾共进晚餐")
print(f"很抱歉的通知您:{list.pop()}，无法邀请您共进晚餐")
print(f"很抱歉的通知您:{list.pop()}，无法邀请您共进晚餐")
print(f"很抱歉的通知您:{list.pop()}，无法邀请您共进晚餐")
print(f"很抱歉的通知您:{list.pop()}，无法邀请您共进晚餐")

print(f"{list[0]}，您依然在受邀之列")
print(f"{list[1]}，您依然在受邀之列")

del list[1]
del list[0]

print(f"名单还有人数：{len(list)}")