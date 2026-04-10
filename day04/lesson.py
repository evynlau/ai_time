# Day 04: 不同种类的"东西"
# 🎯 学习目标：了解字符串、整数、浮点数
#
# 📖 故事：想象一个超级商店！
# 📝 盒子 1: 名字 (文字)
# 🔢 盒子 2: 数字 (可以计算)
# 📊 盒子 3: 价格 (带小数点)

# 不同类型的盒子
name = "彩虹"          # 字符串：文字
age = 8                # 整数：整数
price = 9.99           # 浮点数：小数
color = "🌈"           # Emoji：也是文字！

print(f"🎨 名称：{name}")
print(f"👶 年龄：{age}岁")
print(f"💰 价格：${price}")
print(f"🎉 颜色：{color}")

# 🎮 练习：创建不同类型的数据
fruit = "苹果"
count = 5
weight = 1.5

print(f"🍎 我有 {count} 个 {fruit}")
print(f"⚖️ 重量：{weight}公斤")

# 🎯 小挑战：试试连接文字和数字
sentence = "我有 " + str(count) + " 个 " + fruit
print(f"📝 一句话：{sentence}")
