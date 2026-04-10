# Day 15: 函数返回值
# 🎯 学习目标：理解 return 的概念
#
# 📖 故事：魔法商店!
# 念完咒语，会给你一件"魔法物品"

# 咒语：加法魔法!
def add_two(num1, num2):
    # 计算并返回结果
    total = num1 + num2
    return total  # 把结果给你!

# 使用咒语!
result1 = add_two(3, 5)
result2 = add_two(10, 20)

print(f"3 + 5 = {result1}")
print(f"10 + 20 = {result2}")

print()
print(f"两个结果的和：{result1 + result2}")

# 🎮 练习：问候返回函数
def say_greeting(name):
    return f"👋 {name}, 你好世界!"

message = say_greeting("小明")
print(message)
print(say_greeting("小红"))

# 🎯 小挑战：乘法魔法
def multiply(a, b):
    result = a * b
    return result

product = multiply(4, 5)
print(f"4 × 5 = {product}")
