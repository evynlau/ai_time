# Day 08: 列表 - Python 的百宝箱 - 参考答案
# 📚 本题的所有参考答案

print("=" * 60)
print("        ✅ Day 08 - 参考答案")
print("=" * 60)
print()

# ============================
# 练习 1: 创建列表
# ============================
print("📝 练习 1 答案：创建你的爱好列表")
print("-" * 40)
print()

# 解答：
hobbies = ['阅读', '运动', '音乐', '绘画', '编程']
print(f"答案 1: hobbies = {hobbies}")
print()

# ============================
# 练习 2: 访问和修改
# ============================
print("📝 练习 2 答案：修改购物清单")
print("-" * 40)
print()

# 解答：
shopping = ['苹果', '香蕉', '橙子']
print(f"原始列表：{shopping}")
shopping[1] = '葡萄'
print(f"修改索引 1 为'葡萄'：{shopping}")
shopping.insert(0, '草莓')
print(f"在位置 0 插入'草莓'：{shopping}")
print()

# ============================
# 练习 3: 列表方法
# ============================
print("📝 练习 3 答案：玩转列表方法")
print("-" * 40)
print()

# 解答：
team = ['张三', '李四', '王五']
print(f"原始：{team}")

team.append('赵六')
print(f"1. append('赵六'): {team}")

team.insert(1, '刘七')
print(f"2. insert(1, '刘七'): {team}")

count_zhangsan = team.count('张三')
print(f"3. count('张三') = {count_zhangsan}")

index_wangwu = team.index('王五')
print(f"4. index('王五') = {index_wangwu}")

team.remove('李四')
print(f"5. remove('李四'): {team}")

team.reverse()
print(f"6. reverse(): {team}")
print()

# ============================
# 练习 4: 列表切片
# ============================
print("📝 练习 4 答案：探索列表切片")
print("-" * 40)
print()

# 解答：
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(f"原始：{numbers}")

first_five = numbers[0:5]
print(f"1. [0:5] = {first_five}")

last_five = numbers[-5:]
print(f"2. [-5:] = {last_five}")

middle_five = numbers[5:]
print(f"3. [5:] = {middle_five}")

every_two = numbers[::2]
print(f"4. [::2] = {every_two}")

reversed_list = numbers[::-1]
print(f"5. [::-1] = {reversed_list}")
print()

# ============================
# 练习 5: 列表推导式
# ============================
print("📝 练习 5 答案：列表推导式")
print("-" * 40)
print()

# 解答：
# a) 0-9 的平方列表
squares = [x ** 2 for x in range(10)]
print(f"a) 0-9 的平方：{squares}")

# b) 偶数列表（0-9 中的偶数）
evens_in_range = [x for x in range(10) if x % 2 == 0]
print(f"b) 0-9 中的偶数：{evens_in_range}")

# 如果题目要求 [0, 2, 4, 6, 8]
evens_exact = [0, 2, 4, 6, 8]
print(f"   或指定列表：{evens_exact}")

# c) 单词长度列表
words = ['hello', 'world', 'python', 'code', 'list']
lengths = [len(word) for word in words]
print(f"c) 单词长度：{lengths}")
print()

# ============================
# 练习 6: 嵌套列表
# ============================
print("📝 练习 6 答案：网格矩阵")
print("-" * 40)
print()

# 解答：
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(f"原始矩阵：")
for row in grid:
    print(f"  {row}")
print()

element = grid[1][2]
print(f"grid[1][2] = {element}")

grid[0][0] = 100
print(f"修改后 matrix[0][0] = 100:")
for row in grid:
    print(f"  {row}")
print()

# ============================
# 练习 7: 列表统计
# ============================
print("📝 练习 7 答案：数字统计")
print("-" * 40)
print()

# 解答：
scores = [85, 92, 78, 95, 88, 76, 90, 82, 94, 87]
print(f"分数列表：{scores}")

highest = max(scores)
print(f"最高分：{highest}")

lowest = min(scores)
print(f"最低分：{lowest}")

average = sum(scores) / len(scores)
print(f"平均分：{average:.2f}")

passed = sum(1 for score in scores if score >= 80)
print(f">=80 分的数量：{passed}")
print()

# ============================
# 练习 8: 综合挑战
# ============================
print("📝 练习 8 答案：学生成绩管理器")
print("-" * 40)
print()

# 解答：
grades = {'小明': 85, '小红': 92, '小刚': 78}
print("步骤 1: 原始成绩")
print(f"  grades = {grades}")

grades['小丽'] = 95
grades['小强'] = 76
print("步骤 2: 添加新学生")
print(f"  grades = {grades}")

names = list(grades.keys())
print(f"步骤 3: 学生名称列表")
print(f"  names = {names}")

scores_list = list(grades.values())
print(f"步骤 4: 分数列表")
print(f"  scores_list = {scores_list}")

top_student = max(grades, key=grades.get)
print(f"步骤 5: 最高分学生")
print(f"  {top_student}: {grades[top_student]}分")

class_avg = sum(grades.values()) / len(grades)
print(f"步骤 6: 班级平均分")
print(f"  {class_avg:.2f}分")
print()

# ============================
# 额外示例
# ============================
print("🎯 额外练习题解答：")
print("-" * 40)
print()

# 示例 1: 去重列表
print("示例 1: 去重列表")
original = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique = list(set(original))
print(f"  原列表：{original}")
print(f"  去重后：{unique}")
print()

# 示例 2: 列表过滤
print("示例 2: 列表过滤")
numbers = list(range(1, 21))
doubles = [x * 2 for x in numbers if x % 3 == 0]
print(f"  1-20 中 3 的倍数，然后乘 2: {doubles}")
print()

# 示例 3: 列表排序
print("示例 3: 列表排序（降序）")
nums = [5, 2, 8, 1, 9, 3]
sorted_nums = sorted(nums, reverse=True)
print(f"  原列表：{nums}")
print(f"  降序排序：{sorted_nums}")
print()

print("=" * 60)
print("       🎉 所有练习答案已完成！")
print("=" * 60)
print()
