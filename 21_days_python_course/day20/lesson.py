# Day 20: 毕业项目 - 智能问答程序 🤖
# 🎯 学习目标：综合所学知识，开发一个完整的智能问答程序
# 📅 适合年龄：12 岁 +
# ⏱️ 建议时长：50 分钟

print("=" * 60)
print("        🐍 Python 编程课程 - Day 20        ")
print("        🤖 毕业项目 - 智能问答程序")
print("=" * 60)
print()

# ========================================
# 1. 今天我们要做什么？
# ========================================
print("📖 1. 今天我们要做什么？")
print("-" * 50)
print()

print("🎓 经过 19 天的学习，今天我们将完成一个毕业项目！")
print()
print("💡 智能问答程序功能：")
print("  ✅ 有一个问题知识库（字典存储）")
print("  ✅ 用户可以提问")
print("  ✅ 程序自动匹配答案")
print("  ✅ 可以添加新问题和答案")
print("  ✅ 支持文件保存和加载")
print()

# ========================================
# 2. 设计知识库
# ========================================
print("📖 2. 设计知识库")
print("-" * 50)
print()

knowledge_base = {
    "你好": "你好！有什么我可以帮助你的吗？",
    "你叫什么名字": "我叫小天才，一个智能问答机器人！",
    "今天天气怎么样": "今天天气很好，适合学习编程！",
    "Python是什么": "Python是一种计算机编程语言，简单易学！",
    "再见": "再见！祝你有美好的一天！",
    "你几岁了": "我刚出生，还是一个小宝宝呢！",
    "2+2等于多少": "2+2=4，很简单吧！",
    "中国在哪里": "中国在亚洲，是世界上人口最多的国家！",
}

print("初始知识库：")
for q, a in knowledge_base.items():
    print(f"  Q: {q}")
    print(f"  A: {a}")
    print()
print()

# ========================================
# 3. 基础问答功能
# ========================================
print("📖 3. 基础问答功能")
print("-" * 50)
print()

def find_answer(question, knowledge):
    """在知识库中查找答案"""
    # 精确匹配
    if question in knowledge:
        return knowledge[question]

    # 模糊匹配 - 检查问题是否包含关键词
    question_lower = question.lower()
    for q, a in knowledge.items():
        if question_lower in q.lower() or q.lower() in question_lower:
            return a

    return None

def ask_question(question):
    """问一个问题"""
    answer = find_answer(question, knowledge_base)
    if answer:
        print(f"🤖: {answer}")
    else:
        print(f"🤖: 抱歉，我不知道这个问题的答案。")
    return answer

print("测试问答：")
ask_question("你好")
ask_question("Python是什么")
ask_question("天气")
ask_question("你叫什么")
print()

# ========================================
# 4. 添加新问题
# ========================================
print("📖 4. 添加新问题")
print("-" * 50)
print()

def add_knowledge(question, answer):
    """添加新问题到知识库"""
    if question in knowledge_base:
        print(f"🤖: 这个问题已经存在，原答案是：{knowledge_base[question]}")
        confirm = input("要更新吗？(y/n)：")
        if confirm.lower() != 'y':
            return False

    knowledge_base[question] = answer
    print(f"✅ 已添加：Q: {question} → A: {answer}")
    return True

print("添加新问题：")
add_knowledge("你喜欢什么颜色", "我喜欢蓝色，像天空一样！")
ask_question("你喜欢什么颜色")
print()

# ========================================
# 5. 列出所有问题
# ========================================
print("📖 5. 列出所有问题")
print("-" * 50)
print()

def list_questions():
    """列出所有问题"""
    print(f"知识库共有 {len(knowledge_base)} 个问题：")
    print()
    for i, (q, a) in enumerate(knowledge_base.items(), 1):
        print(f"  {i}. Q: {q}")
        print(f"     A: {a}")
        print()

list_questions()

# ========================================
# 6. 保存和加载知识库
# ========================================
print("📖 6. 保存和加载知识库")
print("-" * 50)
print()

import json

def save_knowledge(filename='/tmp/qa_knowledge.json'):
    """保存知识库到文件"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(knowledge_base, f, ensure_ascii=False, indent=2)
    print(f"✅ 知识库已保存到 {filename}")

def load_knowledge(filename='/tmp/qa_knowledge.json'):
    """从文件加载知识库"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            loaded = json.load(f)
        knowledge_base.update(loaded)
        print(f"✅ 知识库已加载，共 {len(loaded)} 条")
    except FileNotFoundError:
        print("📁 文件不存在，使用默认知识库")
    except:
        print("❌ 加载失败")

# 保存
save_knowledge()
print()

# 添加更多问题
add_knowledge("学习Python难吗", "不难！Python是最适合初学者的编程语言！")
print()

# 保存后再加载验证
load_knowledge()
ask_question("学习Python难吗")
print()

# ========================================
# 7. 完整版本：交互式问答程序
# ========================================
print("📖 7. 完整版本：交互式问答程序")
print("-" * 50)
print()

def run_qa_system():
    """运行问答系统"""
    print("=" * 40)
    print("       🤖 小天才智能问答系统 🤖")
    print("=" * 40)
    print("欢迎使用智能问答系统！")
    print("输入'帮助'查看命令，输入'退出'结束")
    print()

    while True:
        try:
            user_input = input("你：").strip()

            if not user_input:
                continue

            if user_input in ['退出', 'exit', 'quit']:
                print("🤖: 再见！保存知识库中...")
                save_knowledge()
                print("🤖: 已保存！下次见！")
                break

            elif user_input in ['帮助', 'help']:
                print("""
🤖 命令帮助：
  - 直接输入问题，我会尽力回答
  - '添加' + 问题 + 答案 - 添加新知识
  - '列出' - 查看所有问题
  - '保存' - 保存知识库
  - '退出' - 退出程序
""")

            elif user_input == '列出':
                list_questions()

            elif user_input == '保存':
                save_knowledge()

            elif user_input.startswith('添加'):
                # 格式：添加 问题 | 答案
                parts = user_input[2:].strip()
                if '|' in parts:
                    q, a = parts.split('|', 1)
                    add_knowledge(q.strip(), a.strip())
                else:
                    print("格式：请用'添加 问题 | 答案'")

            else:
                answer = find_answer(user_input, knowledge_base)
                if answer:
                    print(f"🤖: {answer}")
                else:
                    print("🤖: 抱歉，我不知道这个问题的答案。")
                    new_answer = input("你可以教我吗？(输入答案或直接回车跳过)：")
                    if new_answer.strip():
                        add_knowledge(user_input, new_answer.strip())

        except EOFError:
            print("（非交互环境）")
            break

# 演示
print("--- 系统演示 ---")
ask_question("你好")
ask_question("Python是什么")
ask_question("学习Python难吗")
print()

# ========================================
# 8. Day 20 总结
# ========================================
print("=" * 60)
print("       📋 Day 20 总结")
print("=" * 60)
print()
print("今天我们完成了：")
print("  ✅ 智能问答程序 - 基础版")
print("  ✅ 问题匹配功能（精确匹配 + 模糊匹配）")
print("  ✅ 添加新问题功能")
print("  ✅ 列出所有问题")
print("  ✅ 文件保存和加载（JSON格式）")
print("  ✅ 完整的交互式问答系统")
print()

print("🎯 课后挑战：")
print("  1. 添加更多问题到知识库")
print("  2. 添加'删除问题'功能")
print("  3. 添加'搜索'功能（按关键词搜索）")
print("  4. 添加'统计'功能（回答了多少问题）")
print()

print("=" * 60)
print("       🎉 Day 20 完成！")
print("=" * 60)
print()
print("太棒了！明天我们将完成最后的毕业设计！")
print()
print("===========================================")
print("     💪 继续加油！学习进度：20/21 天完成！")
print("===========================================")
