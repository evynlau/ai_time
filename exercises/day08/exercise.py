# Day 08 课后练习题 - 比较大小
print("练习 1: 比较分数")

score1 = 85
score2 = 92

if score2 > score1:
    print(f"🏆 {score2} > {score1}")
elif score1 > score2:
    print(f"🏆 {score1} > {score2}")
else:
    print("🤝 一样!")

# 🎯 挑战：比较年龄
age1 = 10
age2 = 12

print(f"\n👶 小明：{age1}岁")
print(f"👧 小红：{age2}岁")

if age1 >= age2:
    print("✅ 小明至少和小红一样大")
else:
    print("✅ 小明比小红小")

# 判断是否达到法定年龄
min_age = 12
age = 11

if age >= min_age:
    print("🎬 可以看电影!")
else:
    print(f"❌ 还需要等 {min_age - age} 岁")
