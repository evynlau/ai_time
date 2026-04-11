# Day 03: 运算符 - 练习
print("=" * 50)
print("       📝 Day 03 练习：计算年龄相关")
print("=" * 50)
print()

# 练习 1: 基础运算计算
print("🎯 练习 1: 计算你的年龄相关")
print("-" * 40)
print()

age = 13

print(f"我今年 {age} 岁")
print()

print("1️⃣ 出生年份:")
birth_year = 2026 - age
print(f"   我出生在 {birth_year} 年")
print()

print("2️⃣ 下一个生日:")
next_age = age + 1
print(f"   下一个生日我将 {next_age} 岁")
print()

print("3️⃣ 5 年后:")
five_years_later = age + 5
print(f"   5 年后我将 {five_years_later} 岁")
print()

print("4️⃣ 比较:")
print(f"   {next_age} > {age} 吗？{next_age > age}")
print()

# 练习 2: 计算体重
print("=" * 50)
print("       📝 练习 2: 计算体重相关")
print("=" * 50)
print()

weight = 45  # 假设体重

print(f"我现在的体重是：{weight} 公斤")
print()

print("1️⃣ 增加 5 公斤:")
new_weight = weight + 5
print(f"   增加 5 公斤后：{new_weight} 公斤")
print()

print("2️⃣ 减少 3 公斤:")
slim_weight = weight - 3
print(f"   减少 3 公斤后：{slim_weight} 公斤")
print()

print("3️⃣ 是现在的 2 倍吗:")
print(f"   {new_weight} / {weight} = {new_weight / weight}")
print()

print("4️⃣ new_weight = 2 × weight 吗:")
print(f"   {new_weight} = {2 * weight} 吗？{new_weight == 2 * weight}")
print()

# 练习 3: 简单逻辑判断
print("=" * 50)
print("       📝 练习 3: 逻辑判断")
print("=" * 50)
print()

is_weekend = True
has_homework = False

print("判断周末是否有作业:")
print(f"是周末吗？{is_weekend}")
print(f"有作业吗？{has_homework}")
print()

print("可以玩游戏吗？(周末且没有作业)")
can_play = is_weekend and (not has_homework)
print(f"   可以玩游戏：{can_play}")
print()

print("可以做点自己喜欢的事？(周末或有作业)")
can_chill = is_weekend or has_homework
print(f"   可以放松：{can_chill}")
print()

print("=" * 50)
print("       ✅ 所有练习完成！")
print("=" * 50)
print()

# 挑战任务
print("🎨 挑战任务：创建一个完整的数学计算")
print("=" * 50)
print("例如：计算你的身高、体重、年龄的综合信息")
print()

# 你的挑战代码在这里
height = 1.60
weight = 48

bmi = weight / (height ** 2)
print(f"📊 身体指标:")
print(f"  身高：{height}米")
print(f"  体重：{weight}公斤")
print(f"  BMI: {bmi:.2f}")
print(f"  BMI < 25 吗？{bmi < 25}")
print()

print("挑战完成！你真棒！🎉")
