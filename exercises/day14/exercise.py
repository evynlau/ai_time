# Day 14 课后练习题 - 带参数函数
print("练习 1: 带参数的问候")

# 定义带参数的函数
def greet(name):
    print(f"👋 你好，{name}!")
    print(f"💕 {name}，今天也要加油!")

# 使用函数
greet("小明")
greet("小红")
greet("小刚")

# 🎯 挑战：创建生日祝福函数
print("\n🎂 生日祝福函数:")

def birthday_wish(name):
    print(f"🎊 {name} 生日快乐!")
    print(f"🎂 祝你天天快乐!")
    print(f"🎁 祝你学习进步!")

birthday_wish("小明")
birthday_wish("小红")

# 创建年龄祝福函数
print("\n📚 年龄祝福:")

def birthday_age(name, age):
    print(f"🎉 {name} {age} 岁生日快乐!")
    print(f"📖 {age} 岁是很棒的年龄!")

birthday_age("小明", 8)
