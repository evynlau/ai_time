# Day 11 课后练习题 - 列表练习
print("练习 1: 购物清单")

# 创建购物清单
shopping_list = ["苹果", "香蕉", "牛奶"]

print("📝 购物清单:")
for i, item in enumerate(shopping_list, 1):
    print(f"   {i}. {item}")

# 🎯 挑战：添加更多物品
shopping_list.append("面包")
shopping_list.append("鸡蛋")

print("\n📝 更新后的清单:")
for i, item in enumerate(shopping_list, 1):
    print(f"   {i}. {item}")

# 创建朋友列表
print("\n👫 我的朋友:")
friends = ["小明", "小红", "小刚"]
print(friends)

# 尝试添加好朋友
friends.append("小丽")
print(f"新加入的朋友：{friends[-1]}")
