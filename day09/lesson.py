# Day 09: for 循环 - 不用重复写代码
# 🎯 学习目标：理解循环的概念
#
# 📖 故事：数气球
# ❌ 不好的方法：写 5 行代码
# ✅ 好的方法：用循环！

# for 循环就像：数 1 次，重复 5 次
for i in range(1, 6):
    print(f"🎈 气球数：{i}")

# 🎮 练习：数星星
print("⭐ 数星星时间:")
for star in range(1, 6):
    print(f"   {star}⭐")

# 数 1 到 5 的苹果
print()
print("🍎 数苹果:")
for i in range(1, 6):
    print(f"    第{i}个苹果")

# 🎯 小挑战：用循环画三角形
print()
print("📐 三角形:")
for i in range(1, 5):
    for j in range(i):
        print("*", end="")
    print()
