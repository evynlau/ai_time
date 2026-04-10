# Day 15 课后练习题 - 返回值函数
print("练习 1: 创建函数并获取返回值")

# 定义计算函数
def add(a, b):
    result = a + b
    return result

# 使用返回值
sum_result = add(5, 7)
print(f"📊 5 + 7 = {sum_result}")

sum_result = add(10, 20)
print(f"📊 10 + 20 = {sum_result}")

# 🎯 挑战：创建乘法函数
print("\n✖️ 乘法函数:")

def multiply(x, y):
    result = x * y
    return result

product = multiply(3, 4)
print(f"3 × 4 = {product}")

# 创建问候函数
print("\n👋 问候函数:")

def greet_user(user):
    message = f"👋 你好，{user}! 欢迎来到编程世界"
    return message

msg = greet_user("小明")
print(msg)

msg = greet_user("小红")
print(msg)
