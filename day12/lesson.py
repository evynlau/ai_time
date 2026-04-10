# Day 12: 列表操作
# 🎯 学习目标：学习如何取列表中的元素
#
# 📖 故事：一盒糖果！
# 1️⃣ 吃掉第 1 颗糖
# 2️⃣ 把第 2 颗糖给朋友
# 3️⃣ 买新糖放进去

# 列表索引：从 0 开始数!
fruits = ["🍎 苹果", "🍌 香蕉", "🍇 葡萄"]

print("第 1 个水果:", fruits[0])
print("第 2 个水果:", fruits[1])
print("第 3 个水果:", fruits[2])

# 加东西到列表
fruits.append("🍊 橘子")
print(f"🍊 新加的水果：{fruits[-1]}")

# 查看列表长度
print(f"📊 列表长度：{len(fruits)} 个水果")

# 🎮 练习：颜色列表
colors = ["red", "blue"]
colors.append("yellow")
colors.append("green")

print(f"🎨 颜色列表：{colors}")
print(f"📊 共有 {len(colors)} 种颜色")

# 🎯 小挑战：取最后一个元素
last_color = colors[-1]
print(f"🌈 最后一颜色是：{last_color}")
