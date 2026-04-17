# Day 10: 带参数的函数 - 参考答案
print("=" * 50)
print("       ✅ Day 10 参考答案")
print("=" * 50)
print()

# ========================================
# 练习 1: 单个参数的函数
# ========================================
print("📝 练习 1: 单个参数的函数")
print("-" * 40)
print()

def greet(name):
    """向指定的人打招呼"""
    print(f"👋 你好，{name}！欢迎来到编程世界！")
    print()

greet("小明")
greet("小红")
greet("小刚")
print("✅ 练习 1 完成！")
print()

# ========================================
# 练习 2: 多个参数的函数
# ========================================
print("📝 练习 2: 多个参数的函数")
print("-" * 40)
print()

def introduce(name, age, hobby):
    """介绍一个人"""
    print(f"📛 姓名：{name}")
    print(f"🎂 年龄：{age} 岁")
    print(f"💕 爱好：{hobby}")
    print("-" * 30)
    print()

introduce("小明", 10, "编程")
introduce("小红", 11, "画画")
introduce("小刚", 9, "踢球")
print("✅ 练习 2 完成！")
print()

# ========================================
# 练习 3: 计算函数
# ========================================
print("📝 练习 3: 计算函数")
print("-" * 40)
print()

def calculate_area(width, height):
    """计算矩形面积"""
    area = width * height
    print(f"  宽度：{width}")
    print(f"  高度：{height}")
    print(f"  面积：{width} × {height} = {area}")
    print()

calculate_area(5, 3)
calculate_area(10, 8)
calculate_area(7, 4)
print("✅ 练习 3 完成！")
print()

# ========================================
# 练习 4: 带默认值的参数
# ========================================
print("📝 练习 4: 带默认值的参数")
print("-" * 40)
print()

def greet_with_title(name, title="同学"):
    """打招呼，可以选择性地加称呼"""
    print(f"👋 你好，{title}{name}！")
    print()

greet_with_title("小明")
greet_with_title("小红")
greet_with_title("老师", "王")
greet_with_title("医生", "李")
print("✅ 练习 4 完成！")
print()

# ========================================
# 练习 5: 判断函数
# ========================================
print("📝 练习 5: 判断函数")
print("-" * 40)
print()

def check_number(num):
    """判断一个数是正数、负数还是零"""
    if num > 0:
        print(f"  {num} 是正数 ✅")
    elif num < 0:
        print(f"  {num} 是负数 ❌")
    else:
        print(f"  {num} 是零 🅾️")
    print()

check_number(10)
check_number(-5)
check_number(0)
check_number(100)
print("✅ 练习 5 完成！")
print()

# ========================================
# 练习 6: 打印图案函数
# ========================================
print("📝 练习 6: 打印图案函数")
print("-" * 40)
print()

def print_rectangle(width, height):
    """用星号打印矩形"""
    print(f"  打印 {width}×{height} 的矩形：")
    for i in range(height):
        print("  " + "*" * width)
    print()

print_rectangle(5, 3)
print_rectangle(8, 4)
print_rectangle(10, 3)
print("✅ 练习 6 完成！")
print()

# ========================================
# 练习 7: 关键字参数
# ========================================
print("📝 练习 7: 关键字参数")
print("-" * 40)
print()

def describe_pet(animal, name, age):
    """描述宠物信息"""
    print(f"  🐾 动物：{animal}")
    print(f"  🐾 名字：{name}")
    print(f"  🐾 年龄：{age} 岁")
    print()

describe_pet(animal="狗", name="旺财", age=3)
describe_pet(name="小白", animal="猫", age=2)
describe_pet(age=5, animal="兔子", name="绒绒")
print("✅ 练习 7 完成！")
print()

# ========================================
# 综合练习: 创建一个小型菜单程序
# ========================================
print("📝 综合练习: 小型菜单系统")
print("-" * 40)
print()

def show_food_menu():
    """显示食物菜单"""
    print("=" * 40)
    print("       🍔 美食菜单 🍔")
    print("=" * 40)
    print("  1. 🍕 披萨      - 30 元")
    print("  2. 🍔 汉堡      - 20 元")
    print("  3. 🍜 面条      - 15 元")
    print("  4. 🍦 冰淇淋    - 10 元")
    print("=" * 40)
    print()

def order_food(food_name, price, quantity):
    """处理订单"""
    total = price * quantity
    print(f"  📝 订单：{food_name}")
    print(f"  💰 单价：{price} 元")
    print(f"  📦 数量：{quantity}")
    print(f"  💵 总计：{total} 元")
    print()

show_food_menu()
order_food("披萨", 30, 3)
order_food("汉堡", 20, 2)
order_food("面条", 15, 1)
print("✅ 综合练习完成！")
print()

# ========================================
# 知识点总结
# ========================================
print("=" * 50)
print("       📊 Day 10 知识点总结")
print("=" * 50)
print()
print("✅ 参数是函数接收的输入信息")
print("✅ def func(param): - param 是参数")
print("✅ 函数调用时传入参数值")
print("✅ 默认值参数：def func(param=默认值)")
print("✅ 关键字参数：func(name='小明')")
print()
print("🎉 恭喜完成所有练习！")
print()
