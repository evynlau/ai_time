# Day 16: 集合和元组 - 更多数据结构 📦
# 🎯 学习目标：学会使用元组和集合
# 📅 适合年龄：12 岁 +
# ⏱️ 建议时长：40 分钟

print("=" * 60)
print("        🐍 Python 编程课程 - Day 16        ")
print("        📦 元组和集合 - 更多数据结构")
print("=" * 60)
print()

# ========================================
# 1. 元组是什么？
# ========================================
print("📖 1. 元组是什么？")
print("-" * 50)
print()

print("元组就像一个不能改变的列表！")
print()
print("想象一下：")
print("  列表像是可以随意添加、删除物品的盒子")
print("  元组像是一个密封的瓶子，一旦做好就不能改变")
print()
print("💡 元组用圆括号 () 而不是方括号 []")
print()

# ========================================
# 2. 创建元组
# ========================================
print("📖 2. 创建元组")
print("-" * 50)
print()

# 创建元组
fruits = ('苹果', '香蕉', '橙子', '葡萄')
numbers = (1, 2, 3, 4, 5)
mixed = ('hello', 100, 3.14, True)

print(f"fruits = {fruits}")
print(f"numbers = {numbers}")
print(f"mixed = {mixed}")
print()

# 单个元素的元组（需要逗号）
single = ('hello',)
print(f"单个元素元组：{single} (注意逗号！)")
print()

# 用 tuple() 转换
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print(f"从列表转换：tuple([1,2,3]) = {my_tuple}")
print()

# ========================================
# 3. 访问元组
# ========================================
print("📖 3. 访问元组")
print("-" * 50)
print()

colors = ('红色', '蓝色', '绿色', '黄色', '紫色')

print(f"colors = {colors}")
print(f"colors[0] = {colors[0]}")
print(f"colors[2] = {colors[2]}")
print(f"colors[-1] = {colors[-1]}")
print(f"colors[1:4] = {colors[1:4]}")
print()

# ========================================
# 4. 元组解包
# ========================================
print("📖 4. 元组解包 - 一次取出多个值")
print("-" * 50)
print()

point = (10, 20)
x, y = point
print(f"point = {point}")
print(f"x = {x}, y = {y}")
print()

# 交换变量
a, b = 5, 10
print(f"交换前：a = {a}, b = {b}")
a, b = b, a
print(f"交换后：a = {a}, b = {b}")
print()

# 返回多个值（实际就是元组）
def get_min_max(numbers):
    return min(numbers), max(numbers)

nums = [3, 1, 9, 5, 7]
min_val, max_val = get_min_max(nums)
print(f"nums = {nums}")
print(f"最小值 = {min_val}, 最大值 = {max_val}")
print()

# ========================================
# 5. 集合是什么？
# ========================================
print("📖 5. 集合是什么？")
print("-" * 50)
print()

print("集合就像一个装有独特物品的篮子！")
print()
print("特点：")
print("  ✅ 不允许重复元素")
print("  ✅ 没有顺序")
print("  ✅ 可以做数学集合运算")
print()

# ========================================
# 6. 创建集合
# ========================================
print("📖 6. 创建集合")
print("-" * 50)
print()

# 创建集合
fruits_set = {'苹果', '香蕉', '橙子', '苹果', '香蕉'}
print(f"fruits_set = {fruits_set}")  # 自动去重！
print()

# set() 从列表转换
my_list = [1, 2, 2, 3, 3, 3, 4]
my_set = set(my_list)
print(f"从列表转换：set([1,2,2,3,3,3,4]) = {my_set}")
print()

# 空集合
empty_set = set()  # 注意：不能用 {}，那是空字典
print(f"空集合：{empty_set}")
print()

# ========================================
# 7. 集合操作
# ========================================
print("📖 7. 集合操作")
print("-" * 50)
print()

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print(f"集合 A = {set_a}")
print(f"集合 B = {set_b}")
print()

# 并集 | (两个集合的所有元素)
print(f"并集 A | B = {set_a | set_b}")
print(f"并集 A.union(B) = {set_a.union(set_b)}")
print()

# 交集 & (两个集合都有的元素)
print(f"交集 A & B = {set_a & set_b}")
print(f"交集 A.intersection(B) = {set_a.intersection(set_b)}")
print()

# 差集 - (A有B没有的元素)
print(f"差集 A - B = {set_a - set_b}")
print(f"差集 A.difference(B) = {set_a.difference(set_b)}")
print()

# 对称差集 ^ (两者不共有的元素)
print(f"对称差集 A ^ B = {set_a ^ set_b}")
print()

# ========================================
# 8. 集合的增删
# ========================================
print("📖 8. 集合的增删")
print("-" * 50)
print()

my_set = {1, 2, 3}
print(f"原始集合：{my_set}")

my_set.add(4)
print(f"添加 4：{my_set}")

my_set.add(2)  # 2 已存在，不会有变化
print(f"再添加 2：{my_set}")

my_set.remove(2)
print(f"删除 2：{my_set}")

# remove 元素不存在会报错，discard 不会
my_set.discard(99)  # 不报错
print(f"discard(99) 后：{my_set}")
print()

# ========================================
# 9. 什么时候用什么？
# ========================================
print("📖 9. 什么时候用什么？")
print("-" * 50)
print()

print("列表 []：")
print("  ✅ 需要按顺序存储")
print("  ✅ 需要通过索引访问")
print("  ✅ 内容会改变")
print()

print("元组 ()：")
print("  ✅ 数据不应该改变")
print("  ✅ 作为字典的键")
print("  ✅ 函数返回多个值")
print()

print("集合 {}：")
print("  ✅ 需要存储不重复的元素")
print("  ✅ 需要做集合运算（并集、交集等）")
print("  ✅ 不需要顺序")
print()

# ========================================
# 10. Day 16 总结
# ========================================
print("=" * 60)
print("       📋 Day 16 总结")
print("=" * 60)
print()
print("今天我们学会了：")
print("  ✅ 元组 - 不可变的列表，用 ()")
print("  ✅ 访问元组 - 和列表一样用索引")
print("  ✅ 元组解包 - 一次取出多个值")
print("  ✅ 集合 - 不重复的元素集合，用 {}")
print("  ✅ 集合运算 - 并集|、交集&、差集-")
print("  ✅ 集合的增删 - add, remove, discard")
print()

print("=" * 60)
print("       🎉 Day 16 完成！")
print("=" * 60)
print()
print("===========================================")
print("     💪 继续加油！学习进度：16/21 天完成！")
print("===========================================")
