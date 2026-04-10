# Day 05: 数学运算 - +, -, *, /
# 🎯 学习目标：学习基本数学运算符
#
# 📖 故事：小明的糖果派对！
# 🎉 5 个朋友来玩，每人 3 颗糖，还要给小狗 1 颗

# 运算符：
# + 加法 🍬+🍬=🍬🍬
# - 减法 🍬🍬-🍬=🍬
# * 乘法 🍬×3=3 颗糖
# / 除法 🍬÷2=1 人分享

friends = 5
candy_per_friend = 3
for_dog = 1

# 计算总糖果数
total = friends * candy_per_friend + for_dog
print(f"🎉 糖果派对！共 {total} 颗糖")

# 分给朋友后还剩多少
left = total - (friends * candy_per_friend)
print(f"🐕 小狗还剩 {left} 颗糖")

# 🎮 练习：做你自己的数学题
apples = 10
eaten = 3
remaining = apples - eaten
print(f"🍎 我有 {apples} 个苹果，吃了 {eaten} 个，还剩 {remaining} 个")

# 🎯 小挑战：计算平均值
score1 = 85
score2 = 90
average = (score1 + score2) / 2
print(f"📊 平均成绩：{average}")
