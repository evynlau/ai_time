# Day 05: 条件语句 - 练习
print("=" * 50)
print("       📝 Day 05 练习 1: 成绩判断系统")
print("=" * 50)
print()

# 练习 1: 成绩判断
print("🎯 任务：创建成绩判断系统")
print()

score = 88
print(f"成绩：{score}")
print()

if score >= 90:
    print("优秀！🏆")
elif score >= 80:
    print("良好！👍")
elif score >= 70:
    print("中等！👌")
elif score >= 60:
    print("及格！❤️")
else:
    print("不及格！💪 加油！")

print()
print("=" * 50)

# 练习 2: 判断奇偶数
print()
print("🎯 练习 2: 判断数字是奇数还是偶数")
print()

number = 28
print(f"数字：{number}")
print()

# 使用取余运算符 % 判断
if number % 2 == 0:
    print(f"⚪ {number} 是偶数")
else:
    print(f"⚫ {number} 是奇数")
print()

# 尝试其他数字
print("尝试其他数字:")
test_numbers = [15, 32, 47, 64, 81]

for num in test_numbers:
    status = "偶数" if num % 2 == 0 else "奇数"
    marker = "⚪" if num % 2 == 0 else "⚫"
    print(f"  {marker} {num} 是 {status}")
print()

# 练习 3: 判断年龄阶段
print("=" * 50)
print("       📝 练习 3: 年龄阶段判断")
print("=" * 50)
print()

age = 16
print(f"年龄：{age} 岁")
print()

if age < 12:
    print("🎮 你是小学生")
elif age < 18:
    print("🎒 你是中学生")
elif age < 65:
    print("🎓 你是成年人")
else:
    print("👴 你是老年人")
print()

# 练习 4: 天气判断
print("=" * 50)
print("       📝 练习 4: 天气判断")
print("=" * 50)
print()

temperature = 22
print(f"当前气温：{temperature}°C")
print()

if temperature > 30:
    print("🌡️ 天气热！建议穿短袖，开空调")
elif temperature > 20:
    print("☀️ 天气舒适！适合户外活动")
elif temperature > 10:
    print("🍂 天气凉爽！建议穿长袖")
else:
    print("❄️ 天气寒冷！穿厚衣服")
print()

# 综合练习
print("=" * 50)
print("       🎨 综合练习")
print("=" * 50)
print()

name = "小明"
age = 14
score = 85

print(f"姓名：{name}")
print(f"年龄：{age} 岁")
print(f"成绩：{score}")
print()

if age < 12:
    school_type = "小学"
elif age < 18:
    school_type = "中学"
else:
    school_type = "大学"

print(f"学校类型：{school_type}")
print()

if score >= 90:
    grade = "优秀"
elif score >= 80:
    grade = "良好"
elif score >= 70:
    grade = "中等"
elif score >= 60:
    grade = "及格"
else:
    grade = "不及格"

print(f"成绩等级：{grade}")
print()

print("=" * 50)
print("       ✅ 所有练习完成！")
print("=" * 50)
