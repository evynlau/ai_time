# Day 14: 带参数的函数
# 🎯 学习目标：函数可以接收输入
#
# 📖 故事：魔法商店!
# 同一个魔法，不同的输入，不同的结果!

# 咒语 1: 问候某人!
def greet_person(name):
    print("👋 " + name + ", 你好!")
    print("💕 今天也要加油!")

# 咒语 2: 打招呼!
def say_hello(person):
    print(f"🎉 你好，{person}!")
    print(f"😄 很高兴见到你，{person}!")

# 使用咒语!
print("🎁 给小明:")
greet_person("小明")

print()
print("🎁 给小红:")
greet_person("小红")

# 🎮 练习：欢迎函数
def welcome(name):
    return f"👋 欢迎 {name} 来到编程世界!"

message = welcome("小明")
print(message)
message = welcome("小红")
print(message)

# 🎯 小挑战：生日祝福函数
def happy_birthday(name):
    print(f"🎊 {name} 生日快乐!")
    print(f"🎂 祝你快乐每一天!")

happy_birthday("小明")
happy_birthday("小红")
