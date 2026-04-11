# Day 06: for 循环 - 答案
print("=" * 50)
print("       📝 Day 06: 完整答案示例")
print("=" * 50)
print()

# 练习 1: 计算累加和
print("🎯 练习 1: 计算累加和完整答案")
print("-" * 40)
print()

total = 0
for i in range(1, 101):
    total += i

print(f"1 到 100 的和：{total}")
print()

print("验证：使用公式 n * (n+1) / 2")
n = 100
formula_result = n * (n + 1) // 2
print(f"公式：{n} * ({n}+1) / 2 = {formula_result}")
print(f"两种方法结果一致！✅")
print()

# 练习 2a: 打印三角形
print("=" * 50)
print("       🎨 练习 2a: 三角形完整答案")
print("=" * 50)
print()

print("打印一个 5 层的三角形:")
print()
for i in range(1, 6):
    # 前面的空格
    for j in range(5, i, -1):
        print(end=" ")
    # 星号
    for j in range(1, 2*i):
        print("*", end="")
    print()
print()

# 练习 2b: 打印矩形
print("=" * 50)
print("       🎨 练习 2b: 矩形完整答案")
print("=" * 50)
print()

print("打印一个 5 行 7 列的矩形:")
print()
for i in range(5):
    print("*" * 7)
print()

# 练习 2c: 菱形
print("=" * 50)
print("       🎨 练习 2c: 菱形完整答案")
print("=" * 50)
print()

print("打印一个菱形:")
print()
for i in range(1, 5):
    print(" " * (4-i), end="")
    print("*" * (2*i - 1))
for i in range(3, 0, -1):
    print(" " * (4-i), end="")
    print("*" * (2*i - 1))
print()

# 练习 3a: 3 的倍数
print("=" * 50)
print("       🔢 练习 3a: 3 的倍数完整答案")
print("=" * 50)
print()

multiples_of_3 = []
for i in range(1, 51):
    if i % 3 == 0:
        multiples_of_3.append(i)

print(f"1 到 50 中 3 的倍数：{multiples_of_3}")
print(f"共 {len(multiples_of_3)} 个数字")
print()

# 练习 3b: 奇数和
print("=" * 50)
print("       🔢 练习 3b: 奇数和完整答案")
print("=" * 50)
print()

sum_odds = 0
count_odds = 0
for i in range(1, 101):
    if i % 2 == 1:
        sum_odds += i
        count_odds += 1

print(f"1 到 100 中奇数的和：{sum_odds}")
print(f"1 到 100 中共有 {count_odds} 个奇数")
print()

print("验证：1, 3, 5, ..., 99")
print("  首项 = 1, 末项 = 99, 项数 = 50")
print("  和 = (1 + 99) * 50 / 2 = 2500")
print(f"  计算结果：{sum_odds}")
print(f"  ✅ 结果匹配！")
print()

# 练习 4: 乘法表
print("=" * 50)
print("       🔁 练习 4: 乘法表完整答案")
print("=" * 50)
print()

print("1 到 5 的乘法表:")
print()
for i in range(1, 6):
    for j in range(1, 6):
        result = i * j
        print(f"{i}×{j:2d}={result:2d}", end="  ")
    print()
print()

# 练习 5: 斐波那契
print("=" * 50)
print("       🌿 练习 5: 斐波那契完整答案")
print("=" * 50)
print()

print("前 10 个斐波那契数:")
print()
fib = [0, 1]
for i in range(8):
    fib.append(fib[i] + fib[i+1])

for i, num in enumerate(fib[:10]):
    marker = "→" if i < 2 else "⬡"
    print(f"  {marker} 第{i+1}个数：{num}")
print()

# 综合任务答案
print("=" * 50)
print("       🎨 综合任务：字母表完整答案")
print("=" * 50)
print()

print("大写字母表:")
for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    print(f"  {char}", end="  ")
    if (ord(char) - ord('A')) % 5 == 4:
        print()
print()

print("小写字母表:")
for char in 'abcdefghijklmnopqrstuvwxyz':
    print(f"  {char}", end="  ")
    if (ord(char) - ord('a')) % 5 == 4:
        print()

print()
print("=" * 50)
print("       ✅ 所有练习完成！")
print("=" * 50)
print()

print("做得非常出色！你已经掌握了 for 循环的所有基础知识！")
print("继续加油，明天进行第一周的总结复习！🎉")
print()

print("=" * 60)
print("       📊 Day 06 知识点总结")
print("=" * 60)
print()
print("✅ for 循环语法")
print("✅ range() 函数")
print("✅ enumerate() 函数")
print("✅ 嵌套循环")
print("✅ loop 中的 break 和 continue")
print("✅ 图案打印技巧")
print()
print("你已经完成了第一周编程的基础训练！💪")
