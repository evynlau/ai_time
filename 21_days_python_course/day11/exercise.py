# Day 11: 函数返回值 - 练习
print("=" * 50)
print("       📝 Day 11 练习：函数返回值")
print("=" * 50)
print()

# ========================================
# 练习 1: 返回单个值
# ========================================
print("🎯 练习 1: 返回单个值")
print("-" * 40)
print()

def multiply(a, b):
    """返回两个数的乘积"""
    return a * b

result = multiply(6, 7)
print(f"multiply(6, 7) = {result}")
print()

def is_even(num):
    """判断是否是偶数"""
    return num % 2 == 0

print(f"is_even(10) = {is_even(10)}")
print(f"is_even(7) = {is_even(7)}")
print("✅ 练习 1 完成！")
print()

# ========================================
# 练习 2: 返回多个值
# ========================================
print("🎯 练习 2: 返回多个值")
print("-" * 40)
print()

def get_rectangle_info(width, height):
    """返回矩形的面积和周长"""
    area = width * height
    perimeter = 2 * (width + height)
    return area, perimeter

area, perimeter = get_rectangle_info(5, 3)
print(f"矩形 5×3：")
print(f"  面积：{area}")
print(f"  周长：{perimeter}")
print()

def get_circle_info(radius):
    """返回圆的面积和周长"""
    pi = 3.14159
    area = pi * radius * radius
    circumference = 2 * pi * radius
    return area, circumference

area, circ = get_circle_info(5)
print(f"圆形半径 5：")
print(f"  面积：{area:.2f}")
print(f"  周长：{circ:.2f}")
print("✅ 练习 2 完成！")
print()

# ========================================
# 练习 3: 返回列表
# ========================================
print("🎯 练习 3: 返回列表")
print("-" * 40)
print()

def get_even_numbers(n):
    """返回 1 到 n 之间所有的偶数"""
    evens = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens

result = get_even_numbers(20)
print(f"1 到 20 的偶数：{result}")
print()

def filter_positive(numbers):
    """返回所有正数"""
    return [x for x in numbers if x > 0]

nums = [-5, 3, -1, 8, -2, 10, 0, -7]
positive_nums = filter_positive(nums)
print(f"原列表：{nums}")
print(f"正数：{positive_nums}")
print("✅ 练习 3 完成！")
print()

# ========================================
# 练习 4: 返回字典
# ========================================
print("🎯 练习 4: 返回字典")
print("-" * 40)
print()

def create_student(name, age, grade):
    """创建学生信息字典"""
    return {
        "name": name,
        "age": age,
        "grade": grade
    }

student = create_student("小明", 10, "三年级")
print(f"学生信息：{student}")
print(f"姓名：{student['name']}")
print(f"年龄：{student['age']}岁")
print()

def build_profile(first, last, **info):
    """创建人物资料"""
    profile = {"first": first, "last": last}
    profile.update(info)
    return profile

profile = build_profile("张", "三", age=10, city="北京", hobby="编程")
print(f"人物资料：{profile}")
print("✅ 练习 4 完成！")
print()

# ========================================
# 练习 5: 条件返回
# ========================================
print("🎯 练习 5: 条件返回")
print("-" * 40)
print()

def get_age_group(age):
    """根据年龄返回年龄段"""
    if age < 0:
        return "无效年龄"
    elif age < 3:
        return "婴儿"
    elif age < 12:
        return "儿童"
    elif age < 18:
        return "青少年"
    else:
        return "成年人"

for age in [-1, 2, 8, 15, 25]:
    print(f"年龄 {age}：{get_age_group(age)}")
print()

def classify_score(score):
    """分类成绩"""
    if score < 0 or score > 100:
        return "无效分数"
    if score >= 90:
        return "优秀"
    elif score >= 75:
        return "良好"
    elif score >= 60:
        return "及格"
    else:
        return "不及格"

scores = [95, 82, 67, 45, 105, -5]
for score in scores:
    print(f"{score}分：{classify_score(score)}")
print("✅ 练习 5 完成！")
print()

# ========================================
# 综合练习: 迷你计算器
# ========================================
print("🎯 综合练习: 迷你计算器")
print("-" * 40)
print()

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "错误：除数为0"
    return a / b

def power(a, b):
    return a ** b

operations = [
    ("加法", add, 10, 5),
    ("减法", subtract, 10, 5),
    ("乘法", multiply, 10, 5),
    ("除法", divide, 10, 5),
    ("幂运算", power, 2, 8),
]

for name, func, a, b in operations:
    result = func(a, b)
    print(f"  {a} 和 {b} 的{name} = {result}")

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
print("  ✅ 使用 return 返回函数结果")
print("  ✅ 返回单个值和多个值")
print("  ✅ 返回列表和字典")
print("  ✅ 根据条件返回不同结果")
print()
print("🎉 太棒了！明天学习 while 循环！")
print()
