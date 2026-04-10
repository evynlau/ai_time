# Day 21: 毕业项目 - 智能问答程序 🎓
# 🎯 学习目标：综合运用所学全部知识
#
# 📖 故事：创建一个能和你对话的程序!

# 定义问候函数
def greet_user(name):
    return f"👋 你好，{name}! 欢迎来到编程世界"

# 定义计算函数
def calculate_sum(a, b):
    return a + b

# 主程序
print("🎓 Python 编程学习完成!")
print("🌟 恭喜你已经学会了:")
print("   ✅ print())
print("   ✅ 变量和赋值")
print("   ✅ 数据类型")
print("   ✅ 条件判断")
print("   ✅ for and while 循环")
print("   ✅ 列表和字典")
print("   ✅ 函数定义和调用")

# 创建你的第一个程序
print()
print("🚀 现在来测试你的程序!")

# 询问用户名字
name = "小明"  # 在真实程序中会用 input()
print(greet_user(name))

# 计算练习
num1 = 10
num2 = 20
result = calculate_sum(num1, num2)
print(f"📊 {num1} + {num2} = {result}")

# 学生字典
student = {
    "name": "小明",
    "age": 8,
    "grade": "小学三年级",
    "favorite": "编程"
}

print(f"👤 学生信息:")
print(f"    姓名：{student['name']}")
print(f"    年龄：{student['age']}岁")
print(f"    年级：{student['grade']}")
print(f"    最爱：{student['favorite']}")

# 游戏循环
print()
print("🎮 开始猜数字游戏!")
import random
target = random.randint(1, 10)
guess = 0
attempts = 0

while guess != target and attempts < 5:
    guess = int(input("猜一个 1-10 的数字: "))
    attempts += 1
    if guess < target:
        print("📈 太小了！")
    elif guess > target:
        print("📉 太大了！")

if guess == target:
    print(f"🎉 恭喜你！猜对了！共用了 {attempts} 次")
else:
    print(f"😅 游戏结束！答案是 {target}")

print()
print("🎊 恭喜你！你已经完成了 21 天的 Python 学习!")
print("🌟 继续加油，成为编程小达人！✨")
