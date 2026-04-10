# Day 04 课后练习题 - 不同类型的盒子
print("练习 1: 识别数据类型")

# 判断每个变量的类型
name = "小华"      # 是什么类型？
age = 10           # 是什么类型？
score = 95.5       # 是什么类型？
is_happy = True    # 是什么类型？

# 你的答案:
print(f"\n📝 类型:")
print(f"   name = '{name}' -> {type(name).__name__}")
print(f"   age = {age} -> {type(age).__name__}")
print(f"   score = {score} -> {type(score).__name__}")
print(f"   is_happy = {is_happy} -> {type(is_happy).__name__}

# 🎯 挑战: 创建不同类型的 5 个变量
fruit = "苹果"
number = 7
price = 12.99
is_raining = False
emoji = "🍎"

print("\n🌟 你的 5 个不同类型变量:")
print(f"   1️⃣ 水果：{fruit} ({type(fruit).__name__})")
print(f"   2️⃣ 数字：{number} ({type(number).__name__})")
print(f"   3️⃣ 价格：{price} ({type(price).__name__})")
print(f"   4️⃣ 天气：{is_raining} ({type(is_raining).__name__})")
print(f"   5️⃣ 表情：{emoji} ({type(emoji).__name__})")
