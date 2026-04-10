# Day 18 课后练习题 - 字符串操作
print("练习 1: 字符串处理")

name = "小明 2024"

# 处理字符串
print(f"📝 原字符串：'{name}'")

# 转大写
print(f"🔤 大写：'{name.upper()}'")

# 转小写
print(f"🔤 小写：'{name.lower()}'")

# 查找位置
pos = name.find("小")
print(f"🔍 '小' 的位置：{pos}")

# 替换
replaced = name.replace("2024", "2025")
print(f"🔄 替换后：'{replaced}'")

# 🎯 挑战：姓名处理
print("\n🎯 挑战：姓名密码")

first_name = "李"
last_name = "小明"

# 组合密码
password = first_name[0] + last_name[0] + last_name[1]
print(f"🔑 密码：{password}")

# 取部分文字
middle = last_name[1:3]
print(f"📝 中间部分：'{middle}'")
