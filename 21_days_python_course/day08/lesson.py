# Day 08: 列表 - Python 的百宝箱 📦
# 🎯 学习目标：理解列表概念，学会创建和操作列表
# 📅 适合年龄：12 岁 +
# ⏱️ 建议时长：45 分钟

print("=" * 60)
print("        🐍 Python 编程课程 - Day 08        ")
print("        📦 列表 - Python 的百宝箱            ")
print("=" * 60)
print()

# ================================
# 1. 列表是什么？
# ================================
print("📖 什么是列表？")
print("-" * 50)
print("列表就像一个百宝箱 🔮 里面可以装很多东西！")
print("Python 列表是一种可以存放多个值的数据结构。")
print("列表用方括号 [] 表示，里面的元素用逗号分隔。")
print()
print("举例：")
print("  我的百宝箱：['糖果', '积木', '画笔', '玩偶'] 🧸")
print()
print("列表的特点:")
print("  ✅ 可以放不同的数据类型")
print("  ✅ 可以放重复的元素")
print("  ✅ 元素的顺序很重要")
print("  ✅ 可以用数字来访问（索引从 0 开始）")
print()

# ================================
# 2. 创建列表
# ================================
print("=" * 60)
print("       🎨 创建你的列表")
print("=" * 60)
print()

print("📝 方法 1: 使用方括号 [] 创建列表")
friends = ['小明', '小红', '小刚', '小丽']
print(f"friends = {friends}")
print()

print("📝 方法 2: 创建混合类型列表")
mixed = ['苹果', 100, 3.14, True, '你好']
print(f"mixed = {mixed}")
print()

print("📝 方法 3: 创建数字列表")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"numbers = {numbers}")
print()

print("📝 方法 4: 创建空列表")
empty_list = []
print(f"empty_list = {empty_list}")
print()

print("📝 方法 5: 使用 list() 函数创建")
fruits = list(['香蕉', '葡萄', '西瓜'])
print(f"fruits = {fruits}")
print()

# ================================
# 3. 访问列表元素
# ================================
print("=" * 60)
print("       🔍 访问列表元素")
print("=" * 60)
print()

print("🎯 访问列表中的元素")
colors = ['红色', '蓝色', '绿色', '黄色', '紫色']
print(f"colors = {colors}")
print()

print("使用索引访问元素（索引从 0 开始）:")
print(f"  colors[0] = '{colors[0]}'  # 第一个元素")
print(f"  colors[1] = '{colors[1]}'  # 第二个元素")
print(f"  colors[2] = '{colors[2]}'  # 第三个元素")
print(f"  colors[4] = '{colors[4]}'  # 第五个元素")
print()

print("🔢 负数索引 - 从后面往前面数:")
print(f"  colors[-1] = '{colors[-1]}'  # 最后一个元素")
print(f"  colors[-2] = '{colors[-2]}'  # 倒数第二个元素")
print()

print("📏 使用 len() 获取列表长度:")
print(f"  列表中有多少个元素：len(colors) = {len(colors)}")
print()

# ================================
# 4. 修改列表元素
# ================================
print("=" * 60)
print("       📝 修改列表")
print("=" * 60)
print()

print("🎯 修改列表中的元素")
shopping = ['牛奶', '面包', '鸡蛋', '苹果']
print(f"原始购物清单：{shopping}")
print()

print("方法 1: 用索引替换元素")
shopping[0] = '豆浆'
print(f"  将第 1 个元素改为'豆浆': {shopping}")
shopping[2] = '黄油'
print(f"  将第 3 个元素改为'黄油': {shopping}")
print()

print("方法 2: 用 list[index1:index2] 批量替换")
colors = ['红', '橙', '黄', '绿，蓝，靛，紫']
print(f"  原始颜色：{colors}")
colors[1:3] = ['橘', '青']
print(f"  将索引 1-2 改为['橘', '青']: {colors}")
print()

# ================================
# 5. 列表的常用方法
# ================================
print("=" * 60)
print("       🛠️ 列表的常用方法")
print("=" * 60)
print()

print("📌 方法 1: .append() - 在末尾添加元素")
pets = ['小猫', '小狗']
print(f"  原始列表：{pets}")
pets.append('小仓鼠')
print(f"  pets.append('小仓鼠') -> {pets}")
pets.append(['小鱼', '乌龟'])
print(f"  pets.append(['小鱼', '乌龟']) -> {pets}")
print()

print("📌 方法 2: .insert() - 在指定位置插入元素")
fruits = ['苹果', '橙子']
print(f"  原始列表：{fruits}")
fruits.insert(1, '香蕉')
print(f"  fruits.insert(1, '香蕉') -> {fruits}")
print()

print("📌 方法 3: .remove() - 删除第一个匹配的元素")
animals = ['猫', '狗', '兔子', '猫']
print(f"  原始列表：{animals}")
animals.remove('猫')
print(f"  animals.remove('猫') -> {animals}")
print()

print("📌 方法 4: .pop() - 删除并返回元素")
numbers = [10, 20, 30, 40, 50]
print(f"  原始列表：{numbers}")
last = numbers.pop()
print(f"  numbers.pop() -> 返回 {last}, 列表变为 {numbers}")
first = numbers.pop(0)
print(f"  numbers.pop(0) -> 返回 {first}, 列表变为 {numbers}")
print()

print("📌 方法 5: .count() - 统计元素出现次数")
items = ['苹果', '香蕉', '苹果', '橙子', '苹果']
print(f"  列表：{items}")
print(f"  items.count('苹果') = {items.count('苹果')}")
print()

print("📌 方法 6: .index() - 查找元素位置")
letters = ['a', 'b', 'c', 'd', 'e']
print(f"  列表：{letters}")
print(f"  letters.index('c') = {letters.index('c')}")
print()

print("📌 方法 7: .extend() - 扩展列表")
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(f"  list1.extend(list2) -> {list1}")
print()

print("📌 方法 8: .sort() 和 .reverse()")
nums = [5, 2, 8, 1, 9]
print(f"  原始列表：{nums}")
nums.sort()
print(f"  nums.sort() -> {nums}  # 从小到大排序")
nums.reverse()
print(f"  nums.reverse() -> {nums}  # 反转列表")
print()

# ================================
# 6. 列表的其他操作
# ================================
print("=" * 60)
print("       🔗 列表的其他操作")
print("=" * 60)
print()

print("🎯 列表拼接")
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print(f"  [1, 2, 3] + [4, 5, 6] = {combined}")
print()

print("🎯 列表复制")
original = [1, 2, 3, 4, 5]
copy_list = original[:]
print(f"  original = {original}")
print(f"  copy_list = original[:] = {copy_list}")
print()

print("🎯 列表切片")
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"  original = {my_list}")
print(f"  my_list[0:5] = {my_list[0:5]}  # 前 5 个元素")
print(f"  my_list[5:] = {my_list[5:]}   # 从索引 5 到最后")
print(f"  my_list[:5] = {my_list[:5]}   # 前 5 个元素")
print(f"  my_list[::2] = {my_list[::2]}  # 每隔一个元素")
print(f"  my_list[::-1] = {my_list[::-1]}  # 反转列表")
print()

print("🎯 in 和 not in 运算符")
fruits = ['苹果', '香蕉', '橙子', '葡萄']
print(f"  fruits = {fruits}")
print(f"  '苹果' in fruits = {'苹果' in fruits}")
print(f"  '草莓' in fruits = {'草莓' in fruits}")
print(f"  '草莓' not in fruits = {'草莓' not in fruits}")
print()

# ================================
# 7. 列表的遍历 - for 循环
# ================================
print("=" * 60)
print("       🔄 列表遍历")
print("=" * 60)
print()

print("🎯 使用 for 循环遍历列表")
colors = ['红色', '蓝色', '绿色', '黄色']
print("  for color in colors:")
print("      print(f'  {color}')")
for color in colors:
    print(f"  {color}")
print()

print("🎯 使用 enumerate() 获取索引和值")
students = ['小明', '小红', '小刚']
print("  for index, student in enumerate(students):")
print("      print(f'{index}: {student}')")
for index, student in enumerate(students):
    print(f"  {index}: {student}")
print()

# ================================
# 8. 列表推导式
# ================================
print("=" * 60)
print("       ✨ 列表推导式")
print("=" * 60)
print()

print("🎯 用列表推导式创建新列表")
numbers = [1, 2, 3, 4, 5]
squares = [x ** 2 for x in numbers]
print(f"  numbers = {numbers}")
print(f"  [x ** 2 for x in numbers] = {squares}")
print()

print("🎯 条件列表推导式")
mixed = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [x for x in mixed if x % 2 == 0]
print(f"  mixed = {mixed}")
print(f"  [x for x in mixed if x % 2 == 0] = {evens}")
print()

# ================================
# 9. 嵌套列表
# ================================
print("=" * 60)
print("       📦 嵌套列表")
print("=" * 60)
print()

print("🎯 列表里可以包含其他列表！")
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(f"  matrix = {matrix}")
print(f"  matrix[0] = {matrix[0]}  # 第一个子列表")
print(f"  matrix[0][0] = {matrix[0][0]}  # 第一行第一列的元素")
print(f"  matrix[1][2] = {matrix[1][2]}  # 第二行第三列的元素")
print()

# ================================
# 10. 实践练习
# ================================
print("=" * 60)
print("       📝 实践练习")
print("=" * 60)
print()
print("🎯 练习：创建你的购物清单管理器")
print()
print("任务：")
print("  1. 创建一个空列表 groceries 作为购物清单")
print("  2. 使用 .append() 添加 3 种你喜欢的食物")
print("  3. 使用 .insert() 在开头添加早餐")
print("  4. 打印完整清单")
print()

print("参考代码:")
groceries = []
groceries.append('牛奶')
groceries.append('面包')
groceries.append('鸡蛋')
groceries.insert(0, '麦片')
print(f"groceries = {groceries}")
print()

# ================================
# 11. Day 08 总结
# ================================
print("=" * 60)
print("       📋 Day 08 总结")
print("=" * 60)
print()
print("今天我们学会了:")
print("  ✅ 列表的概念和创建方法")
print("  ✅ 访问列表元素（索引和负数索引）")
print("  ✅ 列表的常用方法：append, insert, remove, pop, count, index, extend, sort, reverse")
print("  ✅ 列表切片和复制")
print("  ✅ for 循环和 enumerate 遍历列表")
print("  ✅ 列表推导式")
print("  ✅ 嵌套列表")
print()
print("=" * 60)
print("       🎉 Day 08 完成！")
print("=" * 60)
print()
print("恭喜你完成了 Python 学习的第 8 天！")
print("列表是你的好朋友，多多练习！")
print()
print("===========================================")
print("     💪 加油！编程之旅继续！")
print("===========================================")
