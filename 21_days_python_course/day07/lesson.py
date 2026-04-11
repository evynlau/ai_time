#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Day 7: 编程小天才项目 - 我的第一台计算器 🧮
================================================
复习 Day1-6 的知识，创建一个实用的计算器程序！

学习重点：
✅ 变量和数据类型
✅ 运算符和表达式
✅ 输入输出
✅ 条件语句 (if-else)
✅ 循环 (for, while)
"""

print("🎉 欢迎使用'编程小天才'计算器！")
print("=" * 50)
print("今天我们要创建一个实用的计算器程序！")
print("=" * 50)

# ========================================
# 📚 复习知识点
# ========================================

print("\n🔍 我们先来复习一下学过的知识:")
print("-" * 50)

# 1. 变量和赋值
age = 8
print(f"年龄：{age}岁")

favorite_color = "蓝色"
print(f"喜欢的颜色：{favorite_color}")

is_smart = True
print(f"我聪明吗？{is_smart}")

# 2. 基本运算
width = 5
height = 3
area = width * height
print(f"\n长方形面积: {width} × {height} = {area}")

# 3. 比较运算
score = 85
print(f"\n分数：{score}")
print(f"分数>=60: {score >= 60}")
print(f"分数>90: {score > 90}")

print("-" * 50)

# ========================================
# 🎯 项目目标：创建计算器
# ========================================

print("\n🤖 今天的项目：建造一个计算器机器人！")
print("它需要能够:")
print("  ✔️ 加法")
print("  ✔️ 减法")
print("  ✔️ 乘法")
print("  ✔️ 除法")
print("  ✔️ 求余数")

# ========================================
# 🛠️ 编写计算器
# ========================================

print("\n" + "=" * 50)
print("开始编写计算器代码...")
print("=" * 50)

def add_num(a, b):
    """加法函数"""
    return a + b

def subtract_num(a, b):
    """减法函数"""
    return a - b

def multiply_num(a, b):
    """乘法函数"""
    return a * b

def divide_num(a, b):
    """除法函数"""
    if b == 0:
        return "❌ 除数不能为 0!"
    return a / b

def modulo_num(a, b):
    """求余数函数"""
    if b == 0:
        return "❌ 除数不能为 0!"
    return a % b

# 测试计算器功能
print("\n🔧 测试计算器功能:")
print(f"  3 + 5 = {add_num(3, 5)}")
print(f"  10 - 4 = {subtract_num(10, 4)}")
print(f"  6 × 7 = {multiply_num(6, 7)}")
print(f"  20 ÷ 4 = {divide_num(20, 4)}")
print(f"  17 % 5 = {modulo_num(17, 5)}")

# 创建交互式的计算器程序
print("\n" + "=" * 50)
print("创建交互式计算器...")
print("=" * 50)

def calculator_app():
    """交互式计算器应用程序"""
    while True:
        print("\n" + "-" * 50)
        print("🔢 编程小天才计算器")
        print("-" * 50)
        print("请选择运算:")
        print("1️⃣ 加法 (+)")
        print("2️⃣ 减法 (-)")
        print("3️⃣ 乘法 (×)")
        print("4️⃣ 除法 (÷)")
        print("5️⃣ 求余数 (%)")
        print("0️⃣ 退出程序")
        print("-" * 50)
        
        # 获取用户选择
        choice = input("请输入选项 (0-5): ")
        
        # 根据选择执行不同操作
        if choice == "0":
            print("\n👋 感谢使用编程小天才计算器！再见！")
            break
        elif choice in "12345":
            # 获取两个数字
            num1 = float(input("请输入第一个数字: "))
            num2 = float(input("请输入第二个数字: "))
            
            # 执行计算
            if choice == "1":
                result = add_num(num1, num2)
                print(f"  ✅ 结果: {num1} + {num2} = {result}")
            elif choice == "2":
                result = subtract_num(num1, num2)
                print(f"  ✅ 结果: {num1} - {num2} = {result}")
            elif choice == "3":
                result = multiply_num(num1, num2)
                print(f"  ✅ 结果: {num1} × {num2} = {result}")
            elif choice == "4":
                result = divide_num(num1, num2)
                print(f"  ✅ 结果: {num1} ÷ {num2} = {result}")
            elif choice == "5":
                result = modulo_num(num1, num2)
                print(f"  ✅ 结果: {num1} % {num2} = {result}")
        else:
            print("❌ 请输入有效的选项 (0-5)!")

# ========================================
# 💡 知识拓展
# ========================================

print("\n" + "=" * 50)
print("💡 知识拓展：循环和列表")
print("=" * 50)

# 循环运算
print("\n使用循环执行多次计算:")
for i in range(1, 6):
    print(f"  {i} × 2 = {multiply_num(i, 2)}")

# 列表存储结果
results = [add_num(1, 2), add_num(3, 4), add_num(5, 6)]
print(f"\n保存的计算结果: {results}")
print(f"总和: {sum(results)}")

# ========================================
# 🌟 项目完成!
# ========================================

print("\n" + "=" * 50)
print("🎉 恭喜！你已经完成了编程小天才计算器!")
print("=" * 50)
print("\n📝 今天学过的知识点:")
print("  ✅ 定义和使用函数")
print("  ✅ 参数和返回值")
print("  ✅ 条件判断 (if-else)")
print("  ✅ 循环 (while, for)")
print("  ✅ 用户输入和输出")
print("  ✅ 错误处理 (除数不能为 0)")
print("\n🎯 下一步:")
print("  尝试修改计算器，添加:")
print("  - 乘法表功能")
print("  - 平方根计算")
print("  - 幂运算")

print("\n" + "=" * 50)
print("✨ 编程小天才，你真棒！")
print("=" * 50)
