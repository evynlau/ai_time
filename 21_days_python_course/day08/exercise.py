# Day 08: 列表 - Python 的百宝箱 - 练习
# 📝 练习：使用列表解决实际问题

print("=" * 60)
print("        🐜 编程小挑战 - Day 08        ")
print("        📦 列表练习")
print("=" * 60)
print()

# ============================
# 练习 1: 创建列表
# ============================
print("🎯 练习 1: 创建你的爱好列表")
print("-" * 40)
print("任务：创建一个名为 hobbies 的列表，")
print("      包含你喜欢的至少 5 种爱好。")
print("示例: hobbies = ['阅读', '运动', '音乐', '绘画', '编程']")
print()

# 在这里编写你的代码：
hobbies = ['阅读', '运动', '音乐', '绘画', '编程']  # 请修改为你的爱好!
print(f"你的爱好列表：{hobbies}")
print()

# ============================
# 练习 2: 访问和修改
# ============================
print("🎯 练习 2: 修改购物清单")
print("-" * 40)
print("任务：")
print("  a) 创建一个 shopping 列表，包含 ['苹果', '香蕉', '橙子']")
print("  b) 将'香蕉'改为'葡萄'")
print("  c) 在索引 0 的位置添加'草莓'")
print("  d) 打印最终列表")
print()

shopping = ['苹果', '香蕉', '橙子']
shopping[1] = '葡萄'
shopping.insert(0, '草莓')
print(f"修改后的购物清单：{shopping}")
print()

# ============================
# 练习 3: 列表方法
# ============================
print("🎯 练习 3: 玩转列表方法")
print("-" * 40)
print("任务：")
print("  a) 创建一个 team 列表，包含 ['张三', '李四', '王五']")
print("  b) 添加 '赵六' 到列表末尾")
print("  c) 在索引 1 的位置插入 '刘七'")
print("  d) 统计'张三'出现的次数")
print("  e) 找到'王五'的位置索引")
print("  f) 删除列表中的'李四'")
print("  g) 反转列表")
print("  h) 打印最终列表")
print()

team = ['张三', '李四', '王五']
team.append('赵六')
team.insert(1, '刘七')
count_zhangsan = team.count('张三')
index_wangwu = team.index('王五')
team.remove('李四')
team.reverse()
print(f"最终团队列表：{team}")
print(f"'张三'出现的次数：{count_zhangsan}")
print()

# ============================
# 练习 4: 列表切片
# ============================
print("🎯 练习 4: 探索列表切片")
print("-" * 40)
print("任务：")
print("  a) 创建一个 numbers 列表：[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]")
print("  b) 提取前 5 个元素")
print("  c) 提取后 5 个元素")
print("  d) 提取中间的 5 个元素（索引 5-9）")
print("  e) 每两个元素提取一个")
print("  f) 将列表完全反转")
print()

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
first_five = numbers[0:5]
last_five = numbers[5:10]
middle_five = numbers[5:]
every_two = numbers[::2]
reversed_list = numbers[::-1]
print(f"原始列表：{numbers}")
print(f"前 5 个元素：{first_five}")
print(f"后 5 个元素：{last_five}")
print(f"从索引 5 开始：{middle_five}")
print(f"每两个元素：{every_two}")
print(f"完全反转：{reversed_list}")
print()

# ============================
# 练习 5: 列表推导式
# ============================
print("🎯 练习 5: 列表推导式")
print("-" * 40)
print("任务：")
print("  a) 用列表推导式创建 0-9 的平方列表")
print("  b) 用列表推导式创建偶数列表（0,2,4,6,8）")
print("  c) 用列表推导式创建单词长度列表")
print()

# 你的解答：
squares = [x ** 2 for x in range(10)]
evens = [x for x in range(10) if x % 2 == 0]
words = ['hello', 'world', 'python', 'code', 'list']
lengths = [len(word) for word in words]
print(f"0-9 的平方：{squares}")
print(f"偶数列表：{evens}")
print(f"单词长度列表：{lengths}")
print()

# ============================
# 练习 6: 嵌套列表
# ============================
print("🎯 练习 6: 网格矩阵")
print("-" * 40)
print("任务：")
print("  a) 创建一个 3x3 的矩阵 grid")
print("  b) 访问并打印 grid[1][2]（第二行第三列）")
print("  c) 修改 grid[0][0] 的值为 100")
print("  d) 打印完整的矩阵")
print()

grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
element = grid[1][2]
grid[0][0] = 100
print(f"访问的元素：{element}")
print(f"修改后的矩阵：")
for row in grid:
    print(f"  {row}")
print()

# ============================
# 练习 7: 列表统计
# ============================
print("🎯 练习 7: 数字统计")
print("-" * 40)
print("任务：")
print("  a) 创建一个 scores 列表，包含 10 个随机分数（或固定值）")
print("  b) 找出最高分")
print("  c) 找出最低分")
print("  d) 计算平均分")
print("  e) 统计有多少个分数大于等于 80 分")
print()

# 你的解答：
scores = [85, 92, 78, 95, 88, 76, 90, 82, 94, 87]
highest = max(scores)
lowest = min(scores)
average = sum(scores) / len(scores)
passed = sum(1 for score in scores if score >= 80)
print(f"分数列表：{scores}")
print(f"最高分：{highest}")
print(f"最低分：{lowest}")
print(f"平均分：{average:.2f}")
print(f">=80 分的数量：{passed}")
print()

# ============================
# 练习 8: 综合挑战
# ============================
print("🎯 练习 8: 学生成绩管理器")
print("-" * 40)
print("任务：创建一个简单的学生成绩管理系统")
print("  a) 创建字典：{'小明': 85, '小红': 92, '小刚': 78}")
print("  b) 添加新学生：{'小丽': 95, '小强': 76}")
print("  c) 将所有学生名字放入一个列表")
print("  d) 将所有分数放入一个列表")
print("  e) 找出最高分学生")
print("  f) 计算班级平均分")
print()

grades = {'小明': 85, '小红': 92, '小刚': 78}
grades['小丽'] = 95
grades['小强'] = 76
names = list(grades.keys())
scores_list = list(grades.values())
top_student = max(grades, key=grades.get)
class_avg = sum(grades.values()) / len(grades)
print(f"学生列表：{names}")
print(f"分数列表：{scores_list}")
print(f"最高分学生：{top_student} ({grades[top_student]}分)")
print(f"班级平均分：{class_avg:.2f}分")
print()

# ============================
# 完成检查
# ============================
print("=" * 60)
print("       🎉 恭喜你完成了所有练习！")
print("=" * 60)
print()
print("回顾要点:")
print("  ✅ 创建不同类型的列表")
print("  ✅ 访问和修改列表元素")
print("  ✅ 使用列表方法：append, insert, remove, count, index, reverse")
print("  ✅ 列表切片和复制")
print("  ✅ 列表推导式")
print("  ✅ 嵌套列表")
print("  ✅ 列表统计函数：max, min, sum")
print()
print("做得好！继续加油！💪")
print()
