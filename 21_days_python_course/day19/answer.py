# Day 19: 综合练习 - 小游戏开发 - 参考答案
print("=" * 50)
print("       ✅ Day 19 参考答案")
print("=" * 50)
print()

import random

# ========================================
# 练习 1: 完善猜数字游戏
# ========================================
print("📝 练习 1: 完善猜数字游戏")
print("-" * 40)
print()

def guess_number_basic():
    """基础猜数字游戏"""
    secret = random.randint(1, 50)
    max_attempts = 5

    print("🎯 猜 1-50 之间的数字，你有 5 次机会！")

    for attempt in range(max_attempts):
        guess = int(input(f"第 {attempt + 1} 次 - 请输入："))
        if guess == secret:
            print(f"🎉 猜对了！用了 {attempt + 1} 次")
            return
        elif guess < secret:
            print("  太小了！")
        else:
            print("  太大了！")

    print(f"正确答案是 {secret}")

print("✅ 练习 1 完成！")
print()

# ========================================
# 练习 2: 石头剪刀布游戏
# ========================================
print("📝 练习 2: 石头剪刀布游戏")
print("-" * 40)
print()

def rock_paper_scissors():
    """石头剪刀布"""
    options = ['石头', '剪刀', '布']
    user_choice = input("请选择（石头/剪刀/布）：")
    if user_choice not in options:
        print("无效选择！")
        return

    computer = random.choice(options)
    print(f"你出：{user_choice}")
    print(f"电脑出：{computer}")

    if user_choice == computer:
        print("结果：平局！")
    elif (user_choice == '石头' and computer == '剪刀') or \
         (user_choice == '剪刀' and computer == '布') or \
         (user_choice == '布' and computer == '石头'):
        print("结果：你赢！🎉")
    else:
        print("结果：电脑赢！")

print("✅ 练习 2 完成！")
print()

# ========================================
# 练习 3: 问答游戏
# ========================================
print("📝 练习 3: 问答游戏")
print("-" * 40)
print()

questions = [
    {'q': '1+1等于几？', 'a': '2'},
    {'q': '世界上最大的动物是什么？', 'a': '蓝鲸'},
    {'q': '中国的首都是哪里？', 'a': '北京'},
]

score = 0
for item in questions:
    print(f"问题：{item['q']}")
    answer = input("你的答案：")
    if answer.strip() == item['a']:
        print("✅ 正确！")
        score += 1
    else:
        print(f"❌ 错误！正确答案是：{item['a']}")

print(f"\n最终得分：{score}/{len(questions)}")
print("✅ 练习 3 完成！")
print()

# ========================================
# 练习 4: 待办事项管理器
# ========================================
print("📝 练习 4: 待办事项管理器")
print("-" * 40)
print()

todos = []

def add_todo():
    item = input("请输入待办事项：")
    todos.append(item)
    print(f"✅ 已添加：{item}")

def view_todos():
    if not todos:
        print("暂无待办事项！")
    else:
        for i, item in enumerate(todos, 1):
            print(f"  {i}. {item}")

def delete_todo():
    view_todos()
    try:
        idx = int(input("请输入要删除的编号："))
        removed = todos.pop(idx - 1)
        print(f"✅ 已删除：{removed}")
    except:
        print("❌ 无效编号！")

# 演示
add_todo()
add_todo()
add_todo()
view_todos()
delete_todo()
print("✅ 练习 4 完成！")
print()

# ========================================
# 练习 5: 简单计算器
# ========================================
print("📝 练习 5: 简单计算器")
print("-" * 40)
print()

def calculator():
    operations = {
        '1': ('加法', lambda a, b: a + b),
        '2': ('减法', lambda a, b: a - b),
        '3': ('乘法', lambda a, b: a * b),
        '4': ('除法', lambda a, b: a / b if b != 0 else '错误'),
    }

    print("简易计算器")
    for k, (name, _) in operations.items():
        print(f"  {k}. {name}")

    choice = input("选择操作：")
    if choice not in operations:
        print("无效选择！")
        return

    name, op = operations[choice]
    try:
        a = float(input("第一个数："))
        b = float(input("第二个数："))
        result = op(a, b)
        print(f"结果：{result}")
    except:
        print("输入错误！")

calculator()
print()
print("✅ 练习 5 完成！")
print()

# ========================================
# 知识点总结
# ========================================
print("=" * 50)
print("       📊 Day 19 知识点总结")
print("=" * 50)
print()
print("✅ 综合运用所有学过的知识")
print("✅ 函数的定义和调用")
print("✅ 循环和条件判断")
print("✅ 列表和字典的使用")
print("✅ 异常处理 try/except")
print("✅ 简单的游戏逻辑设计")
print()
print("🎉 恭喜完成所有练习！")
print()
