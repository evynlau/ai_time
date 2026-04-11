# Day 04: 输入与输出
# 🎯 学习目标：理解 input() 函数，学会与程序互动
# 📅 适合年龄：12 岁 +
# ⏱️ 建议时长：35 分钟


# ==========================================
# Day 04: 输入与输出
# ==========================================

print("=" * 50)
print("        🐍 Python 编程入门课程 - Day 04        ")
print("              输入与输出 - 程序互动")
print("=" * 50)
print()

# ==========================================
# 1. 使用 input() 获取用户输入
# ==========================================

print("📖 1. input() 函数 - 获取用户输入")
print("-" * 50)
print()

print("input() 函数会等待用户输入文字，然后返回字符串")
print()
print("用法:")
print("  name = input('请输入你的名字：')")
print("  print('你好，' + name + '!')")
print()

# 注意：在实际运行中，input() 会等待用户输入
# 这里我们模拟演示
print("示例运行:")
print("  请输入你的名字：小明")
print("  你好，小明!")
print()

print("🔑 重要提示: input() 返回的是字符串类型！")
print("如果需要数字，需要转换类型")
print()

# ==========================================
# 2. 类型转换
# ==========================================

print("📖 2. 类型转换")
print("-" * 50)
print()

print("1️⃣ int() - 转换为整数")
age_str = "12"
age_int = int(age_str)
print(f"   age_str = '{age_str}'")
print(f"   age_int = int(age_str) = {age_int}")
print(f"   type(age_int) = {type(age_int)}")
print()

print("2️⃣ float() - 转换为浮点数")
height_str = "1.55"
height_float = float(height_str)
print(f"   height_str = '{height_str}'")
print(f"   height_float = float(height_str) = {height_float}")
print(f"   type(height_float) = {type(height_float)}")
print()

print("3️⃣ str() - 转换为字符串")
number = 99
number_str = str(number)
print(f"   number = {number}")
print(f"   number_str = str(number) = '{number_str}'")
print(f"   type(number_str) = {type(number_str)}")
print()

print("4️⃣ bool() - 转换为布尔值")
zero = 0
none_zero = 5
print(f"   bool(0) = {bool(zero)}")
print(f"   bool({none_zero}) = {bool(none_zero)}")
print()

# ====================================
# 3. input() 的常见错误
# ==========================================

print("📖 3. 常见错误")
print("-" * 50)
print()

print("❌ 错误示例:")
print("  age = input('请输入年龄：')")
print("  result = age + 1  # ❌ 会报错！字符串不能加数字")
print()

print("✅ 正确写法:")
print("  age = input('请输入年龄：')")
print("  age = int(age)  # 转换为整数")
print("  result = age + 1")
print()

print("⚠️ 注意：如果用户输入的不是数字，int() 会报错")
print()

# ====================================
# 4. 实际应用：问答程序
# ==========================================

print("📖 4. 实际应用：交互式问答程序")
print("-" * 50)
print()

print("让我们做一个简单的问答程序:")
print()

print("name = input('你叫什么名字？')")
print("age = input('你今年几岁？')")
print("hobby = input('你的爱好是什么？')")
print()
print("print(f'你好，{name}!')")
print("print(f'你今年{age}岁')")
print("print(f'你的爱好是{hobby}')")
print()

print("示例运行:")
print("  你叫什么名字？小红")
print("  你今年几岁？11")
print("  你的爱好是什么？画画")
print()
print("  你好，小红!")
print("  你今年 11 岁")
print("  你的爱好是画画")
print()

# ====================================
# 5. Python 小贴士
# ==========================================

print("=" * 50)
print("       💡 Python 小贴士")
print("=" * 50)
print()
print("1. input() 返回的文字总是字符串")
print("2. 使用 int() 将数字字符串转换为整数")
print("3. 使用 float() 将数字字符串转换为小数")
print("4. 使用 str() 将数字转换为字符串")
print("5. 如果用户输入错误内容（如输入字母），int() 会报错")
print("6. 可以在 input() 提示后面加内容，让用户知道要输入什么")
print("7. 使用 try-except 可以处理错误输入")
print()

# ====================================
# 6. 实践练习
# ==========================================

print("=" * 50)
print("       📝 实践练习：自我介绍问答程序")
print("=" * 50)
print()
print("🎯 任务：创建一个自我介绍问答程序")
print()
print("要求:")
print("  1. 询问用户 3 个问题：姓名、年龄、爱好")
print("  2. 将年龄转换为整数")
print("  3. 显示总结：你好，{姓名}，{年龄}岁，爱好是 {爱好}")
print("  4. 计算 5 年后的年龄")
print()

print("示例答案:")
print("-" * 40)
print("name = input('你叫什么名字？')")
print("age = input('你今年几岁？')")
print("hobby = input('你的爱好是什么？')")
print()
print("age_num = int(age)")
print()
print("print(f'你好，{name}!')")
print("print(f'你今年 {age} 岁')")
print("print(f'你的爱好是：{hobby}')")
print()
print("five_years_later = age_num + 5")
print("print(f'5 年后你将 {five_years_later} 岁')")
print()

# ====================================
# 7. Day 04 总结
# ==========================================

print("=" * 50)
print("       📋 Day 04 总结")
print("=" * 50)
print()
print("今天我们学会了:")
print("  ✅ input() 函数 - 获取用户输入")
print("  ✅ int() 将字符串转换为整数")
print("  ✅ float() 将字符串转换为浮点数")
print("  ✅ str() 将数字转换为字符串")
print("  ✅ type() 查看数据类型")
print()

print("=" * 50)
print("       🎉 Day 04 完成！")
print("=" * 50)
print()
print("恭喜你！你的程序现在可以和用户互动了！")
print("明天学习条件语句，让程序能够做判断！")
print()
print("===============================================")
print("     💪 继续加油！学习进度：4/21 天完成！")
print("===============================================")
