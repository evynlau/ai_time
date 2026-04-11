# Day 04: 输入与输出 - 练习
print("=" * 50)
print("       📝 Day 04 练习：交互式问答程序")
print("=" * 50)
print()

print("🎯 任务：创建一个生日计算程序")
print()

# 第一步：获取用户姓名
print("📝 步骤 1: 获取姓名")
name = input("你叫什么名字？")
print(f"你好，{name}!")
print()

# 第二步：获取年龄
print("📝 步骤 2: 获取年龄")
print("注意：输入的年龄会被当作字符串处理")
age_str = input("你今年几岁？")
age_int = int(age_str)
print(f"你输入的年龄是 {age_int} 岁")
print()

# 第三步：计算
print("📝 步骤 3: 进行计算")
print()

# 5 年后的年龄
future_age = age_int + 5
print(f"5 年后你将 {future_age} 岁")
print()

# 下一个生日
next_birthday = age_int + 1
print(f"下一个生日，你将 {next_birthday} 岁")
print()

# 出生年份
birth_year = 2026 - age_int
print(f"你出生在 {birth_year} 年")
print()

# 第四步：显示总结
print("📝 步骤 4: 显示总结")
print()
print(f"=== {name} 的个人信息 ===")
print(f"姓名：{name}")
print(f"今年：{age_int} 岁")
print(f"5 年后：{future_age} 岁")
print(f"出生年份：{birth_year} 年")
print("=" * 30)
print()

# 练习 2: 重量计算
print("=" * 50)
print("       📝 练习 2: 体重计算")
print("=" * 50)
print()

weight = input("你现在的体重是多少公斤？")
weight_float = float(weight)

print(f"你现在的体重是 {weight_float} 公斤")
print()

increase = input("增加多少公斤？")
increase_float = float(increase)

new_weight = weight_float + increase_float
print(f"增加 {increase_float} 公斤后，你的体重是 {new_weight} 公斤")
print()

# 练习 3: 简单对话
print("=" * 50)
print("       📝 练习 3: 模拟对话程序")
print("=" * 50)
print()

print("程序:")
q1 = input("1. 你最喜欢什么颜色？")
q2 = input("2. 你最喜欢的运动是什么？")

print()
print("程序总结:")
print(f"   你最喜欢 {q1} 色")
print(f"   你最喜欢运动是 {q2}")
print()

print("=" * 50)
print("       ✅ 所有练习完成！")
print("=" * 50)
