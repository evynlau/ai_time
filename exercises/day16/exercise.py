# Day 16 课后练习题 - while 循环
print("练习 1: 猜数字游戏")

# 定义目标数字
target = 7
guess = 0

print("🎮 猜一个 1-10 的数字:")

while guess != target:
    guess = int(input("你的猜测："))
    if guess < target:
        print("📈 太小了!", end=" ")
    elif guess > target:
        print("📉 太大了!", end=" ")

print("\n🎉 恭喜你! 猜对了!")

# 🎯 挑战：倒计时
print("\n🚀 倒计时:")

countdown = 5
while countdown >= 0:
    print(f"   {countdown}")
    countdown = countdown - 1

print("   🚀 发射!")

# 挑战 2: 累加和
print("\n➕ 累加计算:")
total = 0
counter = 1
while counter <= 5:
    total = total + counter
    print(f"   累加到 {counter}: {total}")
    counter = counter + 1

print(f"\n最终总和：{total}")
