# Day 16: while 循环
# 🎯 学习目标：理解 while 循环的作用
#
# 📖 故事：等门铃响
# 门一直会响吗？不知道，用 while!
#
# while 条件:
#     一直做...直到...

# 数到 5
count = 1
while count <= 5:
    print(f"🎈 气球：{count}")
    count = count + 1

print("🎉 气球数完啦！")

# 🎮 练习：猜数字游戏
number = 7
guess = 0

while guess != number:
    guess = int(input("🤔 猜一个数字 (1-10): "))
    if guess < number:
        print("📈 太小了！")
    elif guess > number:
        print("📉 太大了！")

print("🎉 猜对了！")

# 🎯 小挑战：倒计时
print()
print("🚀 倒计时开始:")
countdown = 5
while countdown >= 0:
    print(f"   {countdown}")
    countdown = countdown - 1
print("🎆 发射！")
