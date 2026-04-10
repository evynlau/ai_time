# Day 11: 列表 - 存储多个东西
# 🎯 学习目标：理解列表数据结构
#
# 📖 故事：小明有一个购物清单！
# 他记得住所有东西吗？用列表！

# 什么是列表？
# [ ] 像一排盒子，每个盒子放一个东西
shopping_list = ["苹果", "香蕉", "牛奶", "面包"]
friends = ["小明", "小红", "小华"]

print("📝 购物清单:")
for i, item in enumerate(shopping_list, 1):
    print(f"   {i}. {item}")

print()
print("👫 我的朋友们:")
for name in friends:
    print(f"   👤 {name}")

# 🎮 练习：创建你自己的列表
hobbies = ["读书", "画画", "游泳"]
print(f"🎨 我的爱好：{hobbies}")

# 🎯 小挑战：在列表末尾添加东西
hobbies.append("编程")
print(f"💻 现在爱好有：{hobbies}")
