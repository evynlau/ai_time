# Day 09 课后练习题 - 循环练习
print("练习 1: 数数")

# 数 1 到 10
print("🔢 数数:")
for i in range(1, 11):
    print(f"   {i}")

# 🎯 挑战：数偶数
print("\n🔢 数偶数:")
for i in range(2, 11, 2):
    print(f"   {i}")

# 数 5 的倍数
print("\n🔢 数 5 的倍数:")
for i in range(5, 26, 5):
    print(f"   {i}")

# 反向数数
print("\n🎉 倒计时:")
for i in range(10, 0, -1):
    print(f"   {i} - 发射!")
