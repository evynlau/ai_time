# Day 18: 异常处理 - 练习
print("=" * 50)
print("       📝 Day 18 练习：异常处理")
print("=" * 50)
print()

# ========================================
# 练习 1: 基本 try/except
# ========================================
print("🎯 练习 1: 基本 try/except")
print("-" * 40)
print()

def safe_divide(a, b):
    """安全的除法"""
    try:
        result = a / b
        print(f"  {a} / {b} = {result}")
    except:
        print(f"  ❌ 出错了！")

safe_divide(10, 2)
safe_divide(10, 0)
print("✅ 练习 1 完成！")
print()

# ========================================
# 练习 2: 捕获特定异常
# ========================================
print("🎯 练习 2: 捕获特定异常")
print("-" * 40)
print()

def convert_to_int(value):
    """安全转换为整数"""
    try:
        number = int(value)
        print(f"  ✅ 转换成功：{number}")
        return number
    except ValueError:
        print(f"  ❌ ValueError：'{value}' 不是有效数字")
    except TypeError:
        print(f"  ❌ TypeError：类型不支持转换")

convert_to_int("123")
convert_to_int("hello")
convert_to_int(None)
print("✅ 练习 2 完成！")
print()

# ========================================
# 练习 3: try/except/else
# ========================================
print("🎯 练习 3: try/except/else")
print("-" * 40)
print()

def calculate_square(number):
    """计算平方"""
    try:
        result = number ** 2
    except TypeError:
        print("  ❌ 类型错误！需要数字")
    else:
        print(f"  ✅ 平方计算成功：{number}^2 = {result}")
        return result

calculate_square(5)
calculate_square("hello")
print("✅ 练习 3 完成！")
print()

# ========================================
# 练习 4: try/except/finally
# ========================================
print("🎯 练习 4: try/except/finally")
print("-" * 40)
print()

def process_file(filename):
    """处理文件"""
    print(f"  处理文件：{filename}")
    try:
        with open(filename, 'r') as f:
            content = f.read()
        print(f"  ✅ 读取成功，长度：{len(content)}")
    except FileNotFoundError:
        print(f"  ❌ 文件不存在")
    except PermissionError:
        print(f"  ❌ 没有权限")
    finally:
        print(f"  🔧 清理完成")

print()
process_file('/tmp/test.txt')

# 创建临时文件再测试
with open('/tmp/test.txt', 'w') as f:
    f.write('Hello')
print()
process_file('/tmp/test.txt')
print("✅ 练习 4 完成！")
print()

# ========================================
# 练习 5: raise 主动抛出异常
# ========================================
print("🎯 练习 5: raise 主动抛出异常")
print("-" * 40)
print()

def validate_age(age):
    """验证年龄"""
    if age < 0:
        raise ValueError("年龄不能为负数！")
    if age > 120:
        raise ValueError("年龄超出合理范围！")
    print(f"  ✅ 年龄 {age} 验证通过")

try:
    validate_age(10)
    validate_age(-5)
except ValueError as e:
    print(f"  ❌ 错误：{e}")

try:
    validate_age(200)
except ValueError as e:
    print(f"  ❌ 错误：{e}")
print("✅ 练习 5 完成！")
print()

# ========================================
# 练习 6: 综合验证函数
# ========================================
print("🎯 练习 6: 综合验证函数")
print("-" * 40)
print()

def divide_numbers(a, b):
    """安全的除法运算"""
    try:
        # 先尝试转换
        a = float(a)
        b = float(b)
    except (ValueError, TypeError):
        return "错误：参数需要是数字"
    
    try:
        result = a / b
    except ZeroDivisionError:
        return "错误：不能除以零"
    
    return f"结果：{result}"

tests = [
    (10, 2),
    (10, 0),
    (10, 'a'),
    ('abc', 5),
]

for a, b in tests:
    print(f"  divide({a}, {b}) = {divide_numbers(a, b)}")
print("✅ 练习 6 完成！")
print()

# ========================================
# 练习 7: 访问字典的安全方法
# ========================================
print("🎯 练习 7: 访问字典的安全方法")
print("-" * 40)
print()

def safe_get(d, key, default=None):
    """安全获取字典值"""
    try:
        return d[key]
    except KeyError:
        print(f"  ⚠️ 键 '{key}' 不存在，返回默认值")
        return default

info = {'name': '小明', 'age': 10}

print(f"  name: {safe_get(info, 'name')}")
print(f"  hobby: {safe_get(info, 'hobby', '未知')}")
print(f"  city: {safe_get(info, 'city')}")
print("✅ 练习 7 完成！")
print()

# ========================================
# 完成
# ========================================
print("=" * 50)
print("       ✅ 所有练习完成！")
print("=" * 50)
print()
print("今天学到了：")
print("  ✅ try/except 捕获异常")
print("  ✅ 捕获特定异常类型")
print("  ✅ else 只在成功时执行")
print("  ✅ finally 无论如何都执行")
print("  ✅ raise 主动抛出异常")
print()
print("🎉 明天进行综合练习！")
print()
