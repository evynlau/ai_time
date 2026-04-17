# Day 18: 异常处理 - 处理错误 🛡️
# 🎯 学习目标：学会处理程序中的错误
# 📅 适合年龄：12 岁 +
# ⏱️ 建议时长：45 分钟

print("=" * 60)
print("        🐍 Python 编程课程 - Day 18        ")
print("        🛡️ 异常处理 - 处理错误")
print("=" * 60)
print()

# ========================================
# 1. 什么是异常？
# ========================================
print("📖 1. 什么是异常？")
print("-" * 50)
print()

print("想象一下：")
print("  你在用计算器，突然输入了'abc'")
print("  计算器不知道怎么处理，说'出错了！'")
print()
print("💡 异常就是程序运行时发生的错误！")
print("   比如：除以零、访问不存在的文件、输入错误类型")
print()
print("好的程序要能'优雅地'处理这些错误，不崩溃！")
print()

# ========================================
# 2. 常见的异常类型
# ========================================
print("📖 2. 常见的异常类型")
print("-" * 50)
print()

print("  ZeroDivisionError - 除以零")
print("  ValueError       - 值错误（如 int('abc')）")
print("  TypeError        - 类型错误（如 'hello' + 123）")
print("  FileNotFoundError - 文件不存在")
print("  IndexError       - 列表索引超出范围")
print("  KeyError         - 字典键不存在")
print()

# ========================================
# 3. try/except 基本用法
# ========================================
print("📖 3. try/except 基本用法")
print("-" * 50)
print()

print("格式：")
print("  try:")
print("      可能出错的代码")
print("  except:")
print("      出错后执行的代码")
print()

print("示例：")
try:
    result = 10 / 0
except:
    print("  ❌ 出错了！不能除以零！")
print()

# ========================================
# 4. 捕获特定异常
# ========================================
print("📖 4. 捕获特定异常")
print("-" * 50)
print()

print("可以针对不同错误做不同处理：")
print()

def safe_divide(a, b):
    """安全的除法"""
    try:
        result = a / b
        print(f"  ✅ {a} / {b} = {result}")
    except ZeroDivisionError:
        print(f"  ❌ 错误：不能除以零！")
    except TypeError:
        print(f"  ❌ 错误：需要数字类型！")
    except Exception as e:
        print(f"  ❌ 未知错误：{e}")

safe_divide(10, 2)
safe_divide(10, 0)
safe_divide(10, 'a')
print()

# ========================================
# 5. try/except/else
# ========================================
print("📖 5. try/except/else")
print("-" * 50)
print()

print("else：只有当 try 没有出错时才执行")
print()

def get_age():
    """获取年龄（模拟）"""
    age_str = "10"
    try:
        age = int(age_str)
    except ValueError:
        print("  ❌ 输入不是有效的数字！")
    else:
        print(f"  ✅ 成功！年龄是 {age}")
        return age

result = get_age()
print()

# ========================================
# 6. try/except/finally
# ========================================
print("📖 6. try/except/finally")
print("-" * 50)
print()

print("finally：无论是否出错，都会执行（常用于清理工作）")
print()

def read_file_safe(filename):
    """安全读取文件"""
    print(f"  尝试读取：{filename}")
    try:
        with open(filename, 'r') as f:
            content = f.read()
        print(f"  ✅ 读取成功！内容长度：{len(content)}")
    except FileNotFoundError:
        print(f"  ❌ 文件不存在！")
    except PermissionError:
        print(f"  ❌ 没有读取权限！")
    finally:
        print(f"  🔧 清理工作完成（无论成功与否）")

print()
read_file_safe('/tmp/exists.txt')
print()
read_file_safe('/tmp/not_exists.txt')
print()

# ========================================
# 7. raise 主动抛出异常
# ========================================
print("📖 7. raise 主动抛出异常")
print("-" * 50)
print()

def set_age(age):
    """设置年龄（带验证）"""
    if age < 0:
        raise ValueError("年龄不能为负数！")
    if age > 150:
        raise ValueError("年龄太大了！")
    print(f"  ✅ 年龄设置为 {age}")

try:
    set_age(10)
    set_age(-5)
except ValueError as e:
    print(f"  ❌ 错误：{e}")
print()

# ========================================
# 8. 实际应用：输入验证
# ========================================
print("📖 8. 实际应用：输入验证")
print("-" * 50)
print()

def get_positive_number():
    """获取正数（带异常处理）"""
    while True:
        user_input = input("  请输入一个正数：")
        try:
            number = int(user_input)
            if number <= 0:
                print("  ⚠️ 请输入正数！")
                continue
            print(f"  ✅ 成功！您输入的是 {number}")
            return number
        except ValueError:
            print("  ⚠️ 输入无效，请输入数字！")

# 模拟输入（不真正等待用户输入）
print("  模拟输入验证示例：")
try:
    get_positive_number()
except EOFError:
    print("  （非交互环境，跳过实际输入测试）")
print()

# ========================================
# 9. Python 小贴士
# ========================================
print("=" * 50)
print("       💡 Python 小贴士")
print("=" * 50)
print()
print("1. try/except 会影响性能，尽量精确捕获")
print("2. 越具体的异常越好，不要 bare except")
print("3. except Exception as e 可以获取错误信息")
print("4. finally 常用于关闭文件、清理资源")
print("5. raise 可以主动抛出异常，告诉调用者出错了")
print()

# ========================================
# 10. Day 18 总结
# ========================================
print("=" * 60)
print("       📋 Day 18 总结")
print("=" * 60)
print()
print("今天我们学会了：")
print("  ✅ 什么是异常 - 程序运行时的错误")
print("  ✅ try/except - 捕获和处理错误")
print("  ✅ 捕获特定异常 - 针对不同错误做处理")
print("  ✅ else - try 成功时执行")
print("  ✅ finally - 无论成功与否都执行")
print("  ✅ raise - 主动抛出异常")
print()

print("=" * 60)
print("       🎉 Day 18 完成！")
print("=" * 60)
print()
print("太棒了！你的程序现在不会轻易崩溃了！")
print()
print("===========================================")
print("     💪 继续加油！学习进度：18/21 天完成！")
print("===========================================")
