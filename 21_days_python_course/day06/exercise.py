# Day 06: for 循环 - 练习
print("=" * 50)
print("       📝 Day 06 练习：循环实战")
print("=" * 50)
print()

# 练习 1: 计算累加和
print("🎯 练习 1: 计算 1 到 100 的累加和")
print("-" * 40)
print()

total = 0
for i in range(1, 101):
    total += i

print(f"1 到 100 的和：{total}")
print()

# 练习 2: 打印图案
print("=" * 50)
print("       🎨 练习 2: 打印图案")
print("=" * 50)
print()

# 2a. 三角形图案
print("2a. 打印三角形:")
print()
for i in range(1, 6):
    for j in range(5, i, -1):
        print(end=" ")
    for j in range(1, 2*i):
        print("*", end="")
    print()
print()

# 2b. 矩形图案
print("2b. 打印矩形:")
for i in range(5):
    print("*" * 7)
print()

# 2c. 菱形图案
print("2c. 打印菱形:")
for i in range(1, 5):
    print(" " * (4-i), end="")
    print("*" * (2*i - 1))
for i in range(3, 0, -1):
    print(" " * (4-i), end="")
    print("*" * (2*i - 1))
print()

# 练习 3: 数字处理
print("=" * 50)
print("       🔢 练习 3: 数字处理")
print("=" * 50)
print()

print("3a. 找出 1 到 50 中所有 3 的倍数:")
multiples_of_3 = []
for i in range(1, 51):
    if i % 3 == 0:
        multiples_of_3.append(i)
print(f"   结果：{multiples_of_3}")
print()

print("3b. 找出 1 到 100 中所有奇数的和:")
sum_odds = 0
count_odds = 0
for i in range(1, 101):
    if i % 2 == 1:
        sum_odds += i
        count_odds += 1
print(f"   奇数之和：{sum_odds}")
print(f"   奇数个数：{count_odds}")
print()

# 练习 4: 嵌套循环
print("=" * 50)
print("       🔁 练习 4: 嵌套循环 - 乘法表")
print("=" * 50)
print()

print("打印简单的乘法表:")
for i in range(1, 6):
    for j in range(1, 6):
        result = i * j
        print(f"{i}×{j:2d}={result:2d}", end="  ")
    print()
print()

# 练习 5: 斐波那契数列
print("=" * 50)
print("       🌿 练习 5: 斐波那契数列")
print("=" * 50)
print()

print("前 10 个斐波那契数:")
fib = [0, 1]
for i in range(8):
    fib.append(fib[i] + fib[i+1])

for i, num in enumerate(fib[:10]):
    print(f"  第{i+1}个数：{num}")

print()
print("公式：每个数 = 前两个数的和")
print("0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...")
print()

# 综合练习
print("=" * 50)
print("       🎨 综合任务：打印字母表")
print("=" * 50)
print()

# 用循环打印字母
letters = 'abcdefghijklmnopqrstuvwxyz'
print("大写字母表:")
for char in letters.upper():
    print(f"  {char}", end="  ")
    if (ord(char) - ord('A')) % 5 == 4:
        print()
print()

print("小写字母表:")
for char in letters:
    print(f"  {char}", end="  ")
    if (ord(char) - ord('a')) % 5 == 4:
        print()

print()
print("=" * 50)
print("       ✅ 所有练习完成！")
print("=" * 50)
print()
print("做得很好！你已经掌握了 for 循环的基本用法！")
print("继续加油，明天进行第一周的复习！🎉")
