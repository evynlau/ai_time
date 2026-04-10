# Day 17 课后练习题 - 嵌套循环
print("练习 1: 画矩阵")

# 画 4x4 矩阵
print("📱 4x4 矩阵:")
for i in range(4):
    for j in range(4):
        print("★", end=" ")
    print()

# 🎯 挑战：画乘法表
print("\n📊 乘法表 (1-5):")
for i in range(1, 6):
    for j in range(1, 6):
        result = i * j
        print(f"{result:2}", end=" ")
    print()

# 画钻石图案
print("\n💎 钻石图案:")
for i in range(1, 6):
    print(" " * (5-i) + "♦" * i)
for i in range(4, 0, -1):
    print(" " * (5-i) + "♦" * i)

# 画数字金字塔
print("\n⭐ 数字金字塔:")
for i in range(1, 5):
    print(" " * (4-i) + str(i) * i)
