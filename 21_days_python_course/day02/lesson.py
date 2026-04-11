# Day 02: 变量与数据类型
# 🎯 学习目标：理解变量和赋值，掌握字符串、整数、浮点数、布尔值
# 📅 适合年龄：12 岁 +
# ⏱️ 建议时长：35 分钟


# ==========================================
# Day 02: 变量与数据类型
# ==========================================

print("=" * 50)
print("        🐍 Python 编程入门课程 - Day 02        ")
print("         变量与数据类型")
print("=" * 50)
print()

# ==========================================
# 1. 什么是变量？
# ==========================================

print("📖 1. 什么是变量？")
print("-" * 50)
print("变量就像一个带名字的存储盒，用来存放数据。")
print()
print("想象你有几个盒子：")
print("  📦 盒子 1：名字叫 'name'，里面放名字")
print("  📦 盒子 2：名字叫 'age'，里面放年龄")
print("  📦 盒子 3：名字叫 'hobby'，里面放爱好")
print()

print("在编程中，我们这样创建变量:")
print("  name = '小明'     # 名字")
print("  age = 12         # 年龄")
print("  hobby = '画画'   # 爱好")
print()

# ==========================================
# 2. 使用变量
# ==========================================

print("📖 2. 如何使用变量")
print("-" * 50)
print()

# 创建变量
name = "小明"
age = 12
hobby = "画画"

print(f"  🎯 变量 name 的内容：{name}")
print(f"  🎯 变量 age 的内容：{age}")
print(f"  🎯 变量 hobby 的内容：{hobby}")
print()

print("使用 f-string 格式化变量:")
my_info = f"我叫{name}，今年{age}岁，喜欢{hobby}"
print(f"  📝 {my_info}")
print()

# ==========================================
# 3. 数据结构
# ==========================================

print("📖 3. 数据类型 - Python 中的'数据类型'")
print("-" * 50)
print()
print("Python 有几种主要的数据类型:")
print()

print("1️⃣ 字符串 (str) - 文字")
print("   用引号括起来的内容都是字符串")
print("   name = '小明'")
print(f"   type(name) = {type(name)}")
print()

print("2️⃣ 整数 (int) - 完整的数字")
print("   age = 12")
print(f"   type(age) = {type(age)}")
print()

print("3️⃣ 浮点数 (float) - 带小数点的数字")
print("   height = 1.55")
height = 1.55
print(f"   type(height) = {type(height)}")
print()

print("4️⃣ 布尔值 (bool) - True 或 False")
print("   is_student = True")
is_student = True
print(f"   type(is_student) = {type(is_student)}")
print()

# ==========================================
# 4. 变量命名规则
# ==========================================

print("📖 4. 变量命名规则")
print("-" * 50)
print()
print("正确命名示例:")
print("  ✅ name        # 普通变量")
print("  ✅ age_1        # 数字在下划线后")
print("  ✅ _hello       # 以下划线开头")
print("  ✅ MyVariable   # 驼峰命名")
print()
print("错误命名示例:")
print("  ❌ 1name        # 不能以数字开头")
print("  ❌ name@       # 不能包含特殊字符")
print("  ❌ name-name   # 不能用减号连接")
print("  ❌ if          # 不能是保留关键字")
print()

# ==========================================
# 5. 修改变量
# ==========================================

print("📖 5. 修改变量的值")
print("-" * 50)
print()
print("变量可以随时修改！")

score = 80
print(f"  初始成绩：score = {score}")

score = 85
print(f"  第一次修改：score = {score}")

score = 90
print(f"  第二次修改：score = {score}")
print()

print("注意：每次赋值都会替换原来的值。")
print()

# ==========================================
# 6. Python 小贴士
# ==========================================

print("=" * 50)
print("       💡 Python 小贴士")
print("=" * 50)
print()
print("1. 字符串必须用引号（单引号''或双引号''都可以）")
print("2. 整数没有引号，float 有小数点")
print("3. f'{'text'}' 可以插入变量，叫 f-string")
print("4. 变量名要能描述它的内容")
print("5. 变量可以在任何地方重新赋值")
print()

# ==========================================
# 7. 实践练习
# ==========================================

print("=" * 50)
print("       📝 实践练习：个人信息卡片")
print("=" * 50)
print()
print("🎯 任务：创建一个你的个人信息卡片")
print()
print("要求:")
print("  1. 创建至少 4 个变量（名字、年龄、爱好、学校等）")
print("  2. 使用 f-string 显示你的信息")
print("  3. 打印你的数据类型")
print()

print("示例答案:")
print("-" * 40)
print("my_name = '小红'")
print("my_age = 11")
print("my_hobby = '阅读'")
print("my_school = '阳光小学'")
print()
print("print(f'👤 个人信息：')")
print("print(f'   姓名：{my_name}')")
print("print(f'   年龄：{my_age}岁')")
print("print(f'   爱好：{my_hobby}')")
print("print(f'   学校：{my_school}')")
print()

# ==========================================
# 8. Day 02 总结
# ==========================================

print("=" * 50)
print("       📋 Day 02 总结")
print("=" * 50)
print()
print("今天我们学会了:")
print("  ✅ 什么是变量（带名字的存储盒）")
print("  ✅ 四种主要数据类型：str int float bool")
print("  ✅ 使用 f-string 格式化字符串")
print("  ✅ 变量命名规则")
print("  ✅ 修改变量的值")
print()

print("=" * 50)
print("       🎉 Day 02 完成！")
print("=" * 50)
print()
print("恭喜！你已经掌握了 Python 的基本数据类型！")
print("明天我们会学习运算符 - 就像数学魔法棒！")
print()
print("===============================================")
print("     💪 继续加油！学习进度：2/21 天完成！")
print("===============================================")
