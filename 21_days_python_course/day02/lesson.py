# Day 02: 变量与数据类型
# 📖 变量 = 存储数据的盒子

# 1. 变量定义
name = "小明"
age = 12
height = 1.55
is_student = True

# 2. 使用变量
print("我的名字:", name)
print("我今年", age, "岁")
print("身高", height, "米")
print("是学生:", is_student)

# 3. 数据类型
print("\n📊 数据类型:")
print("name:", type(name).__name__)
print("age:", type(age).__name__)
print("height:", type(height).__name__)
print("is_student:", type(is_student).__name__)

# 4. f-string 格式化
message = f"我叫{name}, {age}岁，{height}米"
print("\n", message)

print("\n🎉 Day 02 完成!")
