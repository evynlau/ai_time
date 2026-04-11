# Day 05: 条件语句
# 🎯 学习目标：理解 if-elif-else，让程序能够做判断
# 📅 适合年龄：12 岁 +
# ⏱️ 建议时长：40 分钟


# ==========================================
# Day 05: 条件语句 - if-elif-else
# ==========================================

print("=" * 50)
print("        🐍 Python 编程入门课程 - Day 05        ")
print("             条件语句 - 程序做判断")
print("=" * 50)
print()

# ==========================================
# 1. if 语句
# ==========================================

print("📖 1. 什么是 if 语句？")
print("-" * 50)
print()

print("if 语句让程序能够做判断，根据条件执行不同的代码")
print()

print("基本用法:")
print("  if 条件:")
print("      要执行的代码")
print()

print("示例:")
score = 95
print(f"score = {score}")
print()
print("if score >= 90:")
print("    print('优秀！')")
print()
print("判断: 5 >= 90?", 95 >= 90)
print("结果：输出 '优秀！'")
print()

# ==========================================
# 2. if-else 语句
# ==========================================

print("📖 2. if-else 语句")
print("-" * 50)
print()

print("if-else 提供两个选择:")
print("  if 条件:")
print("      条件为真时执行的代码")
print("  else:")
print("      条件为假时执行的代码")
print()

print("示例:")
temperature = 35
print(f"temperature = {temperature}")
print()

if temperature >= 30:
    print("🌞 天气很热！")
else:
    print("❄️ 天气很冷！")
print()

print(f"判断：{temperature} >= 30 是 {temperature >= 30}")
print("结果：输出 '🌞 天气很热！'")
print()

# ==========================================
# 3. if-elif-else 语句
# ==========================================

print("📖 3. if-elif-else 语句 - 多个选择")
print("-" * 50)
print()

print("elif 是 else if 的缩写，可以判断多个条件:")
print()

print("基本用法:")
print("  if 条件 1:")
print("      条件 1 为真时执行")
print("  elif 条件 2:")
print("      条件 1 为假，条件 2 为真时执行")
print("  else:")
print("      所有条件都为假时执行")
print()

print("示例 - 成绩判断:")
score = 85
print(f"score = {score}")
print()

if score >= 90:
    print("优秀！（90 分以上）")
elif score >= 70:
    print("良好！（70-89 分）")
else:
    print("及格！（60-69 分）")

print()
print(f"判断：{score} >= 90 是 {score >= 90}")
print(f"判断：{score} >= 70 是 {score >= 70}")
print("结果：输出 '良好！'")
print()

# ====================================
# 4. 实际案例
# ==========================================

print("📖 4. 实际案例：天气判断")
print("-" * 50)
print()

temperature = 25
print(f"今天气温：{temperature}°C")
print()

if temperature > 30:
    print("🌍 天气热！穿短袖吧")
elif temperature > 20:
    print("☀️ 天气舒服！穿短袖")
elif temperature > 10:
    print("🌡️ 天气凉爽！穿长袖")
else:
    print("🥶 天气冷！穿厚衣服")
print()

print("逻辑分析:")
print(f"  {temperature} > 30 是 {temperature > 30}")
print(f"  {temperature} > 20 是 {temperature > 20}")
print("结论：输出'☀️ 天气舒服！穿短袖'")
print()

print("📖 实际案例：年龄判断")
print("-" * 50)
print()

age = 15
print(f"你的年龄：{age} 岁")
print()

if age < 12:
    print("🎮 你是小学生")
elif age < 18:
    print("🎒 你是中学生")
else:
    print("🎓 你是成年人")
print()

print(f"判断：{age} < 12 是 {age < 12}")
print(f"判断：{age} < 18 是 {age < 18}")
print("结论：输出'🎒 你是中学生'")
print()

# ====================================
# 5. 嵌套 if
# ==========================================

print("📖 5. 嵌套 if - if 在里面再嵌套 if")
print("-" * 50)
print()

print("if 语句可以在另一个 if 内部使用:")
print()

is_saturday = True
has_homework = False

print(f"is_saturday = {is_saturday}")
print(f"has_homework = {has_homework}")
print()

if is_saturday:
    if has_homework:
        print("周末但有作业，写作业吧")
    else:
        print("周末且没有作业，可以玩耍！")
else:
    if has_homework:
        print("上学且有作业，要认真写作业")
    else:
        print("上学没有作业，可以休息")

print()
print("分析:")
print(f"  is_saturday = True")
print(f"  has_homework = False")
print("外层 if: True 为真 → 进入第一个分支")
print("内层 if: False 为假 → 执行 else")
print("结论：输出'周末且没有作业，可以玩耍！'")
print()

# ====================================
# 6. Python 小贴士
# ==========================================

print("=" * 50)
print("       💡 Python 小贴士")
print("=" * 50)
print()
print("1. if 语句后面的条件必须为 True 或 False")
print("2. if 语句后的代码块要缩进（通常 4 个空格）")
print("3. elif 可以有多个，用来判断多个条件")
print("4. else 必须放在最后，没有条件")
print("5. if-elif-else 就像选择题，按顺序判断")
print("6. 缩进非常重要！缩进代表代码块")
print("7. 可以嵌套 if 语句")
print()

# ====================================
# 7. 实践练习
# ====================================

print("=" * 50)
print("       📝 实践练习：成绩判断系统")
print("=" * 50)
print()
print("🎯 任务：创建一个成绩判断系统")
print()
print("要求:")
print("  1. 输入成绩（0-100 之间）")
print("  2. 判断等级:")
print("      - 90 分以上：优秀")
print("      - 80-89 分：良好")
print("      - 70-79 分：中等")
print("      - 60-69 分：及格")
print("      - 60 分以下：不及格")
print()

# 示例代码
print("示例答案:")
print("-" * 40)
print("score = int(input('请输入成绩：'))")
print()
print("if score >= 90:")
print("    print('优秀！🏆')")
print("elif score >= 80:")
print("    print('良好！👍')")
print("elif score >= 70:")
print("    print('中等！👌')")
print("elif score >= 60:")
print("    print('及格！❤️')")
print("else:")
print("    print('不及格！💪 加油！')")
print()
print("=" * 50)
print("       📝 额外练习：判断奇偶数")
print("=" * 50)
print()
print("任务：判断一个数字是奇数还是偶数")
print("提示：使用取余运算符 %")
print()

# ====================================
# 8. Day 05 总结
# ==========================================

print("=" * 50)
print("       📋 Day 05 总结")
print("=" * 50)
print()
print("今天我们学会了:")
print("  ✅ if 语句 - 条件判断")
print("  ✅ if-else 语句 - 二选一")
print("  ✅ if-elif-else 语句 - 多个选择")
print("  ✅ 嵌套 if 语句 - if 里套 if")
print("  ✅ 逻辑分析能力")
print()

print("=" * 50)
print("       🎉 Day 05 完成！")
print("=" * 50)
print()
print("太好了！你的程序现在会做判断了！")
print("明天学习 for 循环，让程序能够重复执行！")
print()
print("===============================================")
print("     💪 继续加油！学习进度：5/21 天完成！")
print("===============================================")
