# Day 03: 运算符 - 答案
print("=" * 50)
print("       📝 Day 03 练习 1: 完整答案示例")
print("=" * 50)
print()

# 示例答案：年龄计算
age = 13

print(f"🎂 今年 {age} 岁")
print()

# 1️⃣ 出生年份
birth_year = 2026 - age
print(f"我出生在 {birth_year} 年")
print()

# 2️⃣ 下一个生日
next_age = age + 1
print(f"下一个生日我将 {next_age} 岁")
print()

# 3️⃣ 5 年后
five_years_later = age + 5
print(f"5 年后我将 {five_years_later} 岁")
print()

# 4️⃣ 比较
print(f"{next_age} > {age} 吗？{next_age > age}")
print(f"{five_years_later} > {next_age} 吗？{five_years_later > next_age}")
print()

# 练习 2: 体重计算
print("=" * 50)
print("       📝 练习 2: 体重计算完整答案")
print("=" * 50)
print()

weight = 45

print(f"现在体重：{weight} 公斤")
print()
print("增加 5 公斤后：{0} 公斤".format(weight + 5))
print(f"减少 3 公斤后：{weight - 3} 公斤")
print(f"是现在的 2 倍吗？{weight + 5 == 2 * weight}")
print()

# 练习 3: 逻辑判断完整答案
print("=" * 50)
print("       📝 练习 3: 逻辑判断完整答案")
print("=" * 50)
print()

is_weekend = True
has_homework = False

print(f"是周末吗？{is_weekend}")
print(f"有作业吗？{has_homework}")
print()

can_play = is_weekend and (not has_homework)
print(f"可以玩游戏？{can_play}")
print()

can_chill = is_weekend or has_homework
print(f"可以放松？{can_chill}")
print()

# 挑战任务完整答案
print("=" * 50)
print("       🎨 挑战任务：BMI 计算器完整答案")
print("=" * 50)
print()

height = 1.60
weight = 48

bmi = weight / (height ** 2)
print(f"BMI = {bmi:.2f}")
print()

if bmi < 18.5:
    print("状态：偏瘦")
elif bmi < 25:
    print("状态：正常")
elif bmi < 30:
    print("状态：超重")
else:
    print("状态：肥胖")

print()
print("=" * 50)
print("       ✅ 所有练习完成！")
print("=" * 50)
print()
print("太棒了！你已经掌握了运算符的使用方法！")
print("继续加油，明天学习输入和输出！🎉")
