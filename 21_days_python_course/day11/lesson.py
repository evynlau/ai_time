# Day 11: 函数返回值 - 得到结果 🎯
# 🎯 学习目标：理解函数返回值，学会从函数获取结果
# 📅 适合年龄：12 岁 +
# ⏱️ 建议时长：45 分钟

print("=" * 60)
print("        🐍 Python 编程课程 - Day 11        ")
print("        🎯 函数返回值 - 得到结果")
print("=" * 60)
print()

# ========================================
# 1. 什么是返回值？
# ========================================
print("📖 1. 什么是返回值？")
print("-" * 50)
print()

print("想象一下：")
print("  你去自助机器买饮料")
print("  你投入硬币（参数）")
print("  机器给你饮料（返回值）")
print()
print("💡 函数的返回值，就是函数给你的'饮料'！")
print()

# ========================================
# 2. 使用 return 返回值
# ========================================
print("📖 2. 使用 return 返回值")
print("-" * 50)
print()

print("格式：")
print("  def 函数名(参数):")
print("      计算")
print("      return 结果")
print()

def add(a, b):
    """返回两个数的和"""
    result = a + b
    return result

# 调用函数并使用返回值
sum_result = add(5, 3)
print(f"add(5, 3) 返回：{sum_result}")
print(f"加上 10：{sum_result + 10}")
print()

# ========================================
# 3. 返回多个值
# ========================================
print("📖 3. 返回多个值")
print("-" * 50)
print()

def get_stats(numbers):
    """返回列表的最大值、最小值和平均值"""
    max_val = max(numbers)
    min_val = min(numbers)
    avg_val = sum(numbers) / len(numbers)
    return max_val, min_val, avg_val

scores = [85, 92, 78, 95, 88]
max_score, min_score, avg_score = get_stats(scores)
print(f"分数列表：{scores}")
print(f"最高分：{max_score}")
print(f"最低分：{min_score}")
print(f"平均分：{avg_score:.2f}")
print()

# ========================================
# 4. 立即返回
# ========================================
print("📖 4. 立即返回 - return 的作用")
print("-" * 50)
print()

def find_first_even(numbers):
    """找到第一个偶数"""
    for num in numbers:
        if num % 2 == 0:
            return num
    return None

print(f"find_first_even([1, 3, 5, 6, 7]) = {find_first_even([1, 3, 5, 6, 7])}")
print(f"find_first_even([1, 3, 5, 7]) = {find_first_even([1, 3, 5, 7])}")
print()
print("💡 return 会立即结束函数，后面的代码不会执行！")
print()

# ========================================
# 5. 实际应用
# ========================================
print("📖 5. 实际应用例子")
print("-" * 50)
print()

def calculate_grade(score):
    """根据分数返回等级"""
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

def pass_or_fail(score):
    """判断是否及格"""
    return score >= 60

scores = [95, 82, 67, 45, 88]
print("成绩评定：")
for score in scores:
    grade = calculate_grade(score)
    passed = "✅ 及格" if pass_or_fail(score) else "❌ 不及格"
    print(f"  {score}分 → {grade}级 {passed}")
print()

# ========================================
# 6. 返回字典
# ========================================
print("📖 6. 返回字典")
print("-" * 50)
print()

def create_user(name, age):
    """创建一个用户信息字典"""
    return {
        "name": name,
        "age": age,
        "level": "初级"
    }

user = create_user("小明", 10)
print(f"用户信息：{user}")
print(f"用户名：{user['name']}")
print(f"用户等级：{user['level']}")
print()

# ========================================
# 7. Day 11 总结
# ========================================
print("=" * 60)
print("       📋 Day 11 总结")
print("=" * 60)
print()
print("今天我们学会了：")
print("  ✅ return 语句 - 从函数返回结果")
print("  ✅ return 可以返回一个或多个值")
print("  ✅ return 会立即结束函数执行")
print("  ✅ 可以返回字典、列表等复杂类型")
print()

print("=" * 60)
print("       🎉 Day 11 完成！")
print("=" * 60)
print()
print("太棒了！你的函数现在可以返回结果了！")
print()
print("===========================================")
print("     💪 继续加油！学习进度：11/21 天完成！")
print("===========================================")
