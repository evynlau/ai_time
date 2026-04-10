# Day 06: 条件判断 - 做决定
# 🎯 学习目标：理解 if-elif-else 语句
#
# 📖 故事：天气判断机器人
# ☀️ 如果下雨 → 带伞
# 🌤️ 如果晴天 → 戴帽子
# ☁️ 否则 → 穿外套

# 条件判断：
weather = "rain"

if weather == "rain":
    print("☂️ 下雨了！记得带伞！")
elif weather == "sun":
    print("☀️ 阳光明媚！戴帽子出去玩！")
else:
    print("☁️ 阴天，穿件外套吧！")

# 🎮 练习：温度判断
temperature = 25

if temperature > 30:
    print("🥵 好热！吃冰淇淋吧！")
elif temperature < 10:
    print("🥶 好冷！穿厚衣服！")
else:
    print("😊 天气刚刚好！出去走走！")

# 🎯 小挑战：创建一个自己的判断
score = 85
if score >= 90:
    print("🏆 优秀！得到星星！")
elif score >= 70:
    print("👍 良好！继续加油！")
else:
    print("💪 加油！下次会更好！")
