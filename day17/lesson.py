# Day 17: 嵌套循环
# 🎯 学习目标：理解循环套循环
#
# 📖 故事：矩阵
# 每个点都有行和列编号
#
# 像这样：
# ● ● ●
# ● ● ●
# ● ● ●

# 画一个 3x3 的矩阵
print("📱 3x3 矩阵:")
for i in range(3):
    for j in range(3):
        print("●", end=" ")
    print()

# 🎮 练习：画矩形
print()
print("📐 矩形:")
for row in range(4):
    for col in range(6):
        print("■", end="")
    print()

# 画三角形数字
print()
print("🔢 三角形数字:")
for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end="")
    print()

# 🎯 小挑战：画一个乘法表
print()
print("📊 乘法表:")
for i in range(1, 4):
    for j in range(1, 4):
        result = i * j
        print(f"{result:2}", end=" ")
    print()
