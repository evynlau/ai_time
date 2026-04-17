# Day 09: 函数 - 神奇咒语 - 参考答案
print("=" * 50)
print("       ✅ Day 09 参考答案")
print("=" * 50)
print()

# ========================================
# 练习 1: 创建打招呼函数
# ========================================
print("📝 练习 1: 创建打招呼函数")
print("-" * 40)
print()

def greet():
    """打印简单的打招呼信息"""
    print("=" * 40)
    print("  👋 你好！欢迎来到 Python 世界！")
    print("=" * 40)
    print()

greet()
print("✅ 练习 1 完成！")
print()

# ========================================
# 练习 2: 创建自我介绍函数
# ========================================
print("📝 练习 2: 创建自我介绍函数")
print("-" * 40)
print()

def introduce():
    """打印自我介绍"""
    print("=" * 40)
    print("  📛 姓名：张小明")
    print("  🎂 年龄：10 岁")
    print("  🏫 学校：阳光小学")
    print("  💕 爱好：编程、踢球、画画")
    print("=" * 40)
    print()

introduce()
print("✅ 练习 2 完成！")
print()

# ========================================
# 练习 3: 创建多个功能函数
# ========================================
print("📝 练习 3: 创建多个功能函数")
print("-" * 40)
print()

def say_good_morning():
    """早安问候"""
    print("🌅 早安！新的一天开始了！")
    print("  今天也要加油哦！")
    print()

def say_good_afternoon():
    """午安问候"""
    print("☀️ 中午好！吃午饭了吗？")
    print("  下午也要努力！")
    print()

def say_good_night():
    """晚安问候"""
    print("🌙 晚安！该睡觉了！")
    print("  明天见！做个好梦！")
    print()

# 测试所有函数
say_good_morning()
say_good_afternoon()
say_good_night()
print("✅ 练习 3 完成！")
print()

# ========================================
# 练习 4: 创建计算函数
# ========================================
print("📝 练习 4: 创建简单的计算函数")
print("-" * 40)
print()

def print_math_result():
    """打印数学计算结果"""
    a = 10
    b = 20
    print(f"  {a} + {b} = {a + b}")
    print(f"  {a} × {b} = {a * b}")
    print()

print_math_result()
print("✅ 练习 4 完成！")
print()

# ========================================
# 练习 5: 创建图案打印函数
# ========================================
print("📝 练习 5: 创建图案打印函数")
print("-" * 40)
print()

def print_stars():
    """打印星星图案"""
    print("  ⭐⭐⭐⭐⭐")
    print("  ⭐           ⭐")
    print("  ⭐    🌙    ⭐")
    print("  ⭐           ⭐")
    print("  ⭐⭐⭐⭐⭐")
    print()

def print_heart():
    """打印爱心图案"""
    print("   ❤️❤️❤️   ")
    print("  ❤️❤️❤️❤️❤️  ")
    print("  ❤️❤️❤️❤️❤️  ")
    print("   ❤️❤️❤️   ")
    print("    ❤️❤️   ")
    print("     ❤️   ")
    print()

print("调用 print_stars()：")
print_stars()

print("调用 print_heart()：")
print_heart()
print("✅ 练习 5 完成！")
print()

# ========================================
# 练习 6: 创建菜单函数
# ========================================
print("📝 练习 6: 创建菜单显示函数")
print("-" * 40)
print()

def show_menu():
    """显示餐厅菜单"""
    print("=" * 40)
    print("       🍔 小天才餐厅菜单 🍔")
    print("=" * 40)
    print("  1. 🍕 披萨      - 30 元")
    print("  2. 🍔 汉堡      - 20 元")
    print("  3. 🍜 面条      - 15 元")
    print("  4. 🍦 冰淇淋    - 10 元")
    print("  5. 🍹 果汁      -  8 元")
    print("=" * 40)
    print()

show_menu()
print("✅ 练习 6 完成！")
print()

# ========================================
# 综合练习: 创建计算器展示函数
# ========================================
print("📝 综合练习: 创建计算器展示函数")
print("-" * 40)
print()

def show_calculator():
    """展示计算器功能"""
    print("=" * 40)
    print("       🧮 小天才计算器 🧮")
    print("=" * 40)
    print()
    
    # 加法
    x, y = 25, 17
    print(f"  加法: {x} + {y} = {x + y}")
    
    # 减法
    x, y = 25, 17
    print(f"  减法: {x} - {y} = {x - y}")
    
    # 乘法
    x, y = 25, 17
    print(f"  乘法: {x} × {y} = {x * y}")
    
    # 除法
    x, y = 100, 4
    print(f"  除法: {x} ÷ {y} = {x / y}")
    
    print()
    print("=" * 40)
    print()

show_calculator()
print("✅ 综合练习完成！")
print()

# ========================================
# 知识点总结
# ========================================
print("=" * 50)
print("       📊 Day 09 知识点总结")
print("=" * 50)
print()
print("✅ def 关键字用于定义函数")
print("✅ 函数名后面要加冒号 :")
print("✅ 函数内的代码必须缩进")
print("✅ 调用函数使用 函数名()")
print("✅ 函数的执行顺序是自上而下")
print()
print("🎉 恭喜完成所有练习！")
print()
