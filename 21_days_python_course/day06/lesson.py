# Day 06: for 循环
# 🎯 学习目标：掌握 for 循环，让程序能重复执行代码
# 📅 适合年龄：12 岁 +
# ⏱️ 建议时长：40 分钟


# ==========================================
# Day 06: for 循环
# ==========================================

print("=" * 50)
print("        🐍 Python 编程入门课程 - Day 06        ")
print("               for 循环 - 重复执行")
print("=" * 50)
print()

# ==========================================
# 1. 为什么需要循环？
# ==========================================

print("📖 1. 为什么需要循环？")
print("-" * 50)
print()

print("想象你要重复写 100 次'我错了'，你会怎么写？")
print("❌ 方法 1: 写 100 行代码")
print("    print('我错了')")
print("    print('我错了')")
print("    ...（重复 98 次）")
print()

print("✅ 方法 2: 用循环!")
print("    for i in range(100):")
print("        print('我错了')")
print()

print("循环让程序能够重复执行代码，节省大量时间！")
print()

# ==========================================
# 2. for 循环的基本语法
# ==========================================

print("📖 2. for 循环的基本语法")
print("-" * 50)
print()

print("基本格式:")
print("  for 变量 in 序列:")
print("      要重复执行的代码")
print()

print("例子:")
print("  for i in [1, 2, 3, 4, 5]:")
print("      print(i)")
print()

# 实际演示
print("运行结果:")
for i in [1, 2, 3, 4, 5]:
    print(f"    {i}")
print()

print("分析:")
print(f"  i = 1  → print(1)")
print(f"  i = 2  → print(2)")
print(f"  i = 3  → print(3)")
print(f"  i = 4  → print(4)")
print(f"  i = 5  → print(5)")
print("  循环结束!")
print()

# ==========================================
# 3. range() 函数
# ==========================================

print("📖 3. range() 函数 - 生成数字序列")
print("-" * 50)
print()

print("range() 是用来生成数字序列的函数！")
print()

print("1️⃣ 基本用法：range(终点)")
print("   从 0 开始，到终点-1 结束")
print("   range(5) → 0, 1, 2, 3, 4")
print()

print("   示例:")
for i in range(5):
    print(f"      数字：{i}")
print()

print("2️⃣ 指定起点和终点：range(起点，终点)")
print("   包含起点，不包含终点")
print("   range(3, 8) → 3, 4, 5, 6, 7")
print()

print("   示例:")
for i in range(3, 8):
    print(f"      数字：{i}")
print()

print("3️⃣ 指定步长：range(起点，终点，步长)")
print("   包含起点，不包含终点，每次增加步长")
print("   range(0, 10, 2) → 0, 2, 4, 6, 8")
print()

print("   示例:")
for i in range(0, 10, 2):
    print(f"      数字：{i}")
print()

# ====================================
# 4. for 循环中的索引
# ==========================================

print("📖 4. enumerate() - 获取索引和值")
print("-" * 50)
print()

print("enumerate() 函数可以获取索引和值：")
print("  用于同时知道索引和列表内容")
print()

fruits = ["苹果", "香蕉", "橙子", "葡萄"]
print("列表：", fruits)
print()

for index, fruit in enumerate(fruits):
    print(f"  第 {index + 1} 个水果：{fruit}")
print()

print("注意：索引从 0 开始，所以是 index + 1")
print()

# ====================================
# 5. 嵌套循环
# ==========================================

print("📖 5. 嵌套循环 - for 套 for")
print("-" * 50)
print()

print("一个循环内部再使用循环!")
print()

print("示例：打印乘法表")
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i}×{j}={i*j:2d}", end="  ")
    print()
print()

print("分析：")
print("  外层循环：i = 1, 2, 3, 4, 5")
print("  内层循环：j = 1, 2, 3, 4, 5")
print("  对于每个 i，j 都会遍历完整的 1-5")
print()

# ====================================
# 6. Python 小贴士
# ==========================================

print("=" * 50)
print("       💡 Python 小贴士")
print("=" * 50)
print()
print("1. for 循环用于已知迭代次数的场景")
print("2. range() 的终点是开区间，不包含终点本身")
print("3. 嵌套循环的复杂度是乘积关系")
print("4. 使用 enumerate() 可以同时获取索引和值")
print("5. 使用 break 可以跳出循环")
print("6. 使用 continue 可以跳过本次循环")
print("7. 循环的 else 子句仅在循环正常结束时执行")
print()

# ====================================
# 7. 实践练习
# ==========================================

print("=" * 50)
print("       📝 实践练习：数字统计游戏")
print("=" * 50)
print()
print("🎯 任务：创建一个数字统计和图案绘制程序")
print()
print("要求:")
print("  1. 用循环打印 1 到 10 的累加和")
print("  2. 用循环打印三角形图案")
print("  3. 找出 1 到 100 中所有偶数")
print()

print("示例答案:")
print("-" * 40)
print("# 1. 累加和")
print("total = 0")
print("for i in range(1, 11):")
print("    total += i")
print("print(f'1 到 10 的和：{total}')")
print()
print("# 2. 打印三角形")
print("#    *")
print("#   ***")
print("#  *****")
print("# *******")
print("for i in range(1, 5):")
print("    print(' ' * (4-i) + '*' * (2*i-1))")
print()
print("# 3. 找出偶数")
print("evens = []")
print("for i in range(1, 101):")
print("    if i % 2 == 0:")
print("        evens.append(i)")
print("print(f'偶数：{evens}')")
print()
print("=" * 50)
print("       📝 额外练习：斐波那契数列")
print("=" * 50)
print("任务：生成前 10 个斐波那契数")
print("提示：前两个数是 0, 1，之后每个数是前两个数的和")
print()

# ====================================
# 8. Day 06 总结
# ==========================================

print("=" * 50)
print("       📋 Day 06 总结")
print("=" * 50)
print()
print("今天我们学会了:")
print("  ✅ for 循环 - 重复执行代码")
print("  ✅ range() 函数 - 生成数字序列")
print("  ✅ enumerate() - 获取索引和值")
print("  ✅ 嵌套循环 - for 套 for")
print("  ✅ break 和 continue")
print()

print("=" * 50)
print("       🎉 Day 06 完成！")
print("=" * 50)
print()
print("太棒了！你的程序现在会重复执行代码了！")
print("明天进行基础复习，完成第一周的总结！")
print()
print("===============================================")
print("     💪 继续加油！学习进度：6/21 天完成！")
print("===============================================")
