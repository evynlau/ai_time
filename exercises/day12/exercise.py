# Day 12 课后练习题 - 列表操作
print("练习 1: 列表操作")

# 创建水果列表
fruits = ["🍎 苹果", "🍌 香蕉", "🍇 葡萄", "🍊 橘子"]

print("🍓 水果列表:")
for i, fruit in enumerate(fruits, 1):
    print(f"   {i}. {fruit}")

# 🎯 挑战：取出特定水果
print("\n🔍 取出第 2 个水果:")
print(f"   {fruits[1]}")

print("\n🔍 取出最后一个水果:")
print(f"   {fruits[-1]}")

# 添加新水果
print("\n🍓 添加西瓜:")
fruits.append("🍉 西瓜")
print(f"   更新后：{fruits}")

# 查看数量
print(f"\n📊 共有 {len(fruits)} 种水果")
