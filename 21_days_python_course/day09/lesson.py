# Day 09: 函数 - 神奇咒语 🪄
# 🎯 学习目标：理解函数概念，学会定义和调用函数
# 📅 适合年龄：12 岁 +
# ⏱️ 建议时长：40 分钟

print("=" * 60)
print("        🐍 Python 编程课程 - Day 09        ")
print("        🪄 函数 - 神奇咒语")
print("=" * 60)
print()

# ========================================
# 1. 为什么需要函数？
# ========================================
print("📖 1. 为什么需要函数？")
print("-" * 50)
print()

print("想象一下：")
print("  你每天早上都要刷牙、洗脸、吃早餐")
print("  如果每天都要把这些步骤重新写一遍，多麻烦啊！")
print()
print("✅ 解决方案：把这些步骤定义成一个'早安仪式'函数")
print("   每天只需要说一声'早安仪式()'就行了！")
print()

print("函数的优点：")
print("  ✅ 代码可以重复使用")
print("  ✅ 让程序更有条理")
print("  ✅ 方便修改和维护")
print("  ✅ 让代码更易读")
print()

# ========================================
# 2. 函数的定义和调用
# ========================================
print("📖 2. 函数的定义和调用")
print("-" * 50)
print()

print("定义函数的基本格式：")
print("  def 函数名():")
print("      要执行的代码")
print()

# 定义一个简单的函数
def say_hello():
    """这个函数会让电脑打招呼"""
    print("=" * 40)
    print("  👋 你好！欢迎来到 Python 世界！")
    print("=" * 40)
    print()

# 调用函数
print("调用 say_hello() 函数：")
say_hello()

print("分析：")
print("  def     → 告诉电脑，我要定义一个函数")
print("  say_hello → 函数的名字（自己起的）")
print("  ()       → 空括号，表示这个函数不需要信息")
print("  :        → 冒号，告诉电脑接下来是函数的内容")
print()

# ========================================
# 3. 函数的命名规则
# ========================================
print("📖 3. 函数的命名规则")
print("-" * 50)
print()

print("好的函数名应该：")
print("  ✅ 描述这个函数做什么")
print("  ✅ 用小写字母")
print("  ✅ 单词之间用下划线连接")
print()

print("好的例子：")
print("  say_hello()      → 打招呼")
print("  calculate_area() → 计算面积")
print("  find_max()       → 找最大值")
print("  draw_triangle()  → 画三角形")
print()

print("不好的例子：")
print("  a()              → 不知道做什么")
print("  func1()          → 不知道做什么")
print("  ShanGaoDeHua()   → 不用中文，不用驼峰命名")
print()

# ========================================
# 4. 函数可以有多个任务
# ========================================
print("📖 4. 函数可以有多个任务")
print("-" * 50)
print()

def morning_routine():
    """早安仪式函数"""
    print("🌅 早上好！")
    print("  1. 刷牙")
    print("  2. 洗脸")
    print("  3. 吃早餐")
    print("✅ 准备好开始新的一天了！")
    print()

def evening_routine():
    """晚安仪式函数"""
    print("🌙 晚安！")
    print("  1. 刷牙")
    print("  2. 洗澡")
    print("  3. 上床睡觉")
    print("💤 做个好梦！")
    print()

print("调用 morning_routine()：")
morning_routine()

print("调用 evening_routine()：")
evening_routine()

# ========================================
# 5. 函数的执行顺序
# ========================================
print("📖 5. 函数的执行顺序")
print("-" * 50)
print()

print("看这个例子：")
print()
print("def first():")
print("    print('A: 这是第一个函数')")
print()
print("def second():")
print("    print('B: 这是第二个函数')")
print()
print("print('开始')")
print("first()")
print("second()")
print("print('结束')")
print()

def first():
    print("A: 这是第一个函数")

def second():
    print("B: 这是第二个函数")

print(">>> 开始")
first()
second()
print(">>> 结束")
print()

print("注意：程序从上往下执行，遇到函数定义不执行")
print("      只有调用函数的时候，函数里的代码才会执行！")
print()

# ========================================
# 6. Python 小贴士
# ========================================
print("=" * 50)
print("       💡 Python 小贴士")
print("=" * 50)
print()
print("1. 函数名后面一定要有括号 ()")
print("2. 函数定义后不会自动执行，要调用才行")
print("3. 函数定义要放在调用之前（代码自上而下执行）")
print("4. 函数的代码块要用缩进（4个空格）")
print("5. 用三引号 ''' 可以写函数的说明文档")
print()

# ========================================
# 7. 实践练习
# ========================================
print("=" * 50)
print("       📝 实践练习")
print("=" * 50)
print()

print("🎯 练习：创建你自己的函数")
print()
print("任务：")
print("  1. 创建一个 greet() 函数，打印'你好！欢迎！'")
print("  2. 创建一个 celebrate() 函数，打印生日祝福")
print("  3. 创建一个 show_info() 函数，显示你的名字和年龄")
print()

print("参考代码：")
print("-" * 40)
print()
print("def greet():")
print("    print('=' * 40)")
print("    print('  你好！欢迎来到编程世界！'）")
print("    print('=' * 40)")
print("    print()")
print()
print("def celebrate():")
print("    print('🎂 生日快乐！🎉'）")
print("    print('  祝你天天开心！'）")
print("    print('  心想事成！'）")
print("    print()")
print()
print("def show_info():")
print("    print('=' * 40)")
print("    print('  姓名：小明'）")
print("    print('  年龄：10岁'）")
print("    print('  爱好：编程'）")
print("    print('=' * 40)")
print("    print()")
print()
print("# 调用函数")
print("greet()")
print("celebrate()")
print("show_info()")
print()

# ========================================
# 8. Day 09 总结
# ========================================
print("=" * 60)
print("       📋 Day 09 总结")
print("=" * 60)
print()
print("今天我们学会了：")
print("  ✅ 函数是什么 - 可重复使用的代码块")
print("  ✅ 如何定义函数 - def 函数名():")
print("  ✅ 如何调用函数 - 函数名()")
print("  ✅ 函数可以让代码更有条理")
print()

print("=" * 60)
print("       🎉 Day 09 完成！")
print("=" * 60)
print()
print("太棒了！你学会使用函数了！")
print("函数就像魔法，让你的程序变得超级强大！")
print()
print("明天我们将学习如何给函数传递信息！")
print()
print("===========================================")
print("     💪 继续加油！学习进度：9/21 天完成！")
print("===========================================")
