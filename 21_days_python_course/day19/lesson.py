# Day 19: 综合练习 - 小游戏开发 🎮
# 🎯 学习目标：综合运用所学知识，开发一个完整的小游戏
# 📅 适合年龄：12 岁 +
# ⏱️ 建议时长：50 分钟

print("=" * 60)
print("        🐍 Python 编程课程 - Day 19        ")
print("        🎮 综合练习 - 小游戏开发")
print("=" * 60)
print()

# ========================================
# 1. 今天我们要做什么？
# ========================================
print("📖 1. 今天我们要做什么？")
print("-" * 50)
print()

print("经过 18 天的学习，我们已经学会了：")
print("  ✅ 变量和数据类型")
print("  ✅ 条件判断")
print("  ✅ 循环（for 和 while）")
print("  ✅ 列表和字典")
print("  ✅ 函数")
print("  ✅ 文件操作")
print("  ✅ 异常处理")
print()
print("💡 今天，我们将综合运用这些知识，")
print("   开发一个完整的猜数字游戏！")
print()

# ========================================
# 2. 游戏设计
# ========================================
print("📖 2. 游戏设计")
print("-" * 50)
print()

print("🎯 猜数字游戏规则：")
print("  1. 程序随机选择一个 1-100 的数字")
print("  2. 玩家有 5 次猜测机会")
print("  3. 每次猜测后，程序提示'太大'或'太小'")
print("  4. 猜对或次数用完，游戏结束")
print()

print("🏆 附加功能（可选挑战）：")
print("  - 记录最高分（最少猜测次数）")
print("  - 支持多人玩家")
print("  - 从文件保存和读取最高分")
print()

# ========================================
# 3. 基础版本
# ========================================
print("📖 3. 基础版本")
print("-" * 50)
print()

import random

def guess_number_game():
    """猜数字游戏 - 基础版"""
    secret = random.randint(1, 100)
    attempts = 0
    max_attempts = 5

    print("=" * 40)
    print("       🎯 猜数字游戏 🎯")
    print("=" * 40)
    print(f"我已经想好了一个 1-100 之间的数字")
    print(f"你有 {max_attempts} 次机会，加油！")
    print()

    while attempts < max_attempts:
        remaining = max_attempts - attempts
        print(f"剩余 {remaining} 次机会")

        try:
            guess = int(input("请输入你的猜测："))
        except ValueError:
            print("⚠️ 请输入有效的数字！")
            continue

        attempts += 1

        if guess == secret:
            print(f"🎉 恭喜你！猜对了！答案是 {secret}")
            print(f"你用了 {attempts} 次猜测")
            return True
        elif guess < secret:
            print("📈 太小了！再大一点！")
        else:
            print("📉 太大了！再小一点！")

    print(f"😢 次数用完了！正确答案是 {secret}")
    return False

# 运行游戏
guess_number_game()
print()

# ========================================
# 4. 进阶版本：带最高分
# ========================================
print("📖 4. 进阶版本：带最高分记录")
print("-" * 50)
print()

def guess_number_with_score():
    """猜数字游戏 - 带分数版"""
    secret = random.randint(1, 100)
    attempts = 0
    max_attempts = 5

    print("=" * 40)
    print("       🏆 猜数字 - 挑战模式 🏆")
    print("=" * 40)
    print(f"你有 {max_attempts} 次机会")
    print()

    while attempts < max_attempts:
        remaining = max_attempts - attempts
        try:
            guess_str = input(f"剩余 {remaining} 次 - 请输入猜测：")
            guess = int(guess_str)
        except ValueError:
            print("⚠️ 请输入有效的数字！")
            continue

        attempts += 1

        if guess == secret:
            score = max_attempts - attempts + 1
            print(f"🎉 恭喜！用了 {attempts} 次，得分：{score * 20}")
            return score
        elif guess < secret:
            print("📈 太小了！")
        else:
            print("📉 太大了！")

    print(f"😢 正确答案是 {secret}")
    return 0

score = guess_number_with_score()
print()

# ========================================
# 5. 完整版本：带存档
# ========================================
print("📖 5. 完整版本：带存档功能")
print("-" * 50)
print()

import json

def load_high_score():
    """从文件加载最高分"""
    try:
        with open('/tmp/guess_game_score.json', 'r') as f:
            data = json.load(f)
            return data.get('high_score', 0), data.get('best_player', '')
    except:
        return 0, ''

def save_high_score(score, player_name):
    """保存最高分到文件"""
    try:
        with open('/tmp/guess_game_score.json', 'w') as f:
            json.dump({
                'high_score': score,
                'best_player': player_name
            }, f)
    except:
        pass

def guess_number_full():
    """猜数字游戏 - 完整版"""
    secret = random.randint(1, 100)
    attempts = 0
    max_attempts = 5

    high_score, best_player = load_high_score()
    print("=" * 40)
    print("       🌟 猜数字 - 完整版 🌟")
    print("=" * 40)
    print(f"最高分：{high_score} 分（{best_player}）")
    print()

    player_name = input("请输入你的名字：") or "玩家"

    while attempts < max_attempts:
        remaining = max_attempts - attempts
        try:
            guess = int(input(f"剩余 {remaining} 次 - 请猜测："))
        except ValueError:
            print("⚠️ 请输入有效数字！")
            continue

        attempts += 1

        if guess == secret:
            score = (max_attempts - attempts + 1) * 20
            print(f"🎉 恭喜 {player_name}！得分：{score}")
            if score > high_score:
                save_high_score(score, player_name)
                print("🏆 新纪录！最高分已保存！")
            return True
        elif guess < secret:
            print("📈 太小了！")
        else:
            print("📉 太大了！")

    print(f"😢 正确答案是 {secret}")
    return False

# 完整版演示
print("--- 完整版游戏演示 ---")
try:
    guess_number_full()
except EOFError:
    print("（非交互环境，跳过演示）")
print()

# ========================================
# 6. Python 小贴士
# ========================================
print("=" * 50)
print("       💡 Python 小贴士")
print("=" * 50)
print()
print("1. 综合练习是提升编程能力的最好方式！")
print("2. 先设计再编码，先简单再复杂")
print("3. 函数让代码更有条理")
print("4. 异常处理让程序更健壮")
print("5. 文件操作让数据永久保存")
print()

# ========================================
# 7. Day 19 总结
# ========================================
print("=" * 60)
print("       📋 Day 19 总结")
print("=" * 60)
print()
print("今天我们完成了：")
print("  ✅ 猜数字游戏 - 基础版")
print("  ✅ 猜数字游戏 - 进阶版（带分数）")
print("  ✅ 猜数字游戏 - 完整版（带存档）")
print("  ✅ 综合运用所有学过的知识")
print()

print("🎯 课后挑战：")
print("  1. 添加'再来一局'功能")
print("  2. 添加难度选择（简单/普通/困难）")
print("  3. 制作一个石头剪刀布游戏")
print()

print("=" * 60)
print("       🎉 Day 19 完成！")
print("=" * 60)
print()
print("太棒了！你已经是一个小程序员了！")
print()
print("===========================================")
print("     💪 继续加油！学习进度：19/21 天完成！")
print("===========================================")
