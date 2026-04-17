# Day 15: 字典 - 标签盒子 - 练习
print("=" * 50)
print("       📝 Day 15 练习：字典基础")
print("=" * 50)
print()

# ========================================
# 练习 1: 创建字典
# ========================================
print("🎯 练习 1: 创建字典")
print("-" * 40)
print()

# 创建一个表示你的朋友信息的字典
friend = {
    'name': '小明',
    'age': 10,
    'city': '北京',
    'hobby': '踢足球'
}

print(f"我的朋友：{friend}")
print()

# 创建一个水果字典
fruits = {
    '苹果': 5,
    '香蕉': 3,
    '橙子': 8
}
print(f"水果库存：{fruits}")
print("✅ 练习 1 完成！")
print()

# ========================================
# 练习 2: 访问字典
# ========================================
print("🎯 练习 2: 访问字典")
print("-" * 40)
print()

book = {
    'title': 'Python入门',
    'author': '张三',
    'price': 59,
    'pages': 300
}

print(f"书名：{book['title']}")
print(f"作者：{book['author']}")
print(f"价格：{book['price']}元")
print(f"页数：{book['pages']}页")
print()

# 使用 get 方法
print(f"出版社（不存在，用get）：{book.get('publisher', '未知')}")
print("✅ 练习 2 完成！")
print()

# ========================================
# 练习 3: 修改和添加
# ========================================
print("🎯 练习 3: 修改和添加")
print("-" * 40)
print()

person = {'name': '小明', 'age': 10}
print(f"原始：{person}")

person['age'] = 11
person['city'] = '上海'
person['hobby'] = '画画'
print(f"修改后：{person}")
print("✅ 练习 3 完成！")
print()

# ========================================
# 练习 4: 遍历字典
# ========================================
print("🎯 练习 4: 遍历字典")
print("-" * 40)
print()

scores = {'语文': 92, '数学': 88, '英语': 95, '科学': 90}

print("考试成绩：")
for subject, score in scores.items():
    print(f"  {subject}：{score}分")

print(f"\n总分：{sum(scores.values())}分")
print(f"平均分：{sum(scores.values()) / len(scores):.1f}分")
print("✅ 练习 4 完成！")
print()

# ========================================
# 练习 5: 嵌套字典
# ========================================
print("🎯 练习 5: 嵌套字典")
print("-" * 40)
print()

classroom = {
    'student1': {'name': '小明', 'score': 95},
    'student2': {'name': '小红', 'score': 88},
    'student3': {'name': '小刚', 'score': 92}
}

print("班级成绩：")
for id, info in classroom.items():
    print(f"  {id}：{info['name']}，得分 {info['score']}")
print("✅ 练习 5 完成！")
print()

# ========================================
# 练习 6: 字典方法
# ========================================
print("🎯 练习 6: 字典方法")
print("-" * 40)
print()

info = {'name': '小明', 'age': 10, 'city': '北京', 'grade': '四年级'}

print(f"所有键：{list(info.keys())}")
print(f"所有值：{list(info.values())}")
print(f"键值对：{list(info.items())}")
print()

print("检查键是否存在：")
print(f"  'name' in info = {'name' in info}")
print(f"  'hobby' in info = {'hobby' in info}")
print()

# pop 方法
removed = info.pop('grade')
print(f"删除 grade，值：{removed}")
print(f"删除后：{info}")
print("✅ 练习 6 完成！")
print()

# ========================================
# 综合练习: 图书馆管理系统
# ========================================
print("🎯 综合练习: 图书馆管理系统")
print("-" * 40)
print()

library = {
    'book1': {'title': 'Python入门', 'author': '张三', 'available': True},
    'book2': {'title': '数据结构', 'author': '李四', 'available': False},
    'book3': {'title': '算法设计', 'author': '王五', 'available': True}
}

print("图书馆藏书：")
for id, book in library.items():
    status = "可借" if book['available'] else "已借出"
    print(f"  {id}：《{book['title']}》- {book['author']} [{status}]")

# 借书
library['book2']['available'] = True
print("\nbook2 被归还，现在可借：")
for id, book in library.items():
    status = "可借" if book['available'] else "已借出"
    print(f"  {id}：《{book['title']}》[{status}]")
print()
print("✅ 综合练习完成！")
print()

# ========================================
# 完成
# ========================================
print("=" * 50)
print("       ✅ 所有练习完成！")
print("=" * 50)
print()
print("今天学到了：")
print("  ✅ 创建字典")
print("  ✅ 访问字典的值")
print("  ✅ 修改和添加内容")
print("  ✅ 遍历字典")
print("  ✅ 嵌套字典")
print("  ✅ 字典常用方法")
print()
print("🎉 明天学习集合和元组！")
print()
