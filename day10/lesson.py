# Day 10: 图案打印练习
# 🎯 学习目标：用循环创建图形
#
# 📖 故事：用代码画画
# 我们能用 * 号画出形状

# ✨ 三角形
print("📐 画一个三角形:")
for i in range(1, 5):
    for j in range(i):
        print("*", end=" ")
    print()

print()

# 📦 正方形
print("📦 画一个正方形:")
for i in range(4):
    for j in range(4):
        print("■", end="")
    print()

print()

# 🌟 倒三角
print("📉 画一个倒三角:")
for i in range(5, 0, -1):
    for j in range(i):
        print("★", end=" ")
    print()

# 🎮 练习：画一个菱形
print("💎 画一个菱形:")
for i in range(1, 5):
    print(" " * (5-i) + "*" * (2*i - 1))
for i in range(3, 0, -1):
    print(" " * (5-i) + "*" * (2*i - 1))

# 试试！
print()
print("🎨 你试试：画一个金字塔")
for i in range(1, 4):
    print(" " * (3-i) + "▲" * i)
