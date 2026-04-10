# Day 07: True/False - 真假世界
# 🎯 学习目标：理解布尔值 (True, False)
#
# 📖 故事：真假判断题！
# ❓ 问题 1: 太阳从东方升起吗？ → ✅ True
# ❓ 问题 2: 鱼会飞吗？ → ❌ False
# ❓ 问题 3: 7 大于 5 吗？ → ✅ True

# 布尔值只有两种可能
is_sunny = True       # ✅ 是晴天
is_raining = False    # ❌ 不在下雨
is_happy = True       # ✅ 很开心

print(f"☀️ 今天晴天：{is_sunny}")
print(f"🌧️ 今天下雨：{is_raining}")
print(f"😄 今天快乐：{is_happy}")

# 🎮 练习：创建你的布尔值
is_saturday = True
is_school_day = False

if is_saturday:
    print("🎮 周六！可以玩游戏！")
else:
    print("📚 上学日！好好学习！")

# 🎯 小挑战：组合判断
has_homework = False
is_free = True

if has_homework or is_free:
    print("✅ 可以做点自己喜欢的事！")
else:
    print("📚 必须写作业！")
