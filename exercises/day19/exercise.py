# Day 19 课后练习题 - 字典练习
print("练习 1: 学生信息")

# 创建学生字典
student = {
    "name": "小明",
    "age": 8,
    "grade": "三年级",
    "score": 90
}

print("📝 学生信息:")
for key in student:
    print(f"   {key}: {student[key]}")

# 🎯 挑战：添加新信息
print("\n➕ 添加新信息:")
student["favorite"] = "编程"
student["hobby"] = "画画"

print("📝 更新后的信息:")
for key in student:
    print(f"   {key}: {student[key]}")

# 创建宠物字典
print("\n🐱 宠物信息:")
pet = {
    "type": "小猫",
    "name": "咪咪",
    "color": "白色",
    "age": 2
}

print(f"🐱 类型：{pet['type']}")
print(f"🏷️ 名字：{pet['name']}")
print(f"🎨 颜色：{pet['color']}")
print(f"🎂 年龄：{pet['age']} 岁")
