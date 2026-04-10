# Day 08: 比较大小
# 🎯 学习目标：学习 > < == 等比较符号
#
# 📖 故事：谁跑得更快？
# 小明跑了 100 米，小红跑了 120 米
# 120 > 100 → 小红跑得远！

# 比较符号：
# >   大于
# <   小于
# ==  等于
# >=  大于等于
# <=  小于等于
# !=  不等于

score1 = 85
score2 = 90

print(f"📝 测试 1: {score1}分")
print(f"📝 测试 2: {score2}分")

if score2 > score1:
    print(f"🏆 {score2} > {score1} - 第二题更好!")
elif score1 == score2:
    print("🤝 一样好!")
else:
    print("🎉 第一题做得更好!")

# 🎮 练习：年龄判断
age = 10
min_age = 12

if age >= min_age:
    print("✅ 可以看电影了!")
else:
    print(f"❌ 还需要等 {min_age - age} 岁!")

# 🎯 小挑战：比较两个数字
num1 = 15
num2 = 20

if num1 != num2:
    print(f"🔢 {num1} ≠ {num2}")
    if num1 > num2:
        print(f"❌ {num1} 比 {num2} 小")
    else:
        print(f"✅ {num1} 比 {num2} 大")
