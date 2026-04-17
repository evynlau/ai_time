# Day 10: 带参数的函数 - 接收礼物 🎁
# 🎯 学习目标：理解参数概念，学会给函数传递信息
# 📅 适合年龄：12 岁 +
# ⏱️ 建议时长：45 分钟

print("=" * 60)
print("        🐍 Python 编程课程 - Day 10        ")
print("        🎁 带参数的函数 - 接收礼物")
print("=" * 60)
print()

# ========================================
# 1. 什么是参数？
# ========================================
print("📖 1. 什么是参数？")
print("-" * 50)
print()

print("想象一下：")
print("  你对机器人说：'给我倒一杯饮料'")
print("  但是机器人不知道：什么饮料？多大杯子？要不要加冰？")
print()
print("💡 参数就是告诉函数'怎么做'的信息！")
print("   比如：'给我倒可乐，大杯，加冰'")
print("         可乐=参数1, 大杯=参数2, 加冰=参数3")
print()

# ========================================
# 2. 带参数的基本函数
# ========================================
print("📖 2. 带参数的基本函数")
print("-" * 50)
print()

print("基本格式：")
print("  def 函数名(参数名):")
print("      使用参数的代码")
print()

# 定义带参数的函数
def greet_person(name):
    """向指定的人打招呼"""
    print(f"👋 你好，{name}！欢迎！")
    print()

# 调用带参数的函数
print("调用 greet_person('小明')：")
greet_person("小明")

print("调用 greet_person('小红')：")
greet_person("小红")

print("分析：")
print("  greet_person(name)  → name 是参数，像一个变量")
print("  greet_person('小明') → '小明' 会传给 name")
print("  函数内部：name = '小明'，所以打印出 '你好，小明！'")
print()

# ========================================
# 3. 多个参数
# ========================================
print("📖 3. 多个参数")
print("-" * 50)
print()

def introduce(name, age, city):
    """介绍一个人"""
    print(f"📛 姓名：{name}")
    print(f"🎂 年龄：{age} 岁")
    print(f"🏙️ 城市：{city}")
    print()

print("调用 introduce('小明', 10, '北京')：")
introduce('小明', 10, '北京')

print("调用 introduce('小红', 11, '上海')：")
introduce('小红', 11, '上海')

print("注意：参数顺序很重要！")
print("  introduce('小明', 10, '北京')")
print("  name='小明', age=10, city='北京' ✓")
print()

# ========================================
# 4. 参数的类型
# ========================================
print("📖 4. 参数可以是什么类型？")
print("-" * 50)
print()

# 数字参数
def double_number(x):
    """计算一个数的两倍"""
    result = x * 2
    print(f"  {x} 的两倍是 {result}")
    print()

print("传入数字：")
double_number(5)
double_number(100)

# 字符串参数
def repeat_word(word, times):
    """重复一个单词多次"""
    print(f"  {word} " * times)
    print()

print("传入字符串：")
repeat_word("你好", 3)
repeat_word("Python", 2)

# 列表参数
def print_list(items):
    """打印列表中的所有元素"""
    print("  列表内容：")
    for item in items:
        print(f"    - {item}")
    print()

print("传入列表：")
print_list(["苹果", "香蕉", "橙子"])

# ========================================
# 5. 参数的默认值
# ========================================
print("📖 5. 参数的默认值")
print("-" * 50)
print()

def greet_with_title(name, title="同学"):
    """打招呼，可以选择性地加称呼"""
    print(f"👋 你好，{title}{name}！欢迎！")
    print()

print("不指定 title（使用默认值'同学'）：")
greet_with_title("小明")

print("指定 title：")
greet_with_title("小红", "老师")

print("💡 小贴士：默认值参数要放在最后！")
print()

# ========================================
# 6. 关键字参数
# ========================================
print("📖 6. 关键字参数")
print("-" * 50)
print()

def describe_pet(pet_type, pet_name):
    """描述一只宠物"""
    print(f"🐾 宠物类型：{pet_type}")
    print(f"🐾 宠物名字：{pet_name}")
    print()

print("按顺序传参数：")
describe_pet("小狗", "旺财")

print("用关键字传参数（顺序可以换）：")
describe_pet(pet_name="小白", pet_type="小猫")

print("💡 关键字参数让代码更清晰，不容易出错！")
print()

# ========================================
# 7. 实际应用例子
# ========================================
print("=" * 50)
print("       🎯 实际应用例子")
print("=" * 50)
print()

# 计算器
def calc(a, b, op):
    """简单的计算器"""
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b != 0:
            return a / b
        return "错误：除数为0"
    return "未知操作"

print("calc(10, 5, '+') =", calc(10, 5, "+"))
print("calc(10, 5, '-') =", calc(10, 5, "-"))
print("calc(10, 5, '*') =", calc(10, 5, "*"))
print("calc(10, 5, '/') =", calc(10, 5, "/"))
print()

# ========================================
# 8. Python 小贴士
# ========================================
print("=" * 50)
print("       💡 Python 小贴士")
print("=" * 50)
print()
print("1. 参数就像函数接收的'礼物'")
print("2. 多个参数用逗号分隔")
print("3. 默认值参数放在最后")
print("4. 关键字参数让代码更清晰")
print("5. 参数顺序：普通参数 → 默认参数")
print()

# ========================================
# 9. Day 10 总结
# ========================================
print("=" * 60)
print("       📋 Day 10 总结")
print("=" * 60)
print()
print("今天我们学会了：")
print("  ✅ 参数是什么 - 给函数传递信息")
print("  ✅ 如何定义带参数的函数")
print("  ✅ 如何调用带参数的函数")
print("  ✅ 多个参数的使用方法")
print("  ✅ 默认值参数")
print("  ✅ 关键字参数")
print()

print("=" * 60)
print("       🎉 Day 10 完成！")
print("=" * 60)
print()
print("太棒了！你的函数现在可以接收信息了！")
print()
print("===========================================")
print("     💪 继续加油！学习进度：10/21 天完成！")
print("===========================================")
