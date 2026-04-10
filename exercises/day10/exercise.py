# Day 10 课后练习题 - 图案练习
print("练习 1: 画三角形")

# ✨ 三角形
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()

print("\n🎯 挑战：画正方形")
for i in range(5):
    for j in range(5):
        print("■", end="")
    print()

# 画矩形
print("\n📐 画矩形 (6x4):")
for i in range(4):
    for j in range(6):
        print("□", end="")
    print()

# 阶梯图案
print("\n🪜 画阶梯:")
for i in range(1, 6):
    print(" " * (5-i) + "*" * i)

# 金字塔
print("\n⭐ 画金字塔:")
for i in range(1, 6):
    print(" " * (5-i) + "⭐" * i)
