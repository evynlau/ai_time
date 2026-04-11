# Day 03: 运算符
# 🎯 学习目标：掌握算术运算符和比较运算符
# 📅 适合年龄：12 岁 +
# ⏱️ 建议时长：40 分钟


# ==========================================
# Day 03: 运算符 - 数学魔法棒
# ==========================================

print("=" * 50)
print("        🐍 Python 编程入门课程 - Day 03        ")
print("              运算符 - 数学魔法棒")
print("=" * 50)
print()

# ==========================================
# 1. 算术运算符
# ==========================================

print("📖 1. 算术运算符 - 基本数学运算")
print("-" * 50)
print()

a = 10
b = 3

print(f"定义变量：a = {a}, b = {b}")
print()

print("🔢 加法 (+)")
print(f"  {a} + {b} = {a + b}")
print()

print("➖ 减法 (-)")
print(f"  {a} - {b} = {a - b}")
print()

print("✖️  乘法 (*)")
print(f"  {a} × {b} = {a * b}")
print()

print("➗ 除法 (/)")
result = a / b
print(f"  {a} ÷ {b} = {result}")
print()

print("➗ 整除 (//)")
result = a // b
print(f"  {a} // {b} = {result} (向下取整)")
print()

print("🔢 取余 (%)")
result = a % b
print(f"  {a} % {b} = {result} (求余数)")
print()

print("⏫ 幂运算 (**)")
result = a ** 2
print(f"  {a} ** 2 = {result} (a 的平方)")
print()

# ==========================================
# 2. 比较运算符
# ==========================================

print("📖 2. 比较运算符 - 比较大小")
print("-" * 50)
print()

x = 8
y = 5

print(f"定义变量：x = {x}, y = {y}")
print()

print("⚖️ 大于 (>)")
print(f"  {x} > {y} = {x > y}")
print()

print("⚖️ 小于 (<)")
print(f"  {y} < {x} = {y < x}")
print()

print("⚖️ 等于 (==)")
print(f"  {x} == {y} = {x == y}")
print()

print("⚖️ 不等于 (!=)")
print(f"  {x} != {y} = {x != y}")
print()

print("⚖️ 大于等于 (>=)")
print(f"  {x} >= {x} = {x >= x}")
print()

print("⚖️ 小于等于 (<=)")
print(f"  {y} <= {x} = {y <= x}")
print()

# ==========================================
# 3. 逻辑运算符
# ==========================================

print("📖 3. 逻辑运算符 - 布尔运算")
print("-" * 50)
print()

print("🔗 and - 并且")
print(f"  True and True = {True and True}")
print(f"  True and False = {True and False}")
print()

print("🔗 or - 或者")
print(f"  True or False = {True or False}")
print(f"  False or False = {False or False}")
print()

print("🔗 not - 非")
print(f"  not True = {not True}")
print(f"  not False = {not False}")
print()

# ====================================
# 4. 实际应用
# ==========================================

print("📖 4. 实际应用：简易计算器")
print("-" * 50)
print()

print("让我们做一个完整的计算器:")
print()

num1 = 25
num2 = 5

print(f"f'{num1} 个苹果，分给 {num2} 个朋友:')")
print(f"  🍎 每人分到：{num1 // num2} 个")
print(f"  🍎 剩余：{num1 % num2} 个")
print()

# ====================================
# 5. Python 小贴士
# ==========================================

print("=" * 50)
print("       💡 Python 小贴士")
print("=" * 50)
print()
print("1. 除法(/)会返回浮点数，整除(//)返回整数")
print("2. 取余(%)返回除法的余数")
print("3. 幂运算(**)是 x 的 n 次方，如 2**3 = 8")
print("4. 比较运算符返回 True 或 False")
print("5. and 必须两个都为 True 才返回 True")
print("6. or 只要有一个为 True 就返回 True")
print("7. not 会取反，True 变 False")
print()

# ====================================
# 6. 实践练习
# ==========================================

print("=" * 50)
print("       📝 实践练习：简易数学游戏")
print("=" * 50)
print()
print("🎯 任务：用运算符计算年龄相关的问题")
print()
print("要求:")
print("  1. 创建一个年龄变量（比如 12）")
print("  2. 计算你出生那年的年龄（假设现在是 2026 年）")
print("  3. 计算你的下一个生日年龄（+1 岁）")
print("  4. 比较：下一个生日年龄 > 当前年龄？")
print()

print("示例答案:")
print("-" * 40)
print("age = 12")
print()
print("birth_year = 2026 - age")
print("print(f'我出生在 {birth_year} 年')")
print()
print("next_year_age = age + 1")
print("print(f'下一个生日我将 {next_year_age} 岁')")
print()
print("print(f'{next_year_age} > {age} 吗？{next_year_age > age}')")
print()

# ====================================
# 7. Day 03 总结
# ==========================================

print("=" * 50)
print("       📋 Day 03 总结")
print("=" * 50)
print()
print("今天我们学会了:")
print("  ✅ 算术运算符：+ - * / // % **")
print("  ✅ 比较运算符：> < == != >= <=")
print("  ✅ 逻辑运算符：and or not")
print("  ✅ 运算符的优先级")
print()

print("=" * 50)
print("       🎉 Day 03 完成！")
print("=" * 50)
print()
print("太棒了！你现在会做数学运算了！")
print("明天学习输入和输出，可以让程序和人互动！")
print()
print("===============================================")
print("     💪 继续加油！学习进度：3/21 天完成！")
print("===============================================")
