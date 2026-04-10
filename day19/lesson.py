# Day 19: 字典 - 更智能的盒子
# 🎯 学习目标：理解字典数据结构
#
# 📖 故事：有标签的盒子
# 📦 标签"名字" → "小明"
# 📦 标签"年龄" → 8 岁
# 📦 标签"颜色" → "蓝色"

# 字典用 {} 表示
student = {
    "name": "小明",
    "age": 8,
    "favorite": "编程"
}

print(f"👤 姓名：{student['name']}")
print(f"🎂 年龄：{student['age']}岁")
print(f"🎯 喜欢：{student['favorite']}")

# 添加新标签
student["city"] = "北京"
print(f"🏙️ 城市：{student['city']}")

# 🎮 练习：创建宠物字典
pet = {
    "type": "小猫",
    "name": "咪咪",
    "color": "白色"
}

print()
print(f"🐱 我的小宠物:")
print(f"    类型：{pet['type']}")
print(f"    名字：{pet['name']}")
print(f"    颜色：{pet['color']}")

# 🎯 小挑战：增加宠物年龄
pet["age"] = 2
print(f"    年龄：{pet['age']}岁")
