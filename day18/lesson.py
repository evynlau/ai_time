# Day 18: 字符串操作
# 🎯 学习目标：学习处理文字的方法
#
# 📖 故事：文字就像乐高积木！
# 可以拆开，可以拼合，可以修改

# 字符串方法
text = "Hello Python"

# 转大写
print("🔤 大写:", text.upper())
print("🔤 小写:", text.lower())

# 查找文字
print("🔍 找'o':", text.find("o"))

# 替换文字
print("🔄 替换 'Python':", text.replace("Python", "World"))

# 分割文字
words = "Hello World".split()
print("📝 分割:", words)

# 🎮 练习：姓名处理
name = "小明 2024"
print(f"👤 名字：{name}")
print(f"🔤 大写：{name.upper()}")

# 去掉空格
clean_name = "  Hello  ".strip()
print(f"✨ 去空格：'{clean_name}'")

# 🎯 小挑战：姓名密码
first = "小明"
last = "李"
password = first[0] + last[0] + str(2024)
print(f"🔑 密码：{password}")
