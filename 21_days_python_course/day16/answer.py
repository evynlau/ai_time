# Day 16: 集合和元组 - 参考答案
print("=" * 50)
print("       ✅ Day 16 参考答案")
print("=" * 50)
print()

# ========================================
# 练习 1: 创建元组
# ========================================
print("📝 练习 1: 创建元组")
print("-" * 40)
print()

fruits = ('苹果', '香蕉', '橙子')
numbers = (1, 2, 3, 4, 5)
mixed = ('hello', 100, True)

print(f"水果元组：{fruits}")
print(f"数字元组：{numbers}")
print(f"混合元组：{mixed}")
print()

single = ('独角兽',)
print(f"单元素元组：{single}")
print("✅ 练习 1 完成！")
print()

# ========================================
# 练习 2: 访问元组
# ========================================
print("📝 练习 2: 访问元组")
print("-" * 40)
print()

colors = ('红色', '蓝色', '绿色', '黄色', '紫色')
print(f"colors = {colors}")
print(f"colors[0] = {colors[0]}")
print(f"colors[-1] = {colors[-1]}")
print(f"colors[1:3] = {colors[1:3]}")
print("✅ 练习 2 完成！")
print()

# ========================================
# 练习 3: 元组解包
# ========================================
print("📝 练习 3: 元组解包")
print("-" * 40)
print()

person = ('小明', 10, '北京')
name, age, city = person
print(f"person = {person}")
print(f"解包：name={name}, age={age}, city={city}")
print()

x, y = 3, 7
print(f"交换前：x={x}, y={y}")
x, y = y, x
print(f"交换后：x={x}, y={y}")
print("✅ 练习 3 完成！")
print()

# ========================================
# 练习 4: 创建集合
# ========================================
print("📝 练习 4: 创建集合")
print("-" * 40)
print()

numbers_with_dup = [1, 2, 2, 3, 3, 3, 4, 4, 5]
unique_numbers = set(numbers_with_dup)
print(f"原列表：{numbers_with_dup}")
print(f"去重后：{unique_numbers}")
print()

my_set = {'苹果', '香蕉', '橙子'}
print(f"水果集合：{my_set}")
print("✅ 练习 4 完成！")
print()

# ========================================
# 练习 5: 集合运算
# ========================================
print("📝 练习 5: 集合运算")
print("-" * 40)
print()

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print(f"A = {set_a}")
print(f"B = {set_b}")
print()
print(f"并集 A | B = {set_a | set_b}")
print(f"交集 A & B = {set_a & set_b}")
print(f"差集 A - B = {set_a - set_b}")
print(f"对称差集 A ^ B = {set_a ^ set_b}")
print("✅ 练习 5 完成！")
print()

# ========================================
# 练习 6: 集合增删
# ========================================
print("📝 练习 6: 集合增删")
print("-" * 40)
print()

my_set = {1, 2, 3}
print(f"原始：{my_set}")

my_set.add(4)
print(f"添加 4 后：{my_set}")

my_set.add(2)
print(f"再添加 2（已存在）：{my_set}")

my_set.remove(2)
print(f"删除 2 后：{my_set}")

my_set.discard(99)
print(f"discard(99) 后：{my_set}")
print("✅ 练习 6 完成！")
print()

# ========================================
# 练习 7: 实际应用
# ========================================
print("📝 练习 7: 实际应用")
print("-" * 40)
print()

class_a = {'游泳', '篮球', '足球', '绘画', '音乐'}
class_b = {'篮球', '足球', '绘画', '跳舞', '唱歌'}

common = class_a & class_b
only_a = class_a - class_b
only_b = class_b - class_a
all_hobbies = class_a | class_b

print(f"A班喜好：{class_a}")
print(f"B班喜好：{class_b}")
print()
print(f"共同喜好：{common}")
print(f"只有A班喜欢：{only_a}")
print(f"只有B班喜欢：{only_b}")
print(f"所有喜好：{all_hobbies}")
print()

registrations = ['小明', '小红', '小明', '小刚', '小红', '小丽']
unique_members = set(registrations)
print(f"报名名单：{registrations}")
print(f"去重后：{unique_members}")
print(f"共 {len(unique_members)} 人")
print("✅ 练习 7 完成！")
print()

# ========================================
# 综合练习
# ========================================
print("📝 综合练习: 数据类型转换")
print("-" * 40)
print()

original = [1, 2, 2, 3, 3, 3, 4, 4, 5]

as_tuple = tuple(original)
as_set = set(original)
as_list = list(as_set)

print(f"原始列表：{original}")
print(f"转为元组：{as_tuple}")
print(f"转为集合：{as_set}")
print(f"集合转回列表：{as_list}")
print()
print("✅ 综合练习完成！")
print()

# ========================================
# 知识点总结
# ========================================
print("=" * 50)
print("       📊 Day 16 知识点总结")
print("=" * 50)
print()
print("✅ 元组用 ()，不可变，列表的'锁住版本'")
print("✅ 元组解包：a, b = (1, 2)")
print("✅ 集合用 {}，去重，无顺序")
print("✅ 集合运算：| 并集，& 交集，- 差集")
print("✅ 集合方法：add, remove, discard")
print("✅ list(), tuple(), set() 互相转换")
print()
print("🎉 恭喜完成所有练习！")
print()
