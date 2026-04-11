#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Day 7 参考答案 - 编程小天才挑战！
"""

# === 练习 1: 测试你的加法函数 ===
def test_addition(num1, num2):
    return num1 + num2

# 测试
result = test_addition(10, 20)
print(f"10 + 20 = {result}")  # 输出: 30
print()

# === 练习 2: 完成减法函数 ===
def test_subtraction(num1, num2):
    if num1 < num2:
        return "不能相减，num1 较小"
    else:
        return num1 - num2

# 测试
print(test_subtraction(10, 5))   # 输出: 5
print(test_subtraction(5, 10))   # 输出: "不能相减，num1 较小"
print()

# === 练习 3: 处理除法中的零 ===
def test_division(num1, num2):
    if num2 == 0:
        return "错误：除数不能为 0!"
    else:
        return num1 / num2

# 测试
print(test_division(20, 4))      # 输出: 5.0
print(test_division(10, 0))      # 输出: "错误：除数不能为 0!"
print()

# === 练习 4: 编写乘法表生成器 ===
def generate_multiplication_table(number):
    for i in range(1, 11):
        print(f"{number} × {i} = {number * i}")

# 测试
print("3 的乘法表:")
generate_multiplication_table(3)
print()

# === 练习 5: 创建密码验证器 ===
import math

def calculate_square_root(number):
    if number < 0:
        return "错误：不能计算负数的平方根"
    else:
        return math.sqrt(number)

# 测试
print(calculate_square_root(16))     # 输出: 4.0
print(calculate_square_root(-4))     # 输出: "错误：不能计算负数的平方根"
print()

# === 练习 6: 编写幂运算函数 ===
def power(base, exponent):
    return base ** exponent

# 测试
print(power(2, 3))   # 输出: 8 (2³ = 8)
print(power(5, 2))   # 输出: 25 (5² = 25)
print(power(3, 0))   # 输出: 1 (任何数的 0 次方等于 1)
print()

# === 练习 7: 创建成绩评分器 ===
def grade(score):
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

# 测试
print(grade(95))     # 输出: 'A'
print(grade(85))     # 输出: 'B'
print(grade(72))     # 输出: 'C'
print(grade(65))     # 输出: 'D'
print(grade(45))     # 输出: 'F'
print()

# === 练习 8: 编写密码验证器 ===
def check_password(password):
    # 检查长度
    if len(password) < 8:
        return "密码不安全"
    
    # 检查是否包含数字
    has_digit = False
    for char in password:
        if char.isdigit():
            has_digit = True
            break
    
    # 检查是否包含大写字母
    has_upper = False
    for char in password:
        if char.isupper():
            has_upper = True
            break
    
    if has_digit and has_upper:
        return "密码安全"
    else:
        return "密码不安全"

# 测试
print(check_password("MyPass123"))     # 输出："密码安全"
print(check_password("short1"))        # 输出："密码不安全"
print(check_password("NoNumber"))      # 输出："密码不安全"
print(check_password("NoCapital1"))    # 输出："密码不安全"
print(check_password("abc"))           # 输出："密码不安全"
print()

# === 练习 9: 计算列表平均值 ===
def calculate_average(scores):
    if len(scores) == 0:
        return 0
    return sum(scores) / len(scores)

# 测试
scores = [85, 90, 78, 92, 88]
print(f"平均分：{calculate_average(scores)}")  # 输出：86.6
print()

# === 练习 10: 创建猜数字游戏 ===
import random

def guessing_game():
    number_to_guess = random.randint(1, 100)
    guess = 0
    attempts = 0
    
    print("我已经想好了一个 1-100 之间的数字，来猜猜看！")
    
    while guess != number_to_guess:
        guess = int(input("请输入你的猜测："))
        attempts += 1
        
        if guess < number_to_guess:
            print("太小了！")
        elif guess > number_to_guess:
            print("太大了！")
        else:
            print(f"恭喜你！猜对了！数字是 {number_to_guess}")
            print(f"你猜了 {attempts} 次")
    
    return attempts

# 运行游戏
# guessing_game()  # 取消注释来运行游戏

# === 进阶挑战 ===

# 挑战 A: 科学计算器
def scientific_calculator():
    """添加更多功能"""
    print("\n--- 科学计算器功能测试 ---")
    print(f"绝对值：abs(-5) = {abs(-5)}")
    print(f"最大值：max(1, 5, 3, 9, 2) = {max(1, 5, 3, 9, 2)}")
    print(f"最小值：min(1, 5, 3, 9, 2) = {min(1, 5, 3, 9, 2)}")
    print(f"四舍五入：round(3.6) = {round(3.6)}")
    print(f"平方根：math.sqrt(16) = {math.sqrt(16)}")

# 挑战 B: 分数计算器
from fractions import Fraction

def fraction_calculator():
    """分数计算器"""
    print("\n--- 分数计算器 ---")
    frac1 = Fraction(1, 2)  # 1/2
    frac2 = Fraction(1, 4)  # 1/4
    
    print(f"1/2 + 1/4 = {frac1 + frac2}")
    print(f"1/2 - 1/4 = {frac1 - frac2}")
    print(f"1/2 × 1/4 = {frac1 * frac2}")
    print(f"1/2 ÷ 1/4 = {frac1 / frac2}")

# 挑战 C: 货币转换器
def currency_converter():
    """货币转换器"""
    print("\n--- 货币转换器 ---")
    
    usd_to_cny = 7.2  # 汇率
    
    # 美元转人民币
    usd_amount = 100
    cny_amount = usd_amount * usd_to_cny
    print(f"{usd_amount} USD = {cny_amount} CNY")
    
    # 人民币转美元
    cny_amount = 720
    usd_amount = cny_amount / usd_to_cny
    print(f"{cny_amount} CNY = {usd_amount:.2f} USD")

# 运行挑战
# scientific_calculator()
# fraction_calculator()
# currency_converter()

print("\n🎉 恭喜你完成所有练习！")
