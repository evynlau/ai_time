# Day 15: 字典 - 标签盒子 🏷️
# 🎯 学习目标：理解字典概念，学会使用键值对存储数据
# 📅 适合年龄：12 岁 +
# ⏱️ 建议时长：45 分钟

print("=" * 60)
print("        🐍 Python 编程课程 - Day 15        ")
print("        🏷️ 字典 - 标签盒子")
print("=" * 60)
print()

# ========================================
# 1. 为什么需要字典？
# ========================================
print("📖 1. 为什么需要字典？")
print("-" * 50)
print()

print("想象一下：")
print("  你的通讯录里有很多朋友")
print("  如果用列表存储，你要记住：")
print("    friends[0] = '小明'  → 哪个是名字？")
print("    friends[1] = '10岁'  → 哪个是年龄？")
print("    friends[2] = '北京'  → 哪个是城市？")
print()
print("  太混乱了！")
print()
print("💡 字典就像有标签的收纳盒！")
print("   每个盒子都有标签（键），里面装着东西（值）")
print("   想要什么？看标签就知道了！")
print()

# ========================================
# 2. 创建字典
# ========================================
print("📖 2. 创建字典")
print("-" * 50)
print()

print("基本格式：")
print("  变量 = {'键1': 值1, '键2': 值2, ...}")
print()

# 创建字典
student = {
    'name': '小明',
    'age': 10,
    'city': '北京',
    'grade': '四年级'
}

print("创建一个学生字典：")
print(f"  student = {student}")
print()

print("也可以用 dict() 函数：")
user = dict(name='小红', age=11, city='上海')
print(f"  user = {user}")
print()

# ========================================
# 3. 访问字典的值
# ========================================
print("📖 3. 访问字典的值")
print("-" * 50)
print()

student = {'name': '小明', 'age': 10, 'city': '北京', 'grade': '四年级'}

print("用键来访问值：")
print(f"  student['name']  → {student['name']}")
print(f"  student['age']  → {student['age']}")
print(f"  student['city'] → {student['city']}")
print()

print("用 get() 方法（更安全）：")
print(f"  student.get('name')    → {student.get('name')}")
print(f"  student.get('hobby')    → {student.get('hobby')}")  # 不存在的键
print(f"  student.get('hobby', '未知') → {student.get('hobby', '未知')}")  # 默认值
print()

# ========================================
# 4. 修改和添加
# ========================================
print("📖 4. 修改和添加字典内容")
print("-" * 50)
print()

person = {'name': '小明', 'age': 10}
print(f"原始字典：{person}")

print("\n修改已有的值：")
person['age'] = 11
print(f"  person['age'] = 11 → {person}")

print("\n添加新的键值对：")
person['city'] = '北京'
print(f"  person['city'] = '北京' → {person}")

print("\n删除键值对：")
del person['age']
print(f"  del person['age'] → {person}")
print()

# ========================================
# 5. 字典的常用方法
# ========================================
print("📖 5. 字典的常用方法")
print("-" * 50)
print()

info = {'name': '小明', 'age': 10, 'city': '北京', 'grade': '四年级'}

print("keys() - 获取所有键：")
print(f"  info.keys() = {list(info.keys())}")

print("\nvalues() - 获取所有值：")
print(f"  info.values() = {list(info.values())}")

print("\nitems() - 获取所有键值对：")
print(f"  info.items() = {list(info.items())}")

print("\n遍历字典：")
for key, value in info.items():
    print(f"  {key} → {value}")
print()

# ========================================
# 6. 嵌套字典
# ========================================
print("📖 6. 嵌套字典")
print("-" * 50)
print()

classroom = {
    'student1': {'name': '小明', 'Age': 10, 'Score': 95},
    'student2': {'Name': '小红', 'Age': 11, 'Score': 88},
    'student3': {'Name': '小刚', 'Age': 10, 'Score': 92},
}

print(f"classroom = {classroom}")
print()
print("访问嵌套字典：")
print(f"  classroom['student1'] = {classroom['student1']}")
print(f"  classroom['student1']['Score'] = {classroom['student1']['Score']}")
print()

# ========================================
# 7. 实际应用
# ========================================
print("📖 7. 实际应用 - 水果店")
print("-" * 50)
print()

inventory = {
    '苹果': 50,
    '香蕉': 30,
    '橙子': 25,
    '葡萄': 15
}

print("水果店库存：")
for fruit, count in inventory.items():
    print(f"  {fruit}：{count} 个")

print("\n进货后：")
inventory['苹果'] += 10
inventory['香蕉'] += 20
inventory['草莓'] = 20  # 新增水果

for fruit, count in inventory.items():
    print(f"  {fruit}：{count} 个")
print()

# ========================================
# 8. Python 小贴士
# ========================================
print("=" * 50)
print("       💡 Python 小贴士")
print("=" * 50)
print()
print("1. 字典的键必须是不可变的（字符串、数字、元组）")
print("2. 字典的值可以是任意类型")
print("3. 字典是无序的（Python 3.7+ 保持插入顺序）")
print("4. 键不能重复，值可以重复")
print("5. 用 get() 比直接访问更安全")
print()

# ========================================
# 9. Day 15 总结
# ========================================
print("=" * 60)
print("       📋 Day 15 总结")
print("=" * 60)
print()
print("今天我们学会了：")
print("  ✅ 字典是什么 - 带标签的数据容器")
print("  ✅ 创建字典 - {} 和 dict()")
print("  ✅ 访问字典 - 用键找值")
print("  ✅ 修改和添加 - 添加新标签")
print("  ✅ 常用方法 - keys(), values(), items()")
print("  ✅ 嵌套字典 - 字典里的字典")
print()

print("=" * 60)
print("       🎉 Day 15 完成！")
print("=" * 60)
print()
print("太棒了！字典让你的程序更聪明！")
print()
print("===========================================")
print("     💪 继续加油！学习进度：15/21 天完成！")
print("===========================================")
