# Day 05: 条件语句 - 答案
print("=" * 50)
print("       📝 Day 05: 完整答案示例")
print("=" * 50)
print()

# 练习 1: 成绩判断完整答案
print("🎯 练习 1: 成绩判断完整答案")
print("-" * 50)
print()

score = 88
print(f"成绩：{score}")
print()

if score >= 90:
    print("优秀！🏆 (90 分以上)")
elif score >= 80:
    print("良好！👍 (80-89 分)")
elif score >= 70:
    print("中等！👌 (70-79 分)")
elif score >= 60:
    print("及格！❤️ (60-69 分)")
else:
    print("不及格！💪 (60 分以下)")

print()
print("分析:")
print(f"  {score} >= 90 是 {score >= 90}")
print(f"  {score} >= 80 是 {score >= 80}")
print("结论：输出'良好！👍'")
print()

# 练习 2: 奇偶数判断完整答案
print("=" * 50)
print("       📝 练习 2: 奇偶数判断完整答案")
print("=" * 50)
print()

test_numbers = [15, 32, 47, 64, 81, 100, 73]

print("判断 1-100 内的数字:")
print()

for num in test_numbers:
    if num % 2 == 0:
        marker = "⚪"
        result = "偶数"
    else:
        marker = "⚫"
        result = "奇数"
    
    print(f"  {marker} {num} 是 {result}")
print()

print("=" * 50)
print("       📋 总结")
print("=" * 50)
print()

print("规则:")
print("  - 除以 2 余 0 的是偶数")
print("  - 除以 2 余数不是 0 的是奇数")
print()
print(f"  15 % 2 = {15 % 2}   (奇数)")
print(f"  32 % 2 = {32 % 2}   (偶数)")
print(f"  47 % 2 = {47 % 2}   (奇数)")
print(f"  64 % 2 = {64 % 2}   (偶数)")
print()

# 练习 3: 年龄阶段判断
print("=" * 50)
print("       📝 练习 3: 年龄阶段判断完整答案")
print("=" * 50)
print()

ages = [8, 16, 25, 70]

for age in ages:
    print(f"年龄：{age} 岁")
    
    if age < 12:
        stage = "小学"
    elif age < 18:
        stage = "中学"
    elif age < 65:
        stage = "成年"
    else:
        stage = "老年"
    
    print(f"  → {stage}")
    print()

# 综合练习答案
print("=" * 50)
print("       🎨 综合练习完整答案")
print("=" * 50)
print()

# 示例用户
username = "小红"
user_age = 13
userscore = 92

print(f"姓名：{username}")
print(f"年龄：{user_age} 岁")
print(f"成绩：{userscore}")
print()

# 判断学校类型
if user_age < 12:
    school_type = "小学"
elif user_age < 18:
    school_type = "中学"
else:
    school_type = "大学"

print(f"🏫 学校类型：{school_type}")

# 判断成绩等级
if userscore >= 90:
    grade = "优秀"
    symbol = "🏆"
elif userscore >= 80:
    grade = "良好"
    symbol = "👍"
elif userscore >= 70:
    grade = "中等"
    symbol = "👌"
elif userscore >= 60:
    grade = "及格"
    symbol = "❤️"
else:
    grade = "不及格"
    symbol = "💪 加油"

print(f"📊 成绩等级：{symbol} {grade}")
print()

print("=" * 50)
print("       ✅ 所有练习完成！")
print("=" * 50)
print()

print("做得很好！你已经掌握了条件语句的使用！")
print("继续加油，明天学习 for 循环！🎉")
